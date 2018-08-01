from PyQt4 import QtGui,QtCore
import sys
import kwitansi
import lihatdata_main
import konfigurasi_main
import buat_db
import sqlite3
import string
import MSWinPrint
import textwrap

mm=100
filekonfig = "config.ini"
        

class menuKwitansi(QtGui.QMainWindow,kwitansi.Ui_MainWindow):
    def __init__(self,parent = None):
        QtGui.QMainWindow.__init__(self)
        buat_db.Database()
        self.jum = 0
        self.koneksiDatabase()
        self.setupUi(self)
        self.aksi()
        self.dateEdit.setDate(QtCore.QDate.currentDate())
        self.normal()

    def normal(self):
        self.bersih() 
        self.lineEditNo.setEnabled(False)
        self.lineEditDari.setEnabled(False)
        self.lineEditOleh.setEnabled(False)
        self.lineEditSebesar.setEnabled(False)
        self.lineEditPembayaran.setEnabled(False)
        self.dateEdit.setEnabled(False)
        self.actionEdit.setEnabled(False)
        self.actionDelete.setEnabled(False)
        self.actionCancel.setEnabled(False)
        self.actionAdd.setEnabled(True)
        self.btnCetak.setEnabled(False)
        self.btnSimpan.setEnabled(False)

    def bersih(self):
        self.lineEditNo.clear()
        self.lineEditDari.clear()
        self.lineEditOleh.clear()
        self.lineEditPembayaran.clear()
        self.lineEditSebesar.clear()

    def tambah(self):
        self.bersih()
        bar,jum = self.eksekusi("SELECT * FROM kwitansi")
        if jum==0:
            teks = "000001"            
        else:
            kd = bar[jum-1][1]
            kode_nota = int(kd[-6:])+1            
            if kode_nota <10:
                teks = "00000"+str(kode_nota)
            elif kode_nota < 100:
                teks = "0000" + str(kode_nota)
            elif kode_nota < 1000:
                teks = "000" + str(kode_nota)          
            elif kode_nota < 10000:
                teks = "00" + str(kode_nota)           
            elif kode_nota < 100000:
                teks = "0" + str(kode_nota)
            elif kode_nota < 1000000:
                teks = "" + str(kode_nota)
            else:
                QtGui.QMessageBox.critical(self,"Perhatian!","Data sudah mencapai batas limit!")          
        
        self.dateEdit.setEnabled(True)
        self.lineEditNo.setText(teks)
        self.lineEditNo.setEnabled(True)
        self.lineEditNo.setFocus()
        self.actionAdd.setEnabled(False)
        self.actionCancel.setEnabled(True)

    def aksi(self):
        self.actionCancel.triggered.connect(self.normal)
        self.actionAdd.triggered.connect(self.tambah)
        self.lineEditNo.returnPressed.connect(self.onNoEnter)
        self.lineEditDari.returnPressed.connect(self.onDariEnter)
        self.lineEditOleh.returnPressed.connect(self.onOlehEnter)
        self.lineEditSebesar.returnPressed.connect(self.onSebesarEnter)
        self.lineEditPembayaran.returnPressed.connect(self.onPembayaranEnter)
        self.actionLihat_Data.triggered.connect(self.lihatdata)
        self.actionEdit.triggered.connect(self.onEditKlik)
        self.actionDelete.triggered.connect(self.onDeleteKlik)
        self.actionSetting.triggered.connect(self.onSettingKlik)
        self.btnSimpan.clicked.connect(self.onSimpanKlik)
        self.btnCetak.clicked.connect(self.onCetakKlik)

    def onSimpanKlik(self):
        konfigprint = open(filekonfig)
        lines=konfigprint.readlines()
        cetaklangsung = lines[3].replace('cetak langsung = ','').strip()
        
        no = self.lineEditNo.text()
        dari = self.lineEditDari.text()
        oleh  = self.lineEditOleh.text()
        sebesar = self.lineEditSebesar.text()
        pembayaran = self.lineEditPembayaran.text()
        tanggal = self.dateEdit.text()
        sql = "SELECT * FROM kwitansi WHERE UPPER(no)=UPPER('%s')"%no
        bar,jum = self.eksekusi(sql)
        if jum ==0:
            sql = "INSERT INTO kwitansi VALUES ('%s','%s','%s','%s','%s','%s')"%(tanggal,no,dari,oleh,sebesar,pembayaran)        
            text_sukses = "Data berhasil disimpan!"
            text_gagal = "Tidak dapat menyimpan!\n"
        else:
            sql = """
            UPDATE kwitansi 
            SET 
                dari='%s', 
                oleh='%s',
                sebesar='%s',
                pembayaran='%s' 
            WHERE no='%s' 
            """%(dari,oleh,sebesar,pembayaran,no)
            text_sukses = "Data berhasil dirubah!"
            text_gagal = "Tidak dapat merubah!\n"
        try:
            self.cur.execute(sql)
            self.db.commit()
            QtGui.QMessageBox.information(self,"Sukses!",text_sukses)
            if cetaklangsung=="Ya" :
                self.onCetakKlik()
            self.normal()
            self.tambah()
        except Exception,e:
            print e
            QtGui.QMessageBox.critical(self,"Gagal!",text_gagal+str(e))
        konfigprint.close()
        

    def onCetakKlik(self):
        import win32con
        konfigprint = open(filekonfig)
        lines=konfigprint.readlines()
        printer = lines[0].replace('printer = ','').strip()
        # ukuran = lines[1].replace('ukuran = ','').strip()
        orientasi = lines[2].replace('orientasi = ','').strip()
        # namatoko = lines[5].replace('nama Toko = ','').strip()
        # alamat = lines[6].replace('Alamat = ','').strip()
        # telp = lines[7].replace('No. Telp = ','').strip()
        
        
        no = str(self.lineEditNo.text())
        dari = str(self.lineEditDari.text()).upper()
        # oleh  = self.lineEditOleh.text()
        sebesar = self.lineEditSebesar.text()
        pembayaran = textwrap.fill(str(self.lineEditPembayaran.text()).upper(),width=40)
        tanggal = str(self.dateEdit.text())
        terbilang = textwrap.fill(str(self.Terbilang(int(sebesar)))+" Rupiah",width=40)
        rupiah = format(int(sebesar),',d')

        doc = MSWinPrint.document(papersize="a4",printer=printer,orientation=orientasi)
        doc.begin_document()
        doc.setfont("Lucida Console", 18,bold=0)
        doc.gambartext(no,(mm*44,mm*-146,mm*70,mm*-70),win32con.DT_LEFT)
        doc.gambartext(dari,(mm*68,mm*-153,mm*160,mm*-70),win32con.DT_LEFT)
        doc.gambartext(terbilang,(mm*68,mm*-159,mm*160,mm*-70),win32con.DT_LEFT)
        doc.gambartext(pembayaran,(mm*68,mm*-171,mm*160,mm*-70),win32con.DT_LEFT)
        doc.gambartext(rupiah,(mm*45,mm*-193,mm*160,mm*-70),win32con.DT_LEFT)
        doc.gambartext(tanggal,(mm*110,mm*-181,mm*160,mm*-70),win32con.DT_LEFT)
        doc.end_document()
        konfigprint.close()
                

    def lihatdata(self):
        app = lihatdata_main.LihatData()        
        app.exec_()
        no = app.getNoKwitansi()      
        if no!="":
            sql = "SELECT * FROM kwitansi WHERE UPPER(no)=UPPER('%s')"%no
            bar,jum = self.eksekusi(sql)        
            self.bersih()
            self.lineEditNo.setText(bar[0][1])
            self.lineEditDari.setText(bar[0][2])
            self.lineEditOleh.setText(bar[0][3])
            self.lineEditSebesar.setText(bar[0][4])
            self.lineEditPembayaran.setText(bar[0][5])
            self.lineEditNo.setEnabled(False)
            self.actionCancel.setEnabled(True)
            self.actionDelete.setEnabled(True)
            self.actionEdit.setEnabled(True)
            self.actionAdd.setEnabled(False)
            self.btnCetak.setEnabled(True)
            self.btnCetak.setFocus()

    def onNoEnter(self):
        no = self.lineEditNo.text()
        sql = """
        SELECT * FROM kwitansi WHERE UPPER (no)=UPPER('%s')
        """%no
        bar,jum = self.eksekusi (sql)
        self.jum = jum
        if jum==0:
            self.lineEditDari.setEnabled(True)
            self.lineEditDari.setFocus()
        else:
            tanggal=str(bar[0][0])
            dari = str(bar[0][2])
            oleh = str(bar[0][3])
            sebesar = str(bar[0][4])
            pembayaran = str(bar[0][5])

            hari,bulan,tahun=string.split(tanggal,'/')
            some_date = QtCore.QDate(int(tahun),int(bulan),int(hari)) #Year, Month, Day
            self.dateEdit.setDate(some_date)
            self.dateEdit.setEnabled(False)
            self.lineEditDari.setText(dari)
            self.lineEditOleh.setText(oleh)
            self.lineEditPembayaran.setText(pembayaran)
            self.lineEditSebesar.setText(sebesar)
            self.lineEditNo.setEnabled(False)
            self.actionEdit.setEnabled(True)
            self.actionDelete.setEnabled(True)
            self.btnCetak.setEnabled(True)
            self.btnCetak.setFocus()

    def onDariEnter(self):
        self.lineEditOleh.setEnabled(True)
        self.lineEditOleh.setFocus()

    def onOlehEnter(self):
        self.lineEditSebesar.setEnabled(True)
        self.lineEditSebesar.setFocus()

    def onSebesarEnter(self):
        self.lineEditPembayaran.setEnabled(True)
        self.lineEditPembayaran.setFocus()

    def onPembayaranEnter(self):
        self.btnSimpan.setEnabled(True)
        self.btnSimpan.setFocus()

    def koneksiDatabase(self):
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()

    def eksekusi(self, sql):
        self.cur.execute(sql)
        lineData = self.cur.fetchall()
        totData = len(lineData)     
        return lineData, totData

    def onEditKlik(self):
        self.lineEditDari.setEnabled(True)
        self.lineEditOleh.setEnabled(True)
        self.lineEditSebesar.setEnabled(True)
        self.lineEditPembayaran.setEnabled(True)
        self.lineEditDari.setFocus()
        self.btnCetak.setEnabled(False)
        self.btnSimpan.setEnabled(True)
    
    def onDeleteKlik(self):
        hapus=QtGui.QMessageBox.question(self,"Konfirmasi","Anda yakin akan menghapus data?",
            QtGui.QMessageBox.Yes|QtGui.QMessageBox.No)
        if hapus == QtGui.QMessageBox.Yes:            
            no = self.lineEditNo.text()
            sql = "DELETE FROM kwitansi where UPPER(no)='%s'"%no
            try:
                self.cur.execute(sql)
                self.db.commit()
                QtGui.QMessageBox.warning(self,"Perhatian","Data berhasil dihapus!")
            except Exception,e:
                QtGui.QMessageBox.critical(self,"Error","Gagal menhapus data!\n"+str(e))
        self.normal()

    def onSettingKlik(self):
        app = konfigurasi_main.Konfigurasi()        
        app.exec_()

    def Terbilang(self,n):
        satuan = ("", "Satu", "Dua", "Tiga", "Empat", "Lima", "Enam", "Tujuh", "Delapan", "Sembilan", "Sepuluh", "Sebelas")     
        
        if 0 <= n <= 11:
            return " " + satuan[n]
        elif 12 <= n <= 19:
            return self.Terbilang(n % 10) + " Belas"
        elif 20 <= n <= 99:
            return self.Terbilang(n / 10) + " Puluh" + self.Terbilang(n % 10)
        elif 100 <= n <= 199:
            return " Seratus" + self.Terbilang(n - 100)
        elif 200 <= n <= 999:
            return self.Terbilang(n / 100) + " Ratus" + self.Terbilang(n % 100)
        elif 1000 <= n <= 1999:
            return " Seribu" + self.Terbilang(n - 1000)
        elif 2000 <= n <= 999999:
            return self.Terbilang(n / 1000) + " Ribu" + self.Terbilang(n % 1000)
        elif 1000000 <= n <= 999999999:
            return self.Terbilang(n / 1000000) + " Juta" + self.Terbilang(n % 1000000)
        else:
            return self.Terbilang(n / 1000000000) + " Milyar" + self.Terbilang(n % 1000000000)
 
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    menu = menuKwitansi()
    menu.show()
    sys.exit(app.exec_())