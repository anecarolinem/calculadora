import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, \
    QGridLayout




class App(QMainWindow):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.cw= QWidget()
        self.grid = QGridLayout(self.cw)

        self.btn = QPushButton('Texto do botão')#criar botão
        self.grid.addWidget(self.btn, 0, 0, 1,1) #adicionar botão na tela

        #self.btn.clicked.connect(lambda: print('Olá mundo!'))//Ação de botão
        self.btn.clicked.connect(self.acao) # Ação

    def acao(self):
        print('Alguma coisa...')



        self.setCentralWidget(self.cw)

if __name__ =='__main__':
    qt = QApplication(sys.argv)
    app= App()
    app.show()
    qt.exec_()



