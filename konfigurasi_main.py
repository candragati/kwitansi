from PyQt4 import QtGui
import konfigurasi
import sys
import os
import MSWinPrint

filekonfig = "config.ini"
teks="""printer = 
ukuran = 
orientasi = 
cetak langsung = 

nama Toko = definit():
Alamat = PERUM CAHAYA PERMAI BLOK B1 NO 2
No. Telp = 0819 0664 1219
"""
class Konfigurasi(QtGui.QDialog,konfigurasi.Ui_Dialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self)
        self.setupUi(self)
        self.cek()
        self.aturKomponen()
        self.aksi()

    def aturKomponen(self):
        konfigprint = open(filekonfig)
        lines=konfigprint.readlines()
        printer = lines[0].replace('printer = ','').strip()
        ukuran = lines[1].replace('ukuran = ','').strip()
        orientasi = lines[2].replace('orientasi = ','').strip()
        cetaklangsung = lines[3].replace('cetak langsung = ','').strip()
        namatoko = lines[5].replace('nama Toko = ','').strip()
        alamat = lines[6].replace('Alamat = ','').strip()
        telp = lines[7].replace('No. Telp = ','').strip()
        if orientasi =="portrait":
            self.rbPortrait.setChecked(True)
            self.rbLandscape.setChecked(False)
        else:
            self.rbPortrait.setChecked(False)
            self.rbLandscape.setChecked(True)

        if ukuran =="40M":
            self.rb40M.setChecked(True)
            self.rb40T.setChecked(False)
        else:
            self.rb40M.setChecked(False)
            self.rb40T.setChecked(True)

        if cetaklangsung=="Ya":
            self.rbYa.setChecked(True)
            self.rbTidak.setChecked(False)
        else:
            self.rbYa.setChecked(False)
            self.rbTidak.setChecked(True)

        self.lineEditNama.setText(namatoko)
        self.lineEditAlamat.setText(alamat)
        self.lineEditTelp.setText(telp)

        a = MSWinPrint.listprinters()
        self.comboBox.addItems(a)
        try:
            self.comboBox.setCurrentIndex(a.index(printer))
        except Exception,e:
            print e
            self.comboBox.clear()
            self.comboBox.addItems(a)
        
        

    def aksi(self):
        self.btnSimpan.pressed.connect(self.onSimpanKlik)

    def onSimpanKlik(self):
        lp = self.comboBox.currentText()
        namatoko = self.lineEditNama.text()
        alamat = self.lineEditAlamat.text()
        telp = self.lineEditTelp.text()

        if self.rbLandscape.isChecked():
            orientasi = "landscape"
        else:
            orientasi = "portrait"

        if self.rbYa.isChecked():
            cetaklangsung = "Ya"
        else:
            cetaklangsung = "Tidak"

        if self.rb40M.isChecked():
            ukuran = "40M"
        else:
            ukuran = "40T"

        if lp =="":
            QtGui.QMessageBox.warning(self,"Perhatian","Tidak ada printer yang dipilih")
        
        teks="""printer = %s
ukuran = %s
orientasi = %s
cetak langsung = %s

nama Toko = %s
Alamat = %s
No. Telp = %s
"""%(lp,ukuran,orientasi,cetaklangsung,namatoko,alamat,telp)
        try:
            fo = open(filekonfig,"wb")
            fo.write(teks)
            fo.close()
            QtGui.QMessageBox.information(self,"Sukses","Konfigurasi berhasil disimpan!")
            self.close()
        except Exception,e:
            QtGui.QMessageBox.critical(self,"Error","Tidak dapat menyimpan konfigurasi\n"+str(e))
            self.close()
            
    def cek(self):
        if os.path.exists(filekonfig):
            pass
        else:
            print "membuat konfigurasi..."
            try:
                fo = open(filekonfig,'wb')
                fo.write(teks)
                fo.close()
                print "konfigurasi dibuat otomatis!"
            except Exception,e:
                QtGui.QMessageBox.critical(self,"Perhatian!","Gagal membuat file konfig\n"+str(e))


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = Konfigurasi()
    form.show()
    form.exec_()