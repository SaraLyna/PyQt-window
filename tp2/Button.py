import sys

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from ButtonModel import ButtonModel

"""Exercice 1 : dessiner un bouton"""

""" 1e Etape: Démarrage """


""" 2e Etape: Classe CanvasButton """

class CanvasButton(QWidget):

	defaultCol = QColor(253,108,158)

	hoverCol = QColor(0,255,120)
	pressCol = QColor(0,255,255)

	def __init__(self,model):
		super().__init__()
		self.bbox = QRect(50,50,50,50)
		self.cursorOver = False
		self.buttonModel = model


	def paintEvent(self, event):

		painter = QPainter(self)

		if self.buttonModel.state ==  ButtonModel.idle :
			painter.setBrush(CanvasButton.defaultCol)

		if self.buttonModel.state ==  ButtonModel.hover :
			painter.setBrush(CanvasButton.hoverCol)

		if self.buttonModel.state ==  ButtonModel.pressIn :
			painter.setBrush(CanvasButton.pressCol)

		if self.buttonModel.state ==  ButtonModel.pressOut :
			painter.setBrush(CanvasButton.hoverCol)

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

		self.update()
		print("pressed")



	
	def mouseReleaseEvent(self, eventpressOut):
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

	model= ButtonModel()
	canvas=CanvasButton(model)

	window.setCentralWidget(canvas)
	
	window.resize(500,500)
	window.show()
	app.exec_()
	return




if __name__ == '__main__':
  main(sys.argv)

