# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kwitansi.ui'
#
# Created: Sun May 08 12:39:58 2016
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(359, 281)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEditNo = QtGui.QLineEdit(self.centralwidget)
        self.lineEditNo.setObjectName(_fromUtf8("lineEditNo"))
        self.horizontalLayout_2.addWidget(self.lineEditNo)
        spacerItem = QtGui.QSpacerItem(73, 20, QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.dateEdit = QtGui.QDateEdit(self.centralwidget)
        self.dateEdit.setButtonSymbols(QtGui.QAbstractSpinBox.PlusMinus)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName(_fromUtf8("dateEdit"))
        self.horizontalLayout_2.addWidget(self.dateEdit)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.verticalLayout.addWidget(self.label_6)
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.verticalLayout.addWidget(self.label_5)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.lineEditDari = QtGui.QLineEdit(self.centralwidget)
        self.lineEditDari.setObjectName(_fromUtf8("lineEditDari"))
        self.verticalLayout_2.addWidget(self.lineEditDari)
        self.lineEditOleh = QtGui.QLineEdit(self.centralwidget)
        self.lineEditOleh.setObjectName(_fromUtf8("lineEditOleh"))
        self.verticalLayout_2.addWidget(self.lineEditOleh)
        self.lineEditSebesar = QtGui.QLineEdit(self.centralwidget)
        self.lineEditSebesar.setInputMethodHints(QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhPreferNumbers)
        self.lineEditSebesar.setObjectName(_fromUtf8("lineEditSebesar"))
        self.verticalLayout_2.addWidget(self.lineEditSebesar)
        self.lineEditPembayaran = QtGui.QLineEdit(self.centralwidget)
        self.lineEditPembayaran.setObjectName(_fromUtf8("lineEditPembayaran"))
        self.verticalLayout_2.addWidget(self.lineEditPembayaran)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.btnSimpan = QtGui.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSimpan.setIcon(icon)
        self.btnSimpan.setIconSize(QtCore.QSize(32, 32))
        self.btnSimpan.setObjectName(_fromUtf8("btnSimpan"))
        self.horizontalLayout_3.addWidget(self.btnSimpan)
        self.btnCetak = QtGui.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/printer.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnCetak.setIcon(icon1)
        self.btnCetak.setIconSize(QtCore.QSize(32, 32))
        self.btnCetak.setObjectName(_fromUtf8("btnCetak"))
        self.horizontalLayout_3.addWidget(self.btnCetak)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setIconSize(QtCore.QSize(32, 32))
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionExit = QtGui.QAction(MainWindow)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/door_out.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon2)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.actionLihat_Data = QtGui.QAction(MainWindow)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/application_form_magnify.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLihat_Data.setIcon(icon3)
        self.actionLihat_Data.setObjectName(_fromUtf8("actionLihat_Data"))
        self.actionEdit = QtGui.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/pencil.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionEdit.setIcon(icon4)
        self.actionEdit.setObjectName(_fromUtf8("actionEdit"))
        self.actionCancel = QtGui.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionCancel.setIcon(icon5)
        self.actionCancel.setObjectName(_fromUtf8("actionCancel"))
        self.actionDelete = QtGui.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/delete.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionDelete.setIcon(icon6)
        self.actionDelete.setObjectName(_fromUtf8("actionDelete"))
        self.actionAdd = QtGui.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAdd.setIcon(icon7)
        self.actionAdd.setObjectName(_fromUtf8("actionAdd"))
        self.actionSetting = QtGui.QAction(MainWindow)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/toolbox.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSetting.setIcon(icon8)
        self.actionSetting.setObjectName(_fromUtf8("actionSetting"))
        self.toolBar.addAction(self.actionAdd)
        self.toolBar.addAction(self.actionEdit)
        self.toolBar.addAction(self.actionDelete)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLihat_Data)
        self.toolBar.addAction(self.actionCancel)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSetting)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.actionExit, QtCore.SIGNAL(_fromUtf8("triggered()")), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Kwitansi", None))
        self.label.setText(_translate("MainWindow", "No", None))
        self.label_2.setText(_translate("MainWindow", "Terima Dari", None))
        self.label_6.setText(_translate("MainWindow", "Diterima Oleh", None))
        self.label_4.setText(_translate("MainWindow", "Sebesar", None))
        self.label_5.setText(_translate("MainWindow", "Pembayaran", None))
        self.btnSimpan.setText(_translate("MainWindow", "Save", None))
        self.btnCetak.setText(_translate("MainWindow", "Cetak", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionExit.setText(_translate("MainWindow", "Exit", None))
        self.actionExit.setToolTip(_translate("MainWindow", "Keluar", None))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q", None))
        self.actionLihat_Data.setText(_translate("MainWindow", "Lihat Data", None))
        self.actionLihat_Data.setShortcut(_translate("MainWindow", "F3", None))
        self.actionEdit.setText(_translate("MainWindow", "Edit", None))
        self.actionEdit.setShortcut(_translate("MainWindow", "F2", None))
        self.actionCancel.setText(_translate("MainWindow", "Cancel", None))
        self.actionCancel.setShortcut(_translate("MainWindow", "Esc", None))
        self.actionDelete.setText(_translate("MainWindow", "Delete", None))
        self.actionDelete.setShortcut(_translate("MainWindow", "Del", None))
        self.actionAdd.setText(_translate("MainWindow", "Add", None))
        self.actionAdd.setToolTip(_translate("MainWindow", "Tambah", None))
        self.actionAdd.setShortcut(_translate("MainWindow", "Ctrl+N", None))
        self.actionSetting.setText(_translate("MainWindow", "Setting", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

