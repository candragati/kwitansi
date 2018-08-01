from PyQt4 import QtGui,QtCore
import lihatdata
import sys
import sqlite3

class LihatData(QtGui.QDialog,lihatdata.Ui_Dialog):
    def __init__(self,parent=None):
        QtGui.QDialog.__init__(self)
        self.koneksiDatabase()
        self.setupUi(self)
        self.aksi()
        self.noKwitansi=""
        self.isiDataTable()
    
    def aksi(self):
        self.tableWidget.cellDoubleClicked.connect(self.onListDblKlik)

    def onListDblKlik(self,event=None):
        row = self.tableWidget.currentRow()
        self.noKwitansi = self.tableWidget.item(row,1).text()
        self.getNoKwitansi()
        self.accept()
        
    
    def onClose(self,event=None):
        self.cur.close()
        self.db.close()
        sys.exit()

    def koneksiDatabase(self):
        self.db = sqlite3.connect("database.db")
        self.cur = self.db.cursor()

    def isiDataTable(self):
        sql = "SELECT * FROM kwitansi"
        bar,jum = self.eksekusi(sql)
        self.tableWidget.setRowCount(jum)

        for data in range(jum):
            teks = (
                bar[data][0],
                bar[data][1],
                bar[data][2],
                bar[data][3],
                bar[data][4],
                bar[data][5])
            for i in range(0,6):
                b=str(i)
                item = QtGui.QTableWidgetItem()
                item.setFlags(
                    QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
                exec "item.setToolTip(teks["+b+"])"
                exec "item.setText(teks[" + b + "])"
                exec "self.tableWidget.setItem(data," + b + ",item)"
            
    def getNoKwitansi(self,event=None):
        return self.noKwitansi

    def eksekusi(self, sql):
        self.cur.execute(sql)
        lineData = self.cur.fetchall()
        totData = len(lineData)
        return lineData, totData   

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    form = LihatData()
    form.show()
    form.exec_()
