# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_vogisprofiltoolplot.ui'
#
# Created: Wed Aug 28 17:37:34 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VoGISProfilToolPlot(object):
    def setupUi(self, VoGISProfilToolPlot):
        VoGISProfilToolPlot.setObjectName(_fromUtf8("VoGISProfilToolPlot"))
        VoGISProfilToolPlot.resize(842, 393)
        VoGISProfilToolPlot.setModal(True)
        self.gridLayout_2 = QtGui.QGridLayout(VoGISProfilToolPlot)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.IDC_bClose = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bClose.setObjectName(_fromUtf8("IDC_bClose"))
        self.gridLayout.addWidget(self.IDC_bClose, 3, 8, 1, 1)
        self.IDC_bDxfLine = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bDxfLine.setObjectName(_fromUtf8("IDC_bDxfLine"))
        self.gridLayout.addWidget(self.IDC_bDxfLine, 3, 6, 1, 1)
        self.IDC_bDxfPnt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bDxfPnt.setObjectName(_fromUtf8("IDC_bDxfPnt"))
        self.gridLayout.addWidget(self.IDC_bDxfPnt, 3, 4, 1, 1)
        self.IDC_bShpPnt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bShpPnt.setObjectName(_fromUtf8("IDC_bShpPnt"))
        self.gridLayout.addWidget(self.IDC_bShpPnt, 3, 3, 1, 1)
        self.IDC_bExcel = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bExcel.setObjectName(_fromUtf8("IDC_bExcel"))
        self.gridLayout.addWidget(self.IDC_bExcel, 3, 7, 1, 1)
        self.IDC_bShpLine = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bShpLine.setObjectName(_fromUtf8("IDC_bShpLine"))
        self.gridLayout.addWidget(self.IDC_bShpLine, 3, 5, 1, 1)
        self.IDC_bACadTxt = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bACadTxt.setObjectName(_fromUtf8("IDC_bACadTxt"))
        self.gridLayout.addWidget(self.IDC_bACadTxt, 3, 2, 1, 1)
        self.IDC_bChart = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bChart.setObjectName(_fromUtf8("IDC_bChart"))
        self.gridLayout.addWidget(self.IDC_bChart, 3, 0, 1, 1)
        self.IDC_bText = QtGui.QPushButton(VoGISProfilToolPlot)
        self.IDC_bText.setObjectName(_fromUtf8("IDC_bText"))
        self.gridLayout.addWidget(self.IDC_bText, 3, 1, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.IDC_cbDecimalDelimiter = QtGui.QComboBox(VoGISProfilToolPlot)
        self.IDC_cbDecimalDelimiter.setObjectName(_fromUtf8("IDC_cbDecimalDelimiter"))
        self.IDC_cbDecimalDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDecimalDelimiter.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.IDC_cbDecimalDelimiter)
        self.IDC_cbDelimiter = QtGui.QComboBox(VoGISProfilToolPlot)
        self.IDC_cbDelimiter.setEditable(False)
        self.IDC_cbDelimiter.setObjectName(_fromUtf8("IDC_cbDelimiter"))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.addItem(_fromUtf8(""))
        self.IDC_cbDelimiter.setItemText(3, _fromUtf8(""))
        self.horizontalLayout.addWidget(self.IDC_cbDelimiter)
        self.IDC_chkHekto = QtGui.QCheckBox(VoGISProfilToolPlot)
        self.IDC_chkHekto.setObjectName(_fromUtf8("IDC_chkHekto"))
        self.horizontalLayout.addWidget(self.IDC_chkHekto)
        self.IDC_chkLineAttributes = QtGui.QCheckBox(VoGISProfilToolPlot)
        self.IDC_chkLineAttributes.setChecked(True)
        self.IDC_chkLineAttributes.setObjectName(_fromUtf8("IDC_chkLineAttributes"))
        self.horizontalLayout.addWidget(self.IDC_chkLineAttributes)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 9)
        self.IDC_frPlot = QtGui.QFrame(VoGISProfilToolPlot)
        self.IDC_frPlot.setFrameShape(QtGui.QFrame.StyledPanel)
        self.IDC_frPlot.setFrameShadow(QtGui.QFrame.Raised)
        self.IDC_frPlot.setObjectName(_fromUtf8("IDC_frPlot"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.IDC_frPlot)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout.addWidget(self.IDC_frPlot, 0, 0, 1, 9)
        self.IDC_frToolbar = QtGui.QFrame(VoGISProfilToolPlot)
        self.IDC_frToolbar.setFrameShape(QtGui.QFrame.StyledPanel)
        self.IDC_frToolbar.setFrameShadow(QtGui.QFrame.Raised)
        self.IDC_frToolbar.setObjectName(_fromUtf8("IDC_frToolbar"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.IDC_frToolbar)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.gridLayout.addWidget(self.IDC_frToolbar, 1, 0, 1, 9)
        self.gridLayout_2.addLayout(self.gridLayout, 11, 0, 1, 1)

        self.retranslateUi(VoGISProfilToolPlot)
        QtCore.QObject.connect(self.IDC_bClose, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.reject)
        QtCore.QObject.connect(self.IDC_bText, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportTxt)
        QtCore.QObject.connect(self.IDC_bShpPnt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportShpPnt)
        QtCore.QObject.connect(self.IDC_bShpLine, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportShpLine)
        QtCore.QObject.connect(self.IDC_bExcel, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportCsvXls)
        QtCore.QObject.connect(self.IDC_bACadTxt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportAutoCadTxt)
        QtCore.QObject.connect(self.IDC_bDxfPnt, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportDxfPnt)
        QtCore.QObject.connect(self.IDC_bDxfLine, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolPlot.exportDxfLine)
        QtCore.QMetaObject.connectSlotsByName(VoGISProfilToolPlot)

    def retranslateUi(self, VoGISProfilToolPlot):
        VoGISProfilToolPlot.setWindowTitle(QtGui.QApplication.translate("VoGISProfilToolPlot", "Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bClose.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Schließen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bDxfLine.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "DXF Linie", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bDxfPnt.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "DXF Punkt", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bShpPnt.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Shp Punkt", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bExcel.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "csv (Excel)", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bShpLine.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Shp Linie", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bACadTxt.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Autocad Text", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bChart.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Grafik", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bText.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Textdatei", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_cbDecimalDelimiter.setItemText(0, QtGui.QApplication.translate("VoGISProfilToolPlot", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_cbDecimalDelimiter.setItemText(1, QtGui.QApplication.translate("VoGISProfilToolPlot", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_cbDelimiter.setItemText(0, QtGui.QApplication.translate("VoGISProfilToolPlot", "tab", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_cbDelimiter.setItemText(1, QtGui.QApplication.translate("VoGISProfilToolPlot", ";", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_cbDelimiter.setItemText(2, QtGui.QApplication.translate("VoGISProfilToolPlot", ",", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkHekto.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Hektometrie Attribute", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkLineAttributes.setText(QtGui.QApplication.translate("VoGISProfilToolPlot", "Linien Attribute", None, QtGui.QApplication.UnicodeUTF8))

