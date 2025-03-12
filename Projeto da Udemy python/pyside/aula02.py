import sys
from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout

app = QApplication(sys.argv)

botao = QPushButton("texto do botão")
botao.setStyleSheet('font-size: 80px')


botao2 = QPushButton('Botão')
botao.setStyleSheet('font-size: 80px')

central_Widget= QWidget()

layout = QVBoxLayout()
central_Widget.setLayout(layout) 

layout.addWidget(botao)
layout.addWidget(botao2)

central_Widget.show()
app.exec()
