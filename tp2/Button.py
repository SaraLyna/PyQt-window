import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

"""Exercice 1 : dessiner un bouton"""

""" 1e Etape: Démarrage """

def main(args):
	print(args)
	app = QApplication(args)
	window= QMainWindow()
	canvas=CanvasButton()
	canvas.setCentralWidget(window)
	window.resize(500,500)
	window.show()
	app.exec_()
	return



""" 2e Etape: Classe CanvasButton """

class CanvasButton(QWidget):

	def __init__(self, bbox):
		CanvasButton.__init__(self)
		self.bbox = bbox
		
	def mouseMoveEvent(self, event):
	
	def mousePressEvent(self, event):
	
	def mouseReleaseEvent(self, event):
	
	def paintEvent(self, event):
		painter = QPainter(self)
		pen = QPen(Qt.red)
		pen.setWidth(5)
		painter.setPen(pen)
		painter.setBrush(Qt.lightGray)
		painter.drawRect(5,5,120,40)
		painter.setBrush(QColor(120, 255, 255, 150))
		painter.drawEllipse(0,0,100,130)


	def cursorOnEllipse(self, point):
	






""" 4e Etape: synchroniser ButtonModel et CanvasButton """






if __name__ == '__main__':
  main(sys.argv)

