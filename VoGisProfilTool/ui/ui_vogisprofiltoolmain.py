# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/ui_vogisprofiltoolmain.ui'
#
# Created: Wed Dec 11 19:27:26 2013
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VoGISProfilToolMain(object):
    def setupUi(self, VoGISProfilToolMain):
        VoGISProfilToolMain.setObjectName(_fromUtf8("VoGISProfilToolMain"))
        VoGISProfilToolMain.resize(463, 893)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(VoGISProfilToolMain.sizePolicy().hasHeightForWidth())
        VoGISProfilToolMain.setSizePolicy(sizePolicy)
        self.gridLayout = QtGui.QGridLayout(VoGISProfilToolMain)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.IDC_widRaster = QtGui.QWidget(VoGISProfilToolMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_widRaster.sizePolicy().hasHeightForWidth())
        self.IDC_widRaster.setSizePolicy(sizePolicy)
        self.IDC_widRaster.setObjectName(_fromUtf8("IDC_widRaster"))
        self.gridLayout_2 = QtGui.QGridLayout(self.IDC_widRaster)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.IDC_grpRaster = QtGui.QGroupBox(self.IDC_widRaster)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_grpRaster.sizePolicy().hasHeightForWidth())
        self.IDC_grpRaster.setSizePolicy(sizePolicy)
        self.IDC_grpRaster.setObjectName(_fromUtf8("IDC_grpRaster"))
        self.gridLayout_3 = QtGui.QGridLayout(self.IDC_grpRaster)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.IDC_listRasters = QtGui.QListWidget(self.IDC_grpRaster)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_listRasters.sizePolicy().hasHeightForWidth())
        self.IDC_listRasters.setSizePolicy(sizePolicy)
        self.IDC_listRasters.setObjectName(_fromUtf8("IDC_listRasters"))
        self.gridLayout_3.addWidget(self.IDC_listRasters, 2, 0, 1, 1)
        self.IDC_bSelectVisibleRasters = QtGui.QPushButton(self.IDC_grpRaster)
        self.IDC_bSelectVisibleRasters.setObjectName(_fromUtf8("IDC_bSelectVisibleRasters"))
        self.gridLayout_3.addWidget(self.IDC_bSelectVisibleRasters, 0, 0, 1, 1)
        self.IDC_bRefreshRasterList = QtGui.QPushButton(self.IDC_grpRaster)
        self.IDC_bRefreshRasterList.setObjectName(_fromUtf8("IDC_bRefreshRasterList"))
        self.gridLayout_3.addWidget(self.IDC_bRefreshRasterList, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.IDC_grpRaster, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.IDC_widRaster)
        self.IDC_widProfilLinien = QtGui.QWidget(VoGISProfilToolMain)
        self.IDC_widProfilLinien.setObjectName(_fromUtf8("IDC_widProfilLinien"))
        self.gridLayout_4 = QtGui.QGridLayout(self.IDC_widProfilLinien)
        self.gridLayout_4.setMargin(0)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.IDC_grpProfilLinien = QtGui.QGroupBox(self.IDC_widProfilLinien)
        self.IDC_grpProfilLinien.setObjectName(_fromUtf8("IDC_grpProfilLinien"))
        self.gridLayout_5 = QtGui.QGridLayout(self.IDC_grpProfilLinien)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.IDC_bDrawLine = QtGui.QPushButton(self.IDC_grpProfilLinien)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_bDrawLine.sizePolicy().hasHeightForWidth())
        self.IDC_bDrawLine.setSizePolicy(sizePolicy)
        self.IDC_bDrawLine.setObjectName(_fromUtf8("IDC_bDrawLine"))
        self.gridLayout_5.addWidget(self.IDC_bDrawLine, 4, 0, 1, 1)
        self.IDC_chkOnlySelectedFeatures = QtGui.QCheckBox(self.IDC_grpProfilLinien)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_chkOnlySelectedFeatures.sizePolicy().hasHeightForWidth())
        self.IDC_chkOnlySelectedFeatures.setSizePolicy(sizePolicy)
        self.IDC_chkOnlySelectedFeatures.setObjectName(_fromUtf8("IDC_chkOnlySelectedFeatures"))
        self.gridLayout_5.addWidget(self.IDC_chkOnlySelectedFeatures, 8, 0, 1, 1)
        self.IDC_chkLinesExplode = QtGui.QCheckBox(self.IDC_grpProfilLinien)
        self.IDC_chkLinesExplode.setChecked(True)
        self.IDC_chkLinesExplode.setObjectName(_fromUtf8("IDC_chkLinesExplode"))
        self.gridLayout_5.addWidget(self.IDC_chkLinesExplode, 1, 0, 1, 1)
        self.IDC_cbLineLayers = QtGui.QComboBox(self.IDC_grpProfilLinien)
        self.IDC_cbLineLayers.setMinimumSize(QtCore.QSize(150, 0))
        self.IDC_cbLineLayers.setObjectName(_fromUtf8("IDC_cbLineLayers"))
        self.gridLayout_5.addWidget(self.IDC_cbLineLayers, 7, 0, 1, 1)
        self.IDC_rbShapeLine = QtGui.QRadioButton(self.IDC_grpProfilLinien)
        self.IDC_rbShapeLine.setChecked(True)
        self.IDC_rbShapeLine.setObjectName(_fromUtf8("IDC_rbShapeLine"))
        self.gridLayout_5.addWidget(self.IDC_rbShapeLine, 6, 0, 1, 2)
        self.IDC_rbDigi = QtGui.QRadioButton(self.IDC_grpProfilLinien)
        self.IDC_rbDigi.setObjectName(_fromUtf8("IDC_rbDigi"))
        self.gridLayout_5.addWidget(self.IDC_rbDigi, 3, 0, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.IDC_grpProfilLinien)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.gridLayout_7 = QtGui.QGridLayout(self.groupBox)
        self.gridLayout_7.setObjectName(_fromUtf8("gridLayout_7"))
        self.IDC_tbFromX = QtGui.QLineEdit(self.groupBox)
        self.IDC_tbFromX.setObjectName(_fromUtf8("IDC_tbFromX"))
        self.gridLayout_7.addWidget(self.IDC_tbFromX, 1, 1, 1, 1)
        self.IDC_tbFromY = QtGui.QLineEdit(self.groupBox)
        self.IDC_tbFromY.setObjectName(_fromUtf8("IDC_tbFromY"))
        self.gridLayout_7.addWidget(self.IDC_tbFromY, 1, 2, 1, 1)
        self.IDC_tbToX = QtGui.QLineEdit(self.groupBox)
        self.IDC_tbToX.setObjectName(_fromUtf8("IDC_tbToX"))
        self.gridLayout_7.addWidget(self.IDC_tbToX, 2, 1, 1, 1)
        self.IDC_tbToY = QtGui.QLineEdit(self.groupBox)
        self.IDC_tbToY.setMaxLength(17)
        self.IDC_tbToY.setCursorPosition(0)
        self.IDC_tbToY.setObjectName(_fromUtf8("IDC_tbToY"))
        self.gridLayout_7.addWidget(self.IDC_tbToY, 2, 2, 1, 1)
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_7.addWidget(self.label, 1, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout_7.addWidget(self.label_2, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout_7.addWidget(self.label_3, 0, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_7.addWidget(self.label_4, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox, 10, 0, 1, 1)
        self.IDC_chkLinesMerge = QtGui.QCheckBox(self.IDC_grpProfilLinien)
        self.IDC_chkLinesMerge.setChecked(True)
        self.IDC_chkLinesMerge.setObjectName(_fromUtf8("IDC_chkLinesMerge"))
        self.gridLayout_5.addWidget(self.IDC_chkLinesMerge, 2, 0, 1, 1)
        self.IDC_rbStraigthLine = QtGui.QRadioButton(self.IDC_grpProfilLinien)
        self.IDC_rbStraigthLine.setObjectName(_fromUtf8("IDC_rbStraigthLine"))
        self.gridLayout_5.addWidget(self.IDC_rbStraigthLine, 9, 0, 1, 1)
        self.gridLayout_4.addWidget(self.IDC_grpProfilLinien, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.IDC_widProfilLinien)
        self.IDC_widVertices = QtGui.QWidget(VoGISProfilToolMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_widVertices.sizePolicy().hasHeightForWidth())
        self.IDC_widVertices.setSizePolicy(sizePolicy)
        self.IDC_widVertices.setObjectName(_fromUtf8("IDC_widVertices"))
        self.gridLayout_6 = QtGui.QGridLayout(self.IDC_widVertices)
        self.gridLayout_6.setMargin(0)
        self.gridLayout_6.setObjectName(_fromUtf8("gridLayout_6"))
        self.IDC_grpVertices = QtGui.QGroupBox(self.IDC_widVertices)
        self.IDC_grpVertices.setObjectName(_fromUtf8("IDC_grpVertices"))
        self.gridLayout_8 = QtGui.QGridLayout(self.IDC_grpVertices)
        self.gridLayout_8.setObjectName(_fromUtf8("gridLayout_8"))
        self.IDC_rbEquiDistance = QtGui.QRadioButton(self.IDC_grpVertices)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_rbEquiDistance.sizePolicy().hasHeightForWidth())
        self.IDC_rbEquiDistance.setSizePolicy(sizePolicy)
        self.IDC_rbEquiDistance.setChecked(True)
        self.IDC_rbEquiDistance.setObjectName(_fromUtf8("IDC_rbEquiDistance"))
        self.gridLayout_8.addWidget(self.IDC_rbEquiDistance, 0, 0, 1, 1)
        self.IDC_dblspinDistance = QtGui.QDoubleSpinBox(self.IDC_grpVertices)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_dblspinDistance.sizePolicy().hasHeightForWidth())
        self.IDC_dblspinDistance.setSizePolicy(sizePolicy)
        self.IDC_dblspinDistance.setMaximumSize(QtCore.QSize(70, 16777215))
        self.IDC_dblspinDistance.setDecimals(3)
        self.IDC_dblspinDistance.setMinimum(0.001)
        self.IDC_dblspinDistance.setMaximum(1000000.0)
        self.IDC_dblspinDistance.setProperty("value", 10.0)
        self.IDC_dblspinDistance.setObjectName(_fromUtf8("IDC_dblspinDistance"))
        self.gridLayout_8.addWidget(self.IDC_dblspinDistance, 0, 1, 1, 1)
        self.IDC_rbVertexCount = QtGui.QRadioButton(self.IDC_grpVertices)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.IDC_rbVertexCount.sizePolicy().hasHeightForWidth())
        self.IDC_rbVertexCount.setSizePolicy(sizePolicy)
        self.IDC_rbVertexCount.setObjectName(_fromUtf8("IDC_rbVertexCount"))
        self.gridLayout_8.addWidget(self.IDC_rbVertexCount, 1, 0, 1, 1)
        self.IDC_dblspinVertexCnt = QtGui.QDoubleSpinBox(self.IDC_grpVertices)
        self.IDC_dblspinVertexCnt.setMaximumSize(QtCore.QSize(70, 16777215))
        self.IDC_dblspinVertexCnt.setDecimals(0)
        self.IDC_dblspinVertexCnt.setMinimum(2.0)
        self.IDC_dblspinVertexCnt.setMaximum(1000000.0)
        self.IDC_dblspinVertexCnt.setProperty("value", 100.0)
        self.IDC_dblspinVertexCnt.setObjectName(_fromUtf8("IDC_dblspinVertexCnt"))
        self.gridLayout_8.addWidget(self.IDC_dblspinVertexCnt, 1, 1, 1, 1)
        self.IDC_chkNodesAndVertices = QtGui.QCheckBox(self.IDC_grpVertices)
        self.IDC_chkNodesAndVertices.setChecked(True)
        self.IDC_chkNodesAndVertices.setObjectName(_fromUtf8("IDC_chkNodesAndVertices"))
        self.gridLayout_8.addWidget(self.IDC_chkNodesAndVertices, 2, 0, 1, 1)
        self.gridLayout_6.addWidget(self.IDC_grpVertices, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.IDC_widVertices)
        self.buttonBox = QtGui.QDialogButtonBox(VoGISProfilToolMain)
        self.buttonBox.setEnabled(True)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(VoGISProfilToolMain)
        QtCore.QObject.connect(self.IDC_listRasters, QtCore.SIGNAL(_fromUtf8("itemChanged(QListWidgetItem*)")), VoGISProfilToolMain.lvRasterItemChanged)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VoGISProfilToolMain.reject)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VoGISProfilToolMain.accept)
        QtCore.QObject.connect(self.IDC_bSelectVisibleRasters, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolMain.selectVisibleRasters)
        QtCore.QObject.connect(self.IDC_bDrawLine, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolMain.drawLine)
        QtCore.QObject.connect(self.IDC_dblspinDistance, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), VoGISProfilToolMain.valueChangedEquiDistance)
        QtCore.QObject.connect(self.IDC_dblspinVertexCnt, QtCore.SIGNAL(_fromUtf8("valueChanged(double)")), VoGISProfilToolMain.valueChangedVertexCount)
        QtCore.QObject.connect(self.IDC_cbLineLayers, QtCore.SIGNAL(_fromUtf8("currentIndexChanged(int)")), VoGISProfilToolMain.lineLayerChanged)
        QtCore.QObject.connect(self.IDC_bRefreshRasterList, QtCore.SIGNAL(_fromUtf8("clicked()")), VoGISProfilToolMain.refreshRasterList)
        QtCore.QMetaObject.connectSlotsByName(VoGISProfilToolMain)

    def retranslateUi(self, VoGISProfilToolMain):
        VoGISProfilToolMain.setWindowTitle(QtGui.QApplication.translate("VoGISProfilToolMain", "VoGIS Profil Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_grpRaster.setTitle(QtGui.QApplication.translate("VoGISProfilToolMain", "Rastermodell(e) auswählen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bSelectVisibleRasters.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Im aktuellen Extent sichtbare Raster auswählen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bRefreshRasterList.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Raster aktualisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_grpProfilLinien.setTitle(QtGui.QApplication.translate("VoGISProfilToolMain", "Lage der Profillinie(n) festlegen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_bDrawLine.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Profillinie (neu) digitalisieren", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkOnlySelectedFeatures.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "nur selektierte Elemente verwenden", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkLinesExplode.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Linien explodieren (Multipart Features)", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_rbShapeLine.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Profillinie(n) aus Linienthema übernehmen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_rbDigi.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Profillinie am Bildschirm zeichen", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("VoGISProfilToolMain", "Linie", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_tbToY.setText(QtGui.QApplication.translate("VoGISProfilToolMain", ".", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "von:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "nach:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Rechtswert", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Hochwert", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkLinesMerge.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Zusammenhängende Linien verbinden", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_rbStraigthLine.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "gerade Profillinie zwischen zwei Punkten", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_grpVertices.setTitle(QtGui.QApplication.translate("VoGISProfilToolMain", "Stützstellen festlegen", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_rbEquiDistance.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Abstand zwischen den Profilpunkten", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_rbVertexCount.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Anzahl Profilpunkte pro Profil", None, QtGui.QApplication.UnicodeUTF8))
        self.IDC_chkNodesAndVertices.setText(QtGui.QApplication.translate("VoGISProfilToolMain", "Profilpunkte erstellen an Knoten und Stützstellen", None, QtGui.QApplication.UnicodeUTF8))

