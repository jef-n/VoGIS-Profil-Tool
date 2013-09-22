# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VoGISProfilToolMainDialog
                                 A QGIS plugin
 VoGIS ProfilTool
                             -------------------
        begin                : 2013-05-28
        copyright            : (C) 2013 by BergWerk GIS
        email                : wb@BergWerk-GIS.at
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.core import *
from random import randrange
from ui.ui_vogisprofiltoolplot import Ui_VoGISProfilToolPlot
from bo.plotExtent import PlotExtent
from util.u import Util
from util.exportShape import ExportShape
from util.exportDxf import ExportDxf
import locale
#import ogr
import matplotlib
from matplotlib.figure import Figure
from matplotlib.lines import Line2D
from matplotlib.collections import LineCollection
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg


class VoGISProfilToolPlotDialog(QDialog):
    def __init__(self, interface, settings, profiles):

        QDialog.__init__(self, interface.mainWindow())
        self.iface = interface
        self.settings = settings
        self.profiles = profiles
        # Set up the user interface from Designer.
        self.ui = Ui_VoGISProfilToolPlot()
        self.ui.setupUi(self)

        if self.settings.onlyHektoMode is True:
            self.ui.IDC_frPlot.hide()
            self.ui.IDC_frToolbar.hide()
            self.adjustSize()
            self.ui.IDC_chkHekto.setCheckState(Qt.Checked)
            self.ui.IDC_chkHekto.setEnabled(False)

        #self.filePath = ''
        self.filePath = QSettings().value("vogisprofiltoolmain/savepath", "").toString()

        #nimmt die Locale vom System, nicht von QGIS
        #kein Weg gefunden, um QGIS Locale: QSettings().value("locale/userLocale")
        #zu initialisieren, nur um Dezimaltrenne auszulesen
        #QgsMessageLog.logMessage('QGIS Locale:{0}'.format(QSettings().value("locale/userLocale").toString()), 'VoGis')
        #!!!nl_langinfo not available on Windows!!!
        #http://docs.python.org/2.7/library/locale.html#locale.nl_langinfo
        # ...  This function is not available on all systems ...
        #decimalDelimiter = locale.nl_langinfo(locale.RADIXCHAR)
        decimalDelimiter = locale.localeconv()['decimal_point']
        QgsMessageLog.logMessage('delimiter:{0}'.format(decimalDelimiter), 'VoGis')
        idx = self.ui.IDC_cbDecimalDelimiter.findText(decimalDelimiter, Qt.MatchExactly)
        QgsMessageLog.logMessage('idx:{0}'.format(idx), 'VoGis')
        self.ui.IDC_cbDecimalDelimiter.setCurrentIndex(idx)

        pltExt = PlotExtent()
        for p in self.profiles:
            pltExt.union(p.getExtent())
            #QgsMessageLog.logMessage(pltExt.toString(), 'VoGis')

        pltExt.expand()
        self.origPltExt = PlotExtent(pltExt.xmin, pltExt.ymin, pltExt.xmax, pltExt.ymax)
        self.pltWidget = self.__createMatplotlibCanvas(pltExt)
        layout = self.ui.IDC_frPlot.layout()
        #QgsMessageLog.logMessage('layout: {0}'.format(layout), 'VoGis')
        layout.addWidget(self.pltWidget)
        pltToolbar = matplotlib.backends.backend_qt4agg.NavigationToolbar2QTAgg(self.pltWidget, self.ui.IDC_frPlot)
        self.ui.IDC_frToolbar.layout().addWidget(pltToolbar)
        lstActions = pltToolbar.actions()

        #QgsMessageLog.logMessage('{0}'.format(dir(lstActions[0])), 'VoGis')
        #i = QIcon()
        #i.addPixmap(QPixmap(":/plugins/vogisprofiltoolmain/icons/home.png"), QIcon.Normal, QIcon.Off)
        #lstActions[0].setIcon(i)
        lstActions[0].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/home.png"))
        #lstActions[0].setWhatsThis("Configuration for test plugin")
        #lstActions[0].setStatusTip("This is status tip")
        lstActions[1].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/zoomlast.png"))
        lstActions[2].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/zoomnext.png"))
        lstActions[4].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/pan.png"))
        lstActions[5].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/zoomselect.png"))
        lstActions[9].setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/save.png"))
        pltToolbar.removeAction(lstActions[7])
        pltToolbar.removeAction(lstActions[8])
        #insert 1:1 zoom button
        self.one2one = QPushButton()
        self.one2one.setText('1:1')
        self.one2one.clicked.connect(self.__one2oneClicked)
        #pltToolbar.addWidget(self.one2one)
        #insert QLineEdit to change the exaggeration
        #catch updating of figure, when exaggeration QLineEdit has been updated from draw_event of figure
        self.drawEventFired = False
        #catch closing of dialog, when enter key has been used accept exaggeration edit field
        self.exaggerationEdited = False
        self.editExaggeration = QLineEdit()
        self.editExaggeration.setFixedWidth(60)
        self.editExaggeration.setMaximumWidth(60)
        pltToolbar.insertWidget(lstActions[0], self.editExaggeration)
        self.editExaggeration.editingFinished.connect(self.__exaggerationEdited)
        #insert identify button -> deactivate all tools
        pltToolbar.insertWidget(lstActions[0], self.one2one)
        self.identify = QPushButton()
        self.identify.setIcon(QIcon(":/plugins/vogisprofiltoolmain/icons/identify.png"))
        self.identify.clicked.connect(self.__identify)
        pltToolbar.insertWidget(lstActions[0], self.identify)
        #insert identify label to show name of clicked dhm
        self.dhmLbl = QLabel()
        pltToolbar.insertWidget(lstActions[0], self.dhmLbl)
        #measure in figure
        self.click1 = None
        self.click2 = None
        self.measureLbl = QLabel()
        self.measureLbl.setText(u' 1:? 2:? ')
        pltToolbar.insertWidget(lstActions[0], self.measureLbl)

        #for less thatn 10 colors:
        #alternative method: http://stackoverflow.com/a/14720445
        colors = [(1.0, 0.0, 0.0, 1.0),
                  (0.0, 1.0, 0.0, 1.0),
                  (0.0, 0.0, 1.0, 1.0),
                  (1.0, 1.0, 0.5, 1.0),
                  (1.0, 0.0, 1.0, 1.0),
                  (0.0, 1.0, 1.0, 1.0),
                  (0.415686275, 0.807843137, 0.890196078, 1.0),
                  (0.121568627, 0.470588235, 0.705882353, 1.0),
                  (0.698039216, 0.874509804, 0.541176471, 1.0),
                  (0.2, 0.62745098, 0.17254902, 1.0),
                  (0.984313725, 0.603921569, 0.6, 1.0),
                  (0.890196078, 0.101960784, 0.109803922, 1.0),
                  (0.992156863, 0.749019608, 0.435294118, 1.0),
                  (1, 0.498039216, 0, 1.0),
                  (0.792156863, 0.698039216, 0.839215686, 1.0),
                  (0.415686275, 0.239215686, 0.603921569, 1.0),
                  (1, 1, 0.521568627, 1.0),
                  ]

        #idxCol = 0
        for idx, p in enumerate(self.profiles):
            #if idxCol > len(colors) - 1:
            #    idxCol = 0
            #x, pltSegs = p.getPlotSegments()
            #QgsMessageLog.logMessage('x: {0}'.format(x), 'VoGis')
            pltSegs = p.getPlotSegments()
            #QgsMessageLog.logMessage('pltSegs: {0}'.format(pltSegs), 'VoGis')
            lineColl = LineCollection(pltSegs,
                                      linewidths=2,
                                      linestyles='solid',
                                      #colors=colors[randrange(len(colors))],
                                      #colors=colors[idxCol],
                                      colors=colors[:len(settings.mapData.rasters.selectedRasters())],
                                      picker=True,
                                      label='LBL'
                                      )
            #lineColl.set_array(x)
            #lineColl.text.set_text('line label')
            self.subplot.add_collection(lineColl)
            #idxCol += 1
        #save inital view in history
        pltToolbar.push_current()
        #select pan tool
        pltToolbar.pan()
        self.pltToolbar = pltToolbar
        QApplication.restoreOverrideCursor()

    def accept(self):
        #QMessageBox.warning(self.iface.mainWindow(), "VoGIS-Profiltool", "ACCEPTED")
        QgsMessageLog.logMessage('accept: {0}'.format(self.exaggerationEdited), 'VoGis')
        if self.exaggerationEdited is True:
            self.exaggerationEdited = False
            return
        QDialog.accept(self)

    def reject(self):
        #QMessageBox.warning(self.iface.mainWindow(), "VoGIS-Profiltool", "REJECTED")
        QgsMessageLog.logMessage('reject: {0}'.format(self.exaggerationEdited), 'VoGis')
        if self.exaggerationEdited is True:
            self.exaggerationEdited = False
            return
        QDialog.reject(self)

    def exportShpPnt(self):
        self.__exportShp(True)

    def exportShpLine(self):
        self.__exportShp(False)

    def __exportShp(self, asPnt):

        u = Util(self.iface)
        if asPnt is True:
            caption = QApplication.translate('code', 'Punkt Shapefile exportieren', None, QApplication.UnicodeUTF8)
        else:
            caption = QApplication.translate('code', 'Linien Shapefile exportieren', None, QApplication.UnicodeUTF8)
        fileName = u.getFileName(caption, "SHP (*.shp)", self.filePath)
        if fileName == '':
            return
        fInfo = QFileInfo(fileName)
        self.filePath = fInfo.path()
        QSettings().setValue("vogisprofiltoolmain/savepath", self.filePath)
        expShp = ExportShape(self.iface,
                             (self.ui.IDC_chkHekto.checkState() == Qt.Checked),
                             (self.ui.IDC_chkLineAttributes.checkState() == Qt.Checked),
                             self.__getDelimiter(),
                             self.__getDecimalDelimiter(),
                             fileName,
                             self.settings,
                             self.profiles
                             )
        if asPnt is False:
            expShp.exportLine()
        else:
            expShp.exportPoint()

    def exportCsvXls(self):
        u = Util(self.iface)
        caption = QApplication.translate('code', 'CSV-datei exportieren', None, QApplication.UnicodeUTF8)
        fileName = u.getFileName(caption, "CSV (*.csv)", self.filePath)
        if fileName == '':
            return
        fInfo = QFileInfo(fileName)
        self.filePath = fInfo.path()
        QSettings().setValue("vogisprofiltoolmain/savepath", self.filePath)
        hekto = (self.ui.IDC_chkHekto.checkState() == Qt.Checked)
        attribs = (self.ui.IDC_chkLineAttributes.checkState() == Qt.Checked)
        delimiter = ';'
        decimalDelimiter = self.__getDecimalDelimiter()

        txt = open(fileName, 'w')

        txt.write(self.profiles[0].writeHeader(self.settings.mapData.rasters.selectedRasters(), hekto, attribs, delimiter))
        for p in self.profiles:
            #txt.write('=====Profil {0}======\r\n'.format(p.id))
            #txt.write('Segments:{0}\r\n'.format(len(p.segments)))
            #for s in p.segments:
            #    txt.write('Vertices:{0}\r\n'.format(len(s.vertices)))
            txt.write(p.toString(hekto,
                                 attribs,
                                 delimiter,
                                 decimalDelimiter
                                 ))

    def exportTxt(self):
        delimiter = self.__getDelimiter()
        decimalDelimiter = self.__getDecimalDelimiter()
        if delimiter == decimalDelimiter:
            msg = QApplication.translate('code', 'Gleiches Dezimal- und Spaltentrennzeichen gewählt!', None, QApplication.UnicodeUTF8)
            QMessageBox.warning(self.iface.mainWindow(), 'VoGIS-Profiltool', msg)
            return

        u = Util(self.iface)
        caption = QApplication.translate('code', 'Textdatei exportieren', None, QApplication.UnicodeUTF8)
        fileName = u.getFileName(caption, "TXT (*.txt)", self.filePath)
        if fileName == '':
            return
        fInfo = QFileInfo(fileName)
        self.filePath = fInfo.path()
        QSettings().setValue("vogisprofiltoolmain/savepath", self.filePath)
        hekto = (self.ui.IDC_chkHekto.checkState() == Qt.Checked)
        attribs = (self.ui.IDC_chkLineAttributes.checkState() == Qt.Checked)
        txt = open(fileName, 'w')

        txt.write(self.profiles[0].writeHeader(self.settings.mapData.rasters.selectedRasters(), hekto, attribs, delimiter))
        for p in self.profiles:
            #txt.write('=====Profil {0}======\r\n'.format(p.id))
            #txt.write('Segments:{0}\r\n'.format(len(p.segments)))
            #for s in p.segments:
            #    txt.write('Vertices:{0}\r\n'.format(len(s.vertices)))
            txt.write(p.toString(hekto,
                                 attribs,
                                 delimiter,
                                 decimalDelimiter
                                 ))

        txt.close()

    def exportAutoCadTxt(self):
        u = Util(self.iface)
        caption = QApplication.translate('code', 'AutoCad Textdatei exportieren', None, QApplication.UnicodeUTF8)
        fileName = u.getFileName(caption, "TXT (*.txt)", self.filePath)
        if fileName == '':
            return
        fInfo = QFileInfo(fileName)
        self.filePath = fInfo.path()
        QSettings().setValue("vogisprofiltoolmain/savepath", self.filePath)
        txt = open(fileName, 'w')
        for p in self.profiles:
            txt.write(p.toACadTxt(' ', '.'))
        txt.close()

    def exportDxfPnt(self):
        self.__exportDxf(True)

    def exportDxfLine(self):
        self.__exportDxf(False)

    def __exportDxf(self, asPnt):
        u = Util(self.iface)
        caption = QApplication.translate('code', 'DXF exportieren', None, QApplication.UnicodeUTF8)
        fileName = u.getFileName(caption, "DXF (*.dxf)", self.filePath)
        if fileName == '':
            return
        fInfo = QFileInfo(fileName)
        self.filePath = fInfo.path()
        QSettings().setValue("vogisprofiltoolmain/savepath", self.filePath)
        exDxf = ExportDxf(self.iface, fileName, self.settings, self.profiles)
        if asPnt is True:
            exDxf.exportPoint()
        else:
            exDxf.exportLine()

    def __identify(self):
        #dirty hack: deselect all tools
        #selecting a tool twice deselects it
        self.pltToolbar.pan()
        self.pltToolbar.zoom()
        self.pltToolbar.zoom()

    def __figureDrawn(self, event):
        #QgsMessageLog.logMessage('draw_event: {0}'.format(self.exaggerationEdited), 'VoGis')
        axes = self.pltWidget.figure.get_axes()[0]
        xlim = axes.get_xlim()
        ylim = axes.get_ylim()
        #QgsMessageLog.logMessage('draw_event: xlim:{0} ylim:{1}'.format(xlim, ylim), 'VoGis')
        dpi = self.pltWidget.figure.get_dpi()
        figWidth = self.pltWidget.figure.get_figwidth() * dpi
        figHeight = self.pltWidget.figure.get_figheight() * dpi
        deltaX = xlim[1] - xlim[0]
        deltaY = ylim[1] - ylim[0]
        ratio = (deltaX / figWidth) / (deltaY / figHeight)
        self.drawEventFired = True
        self.editExaggeration.setText('{0:.1f}'.format(ratio))
        self.drawEventFired = False

    def __exaggerationEdited(self, *args):
        if self.drawEventFired is True:
            return
        self.exaggerationEdited = True
        #QgsMessageLog.logMessage('__exaggerationEdited: {0}'.format(self.exaggerationEdited), 'VoGis')
        ut = Util(self.iface)
        txtExa = QApplication.translate('code', 'Überhöhung', None, QApplication.UnicodeUTF8)
        if ut.isFloat(self.editExaggeration.text(), txtExa) is False:
            return False
        #clear focus of lineedit, otherwise it gets called even when the user wants to close the dialog
        self.editExaggeration.clearFocus()
        exa = float(self.editExaggeration.text().replace(',', '.'))
        self.__adjustAxes(exa)

    def __one2oneClicked(self):
        #QgsMessageLog.logMessage('1:1 clicked', 'VoGis')
        #QgsMessageLog.logMessage('axes:{0}'.format(self.pltWidget.figure.get_axes()), 'VoGis')
        self.__adjustAxes(1.0)

    def __adjustAxes(self, exaggeration):
        dpi = self.pltWidget.figure.get_dpi()
        figWidth = self.pltWidget.figure.get_figwidth() * dpi
        figHeight = self.pltWidget.figure.get_figheight() * dpi
        QgsMessageLog.logMessage('dataExtent:{0}'.format(self.origPltExt.toString()), 'VoGis')
        QgsMessageLog.logMessage('fig size:{0}/{1}'.format(figWidth, figHeight), 'VoGis')
        mPerPixH = self.origPltExt.xmax / figWidth
        deltaVnew = figHeight * mPerPixH / exaggeration
        newYmax = self.origPltExt.ymin + deltaVnew
        #QgsMessageLog.logMessage('mPerPixH:{0} deltaV:{1} deltaVnew:{2} newYmax:{3}'.format(mPerPixH, deltaV, deltaVnew, newYmax), 'VoGis')
        #self.pltWidget.figure.get_axes()[0].set_xbound(self.origPltExt.xmin, self.origPltExt.xmax)
        #self.pltWidget.figure.get_axes()[0].set_ybound(self.origPltExt.ymin, newYmax)
        self.pltWidget.figure.get_axes()[0].set_xlim((self.origPltExt.xmin, self.origPltExt.xmax))
        self.pltWidget.figure.get_axes()[0].set_ylim((self.origPltExt.ymin, newYmax))
        self.pltWidget.figure.get_axes()[0].redraw_in_frame()
        self.pltWidget.draw()

    def __plotPicked(self, event):
        #QgsMessageLog.logMessage('artist:{0}'.format(type(event.artist)), 'VoGis')
        self.dhmLbl.setText(' ? ')
        if isinstance(event.artist, Line2D):
            QgsMessageLog.logMessage('Line2D', 'VoGis')
            line = event.artist
            xdata = line.get_xdata()
            ydata = line.get_ydata()
            ind = event.ind
            QgsMessageLog.logMessage('{0}: {1} {2}'.format(ind, xdata, ydata), 'VoGis')
            QgsMessageLog.logMessage(help(line), 'VoGis')
        elif isinstance(event.artist, LineCollection):
            QgsMessageLog.logMessage('LineCollection', 'VoGis')
            r = self.settings.mapData.rasters.selectedRasters()[event.ind[0]]
            QgsMessageLog.logMessage('Raster: {0}'.format(r.name), 'VoGis')
            #self.pltWidget.figure.suptitle(r.name)
            self.dhmLbl.setText(u'  [' + r.name + '] ')
            #QgsMessageLog.logMessage('{0}'.format(event), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.artist), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.artist)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.canvas), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.canvas)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.guiEvent), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.guiEvent)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.ind), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.ind)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.mouseevent), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.mouseevent)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(event.name), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(dir(event.name)), 'VoGis')
            #lColl = event.artist
            #QgsMessageLog.logMessage('{0}'.format(lColl.get_array()), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(lColl.get_paths()[event.ind[0]]), 'VoGis')
            #segs = lColl.get_segments()
            #l = segs[ind]
            #QgsMessageLog.logMessage('{0}'.format(l.get_data(True)), 'VoGis')
            #QgsMessageLog.logMessage('{0}'.format(l.get_data()), 'VoGis')
        else:
            QgsMessageLog.logMessage('no Line2D or LineCollection', 'VoGis')

    def __buttonPressed(self, event):
        #QgsMessageLog.logMessage('x:{0} y:{1} xdata:{2} ydata:{3}'.format(event.x, event.y, event.xdata, event.ydata), 'VoGis')
        if self.click1 is None:
            self.click1 = [event.xdata, event.ydata]
            self.click2 = None
            self.measureLbl.setText(u' 1:ok 2:? ')
        elif self.click2 is None:
            self.click2 = [event.xdata, event.ydata]
            deltaX = abs(self.click2[0] - self.click1[0])
            deltaY = abs(self.click2[1] - self.click1[1])
            dist = ((deltaX ** 2) + (deltaY ** 2)) ** 0.5
            self.measureLbl.setText(u' dist: {0:.1f} '.format(dist))
            self.click1 = None

    def __createMatplotlibCanvas(self, pltExt):
            fig = Figure((1.0, 1.0),
                         linewidth=0.0,
                         subplotpars=matplotlib.figure.SubplotParams(left=0,
                                                                     bottom=0,
                                                                     right=1,
                                                                     top=1,
                                                                     wspace=0,
                                                                     hspace=0
                                                                     )
                         )
            #font = {'family': 'arial', 'weight': 'normal', 'size': 12}
            #rc('font', **font)
            rect = fig.patch
            rect.set_facecolor((0.9, 0.9, 0.9))

            self.subplot = fig.add_axes((0.08, 0.15, 0.92, 0.82))
            self.subplot.set_xbound(pltExt.xmin, pltExt.xmax)
            self.subplot.set_ybound(pltExt.ymin, pltExt.ymax)
            self.__setupAxes(self.subplot)
            canvas = FigureCanvasQTAgg(fig)
            sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            canvas.setSizePolicy(sizePolicy)
            canvas.mpl_connect('pick_event', self.__plotPicked)
            canvas.mpl_connect('draw_event', self.__figureDrawn)
            canvas.mpl_connect('button_press_event', self.__buttonPressed)
            return canvas

    def __setupAxes(self, axe1):
        axe1.grid()
        axe1.tick_params(axis="both",
                         which="major",
                         direction="out",
                         length=10,
                         width=1,
                         bottom=True,
                         top=False,
                         left=True,
                         right=False
                         )
        axe1.minorticks_on()
        axe1.tick_params(axis="both",
                         which="minor",
                         direction="out",
                         length=5,
                         width=1,
                         bottom=True,
                         top=False,
                         left=True,
                         right=False
                         )

    def __getDecimalDelimiter(self):
        #delim = self.ui.IDC_cbDecimalDelimiter.itemData(self.ui.IDC_cbDecimalDelimiter.currentIndex())
        delim = self.ui.IDC_cbDecimalDelimiter.currentText()
        #QgsMessageLog.logMessage('delim:' + str(delim), 'VoGis')
        return delim

    def __getDelimiter(self):
        #delim = self.ui.IDC_cbDelimiter.itemData(self.ui.IDC_cbDelimiter.currentIndex())
        delim = self.ui.IDC_cbDelimiter.currentText()
        if delim == "tab":
            delim = '\t'
        return delim
