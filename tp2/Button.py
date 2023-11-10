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
		self.cursorOver = True
		self.buttonModel = ButtonModel()


	def paintEvent(self, event):

		painter = QPainter(self)

		if self.cursorOver :
			if self.buttonModel.state ==  ButtonModel.hover :
				painter.setBrush(CanvasButton.hoverCol)
		
			if self.buttonModel.state ==  ButtonModel.pressIn :
				painter.setBrush(CanvasButton.pressCol)

			if self.buttonModel.state ==  ButtonModel.pressOut :
				painter.setBrush(CanvasButton.hoverCol)


		else:
			painter.setBrush(CanvasButton.defaultCol)
		painter.drawEllipse(self.bbox)


	def cursorOnEllipse(self, point):
		return self.bbox.contains(point)
		
	
	def mouseMoveEvent(self, event):
		if self.cursorOnEllipse(event.pos()):
			self.buttonModel.enter()

		else :
			self.buttonModel.leave()

		self.update()
		print("moved")



	def mousePressEvent(self, event):
		if self.cursorOnEllipse(event.pos()):
			self.buttonModel.press()
			self.cursorOver = not self.cursorOver
			print("pressed")

		self.update()
		



	
	def mouseReleaseEvent(self, event):
		if self.buttonModel.state == ButtonModel.pressIn :
			self.buttonModel.action()
		self.buttonModel.release()
			
		self.update()
		print("released")







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

