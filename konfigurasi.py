# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'konfigurasi.ui'
#
# Created: Sun May 08 20:26:48 2016
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(330, 245)
        self.gridLayout = QtGui.QGridLayout(Dialog)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.comboBox = QtGui.QComboBox(Dialog)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 3)
        self.groupBox = QtGui.QGroupBox(Dialog)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rb40T = QtGui.QRadioButton(self.groupBox)
        self.rb40T.setGeometry(QtCore.QRect(11, 24, 44, 17))
        self.rb40T.setCheckable(True)
        self.rb40T.setChecked(True)
        self.rb40T.setObjectName(_fromUtf8("rb40T"))
        self.rb40M = QtGui.QRadioButton(self.groupBox)
        self.rb40M.setGeometry(QtCore.QRect(11, 47, 46, 17))
        self.rb40M.setCheckable(True)
        self.rb40M.setChecked(False)
        self.rb40M.setObjectName(_fromUtf8("rb40M"))
        self.gridLayout.addWidget(self.groupBox, 1, 0, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(Dialog)
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.rbLandscape = QtGui.QRadioButton(self.groupBox_2)
        self.rbLandscape.setGeometry(QtCore.QRect(11, 47, 74, 17))
        self.rbLandscape.setChecked(False)
        self.rbLandscape.setObjectName(_fromUtf8("rbLandscape"))
        self.rbPortrait = QtGui.QRadioButton(self.groupBox_2)
        self.rbPortrait.setGeometry(QtCore.QRect(11, 24, 59, 17))
        self.rbPortrait.setChecked(True)
        self.rbPortrait.setObjectName(_fromUtf8("rbPortrait"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 1, 1, 1)
        self.groupBox_3 = QtGui.QGroupBox(Dialog)
        self.groupBox_3.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.rbTidak = QtGui.QRadioButton(self.groupBox_3)
        self.rbTidak.setGeometry(QtCore.QRect(11, 47, 48, 17))
        self.rbTidak.setObjectName(_fromUtf8("rbTidak"))
        self.rbYa = QtGui.QRadioButton(self.groupBox_3)
        self.rbYa.setGeometry(QtCore.QRect(11, 24, 34, 17))
        self.rbYa.setChecked(True)
        self.rbYa.setObjectName(_fromUtf8("rbYa"))
        self.gridLayout.addWidget(self.groupBox_3, 1, 2, 1, 1)
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.lineEditNama = QtGui.QLineEdit(Dialog)
        self.lineEditNama.setObjectName(_fromUtf8("lineEditNama"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineEditNama)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEditAlamat = QtGui.QLineEdit(Dialog)
        self.lineEditAlamat.setObjectName(_fromUtf8("lineEditAlamat"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.lineEditAlamat)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEditTelp = QtGui.QLineEdit(Dialog)
        self.lineEditTelp.setObjectName(_fromUtf8("lineEditTelp"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.lineEditTelp)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 3)
        self.btnSimpan = QtGui.QPushButton(Dialog)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icon/DESIGN/icon/32x32/disk.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btnSimpan.setIcon(icon)
        self.btnSimpan.setIconSize(QtCore.QSize(32, 32))
        self.btnSimpan.setObjectName(_fromUtf8("btnSimpan"))
        self.gridLayout.addWidget(self.btnSimpan, 3, 1, 1, 1)

        self.retranslateUi(Dialog)
        self.comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Konfigurasi", None))
        self.groupBox.setTitle(_translate("Dialog", "Ukuran Kwitansi", None))
        self.rb40T.setText(_translate("Dialog", "40 T", None))
        self.rb40M.setText(_translate("Dialog", "40 M", None))
        self.groupBox_2.setTitle(_translate("Dialog", "Orientation", None))
        self.rbLandscape.setText(_translate("Dialog", "Landscape", None))
        self.rbPortrait.setText(_translate("Dialog", "Portrait", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Langsung Cetak ?", None))
        self.rbTidak.setText(_translate("Dialog", "Tidak", None))
        self.rbYa.setText(_translate("Dialog", "Ya", None))
        self.label.setText(_translate("Dialog", "Nama Toko", None))
        self.label_2.setText(_translate("Dialog", "Alamat", None))
        self.label_3.setText(_translate("Dialog", "No. Telp", None))
        self.btnSimpan.setText(_translate("Dialog", "SIMPAN", None))

import icon_rc

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Dialog = QtGui.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

