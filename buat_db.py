import sqlite3
import os,sys

db_kwitansi = "database.db"
class Database():
    def __init__(self):
        self.cek()

    def cek(self):
        statusDB = os.path.exists(db_kwitansi)
        if statusDB:
            print "file database sudah ada\nskipping..."
        else:
            print "membuat file database..."
            try:
                self.koneksiDatabase()
                self.createTable()
                print "database berhasil dibuat"
            except Exception,e:
                print e
                sys.exit()

    def koneksiDatabase(self):
        self.db = sqlite3.connect(db_kwitansi)
        self.cur = self.db.cursor()

    def createTable(self):
        self.buatTable()

    def buatTable(self):
        sqlPesan = """
       CREATE TABLE kwitansi ( 
            tanggal    DATE,
            [no]       TEXT PRIMARY KEY ,
            dari       TEXT,
            oleh       TEXT,
            sebesar    TEXT,
            pembayaran TEXT
            
        );
        """
        self.cur.execute(sqlPesan) 

if __name__ == '__main__':
    Database()
