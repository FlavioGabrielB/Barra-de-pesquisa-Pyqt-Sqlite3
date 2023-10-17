import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QTableWidget, QPushButton
from buscador import *

class Gui(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gui = Ui_MainWindow()
        self.gui.setupUi(self)
        self.gui.pushButton.clicked.connect(self.buscar)
        
        #inseri dados como exemplo
        # self.nome = 'Teste'
        # self.s = f'''INSERT INTO dados(nome)
        #             VALUES('{self.nome}')'''
        # self.d = "CREATE TABLE IF NOT EXISTS dados (id integer not null primary key autoincrement, nome text)"
        # self.banco = sqlite3.connect('banco_buscar.db')
        # self.csr = self.banco.cursor()
        # self.csr.execute(self.d)
        # self.csr.execute(self.s)
        # self.banco.commit()
        # self.banco.close()

        # Atualiza os dados na tela
        self.atualizar()
        
    def atualizar(self):
        self.banco = sqlite3.connect('banco_buscar.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute('SELECT id, nome FROM dados')
        self.dados_lidos = self.csr.fetchall()
        self.gui.tableWidget.setRowCount(len(self.dados_lidos))
        self.gui.tableWidget.setColumnCount(2)
        print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,2):
                self.gui.tableWidget.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))             
        self.banco.close()

    def buscar(self): #ao apertar buscar os dados são atualizados
        self.texto = self.gui.lineEdit.text()
        print(self.texto)
        self.banco = sqlite3.connect('banco_buscar.db', timeout=1)
        self.csr = self.banco.cursor()
        self.csr.execute(f'SELECT id, nome FROM dados WHERE nome LIKE "%{self.texto}%" OR id LIKE "%{self.texto}%" ')
        self.dados_lidos = self.csr.fetchall()
        self.gui.tableWidget.setRowCount(len(self.dados_lidos))
        self.gui.tableWidget.setColumnCount(2)
        print(self.dados_lidos)
        for self.i in range(0, len(self.dados_lidos)):
            for self.j in range(0,2):
                self.gui.tableWidget.setItem(self.i,self.j,QTableWidgetItem(str(self.dados_lidos[self.i][self.j])))             
        self.banco.close()

if __name__ == '__main__':
    qt = QApplication(sys.argv)
    view = Gui()
    view.show()
    qt.exec()
