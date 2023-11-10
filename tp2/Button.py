import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ButtonModel import ButtonModel

"""Exercice 1 : dessiner un bouton"""

""" 1e Etape: Démarrage """


""" 2e Etape: Classe CanvasButton """

class CanvasButton(QWidget):

	defaultCol = QColor(Qt.lightGray)

	hoverCol = QColor(Qt.cyan)
	pressCol = QColor(Qt.blue)


	def __init__(self):
		super().__init__()
		self.bbox = QRect(200,100,200,100)
		self.buttonModel = ButtonModel()
		self.sara = CanvasButton.defaultCol
		self.setMouseTracking(True)


	def paintEvent(self, event):
		painter = QPainter(self)
		painter.setBrush(self.sara)
		painter.drawEllipse(self.bbox)


	def cursorOnEllipse(self, point):
		return self.bbox.contains(point)
		
	
	def mouseMoveEvent(self, event):
		if self.cursorOnEllipse(event.pos()):
			self.buttonModel.enter()
			self.sara = self.hoverCol
			if self.buttonModel.state == ButtonModel.pressIn :
				self.sara = self.pressCol

		else :
			self.buttonModel.leave()
			self.sara = self.defaultCol

		self.update()
		



	def mousePressEvent(self, event) :
		if self.cursorOnEllipse(event.pos()):
			self.buttonModel.press()
			self.sara = self.pressCol

		self.update()
		



	
	def mouseReleaseEvent(self, event):
		if self.cursorOnEllipse(event.pos()):
			if self.buttonModel.state == ButtonModel.pressIn  :
				self.buttonModel.action()
			self.buttonModel.release()
			self.sara = self.hoverCol
		if not self.cursorOnEllipse(event.pos()):
			if self.buttonModel.state == ButtonModel.pressIn  :
				self.buttonModel.action()
			self.buttonModel.release()
			self.sara = self.defaultCol

			
		self.update()







""" 4e Etape: synchroniser ButtonModel et CanvasButton """



def main(args):
	print(args)
	app = QApplication(args)
	window= QMainWindow()

	canvas=CanvasButton()

	window.setCentralWidget(canvas)
	
	window.resize(500,500)
	window.show()
	app.exec_()
	return




if __name__ == '__main__':
  main(sys.argv)

