import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from CanvasDessin import CanvasDessin

""" Exercice 2 : Zone de dessin"""

"""1e Etape: Créer un nouveau projet affichant une zone de dessin"""

class Dessin(QMainWindow):
	action = None
	def __init__(self):
		super().__init__()
		self.canvas = CanvasDessin()
		self.setCentralWidget(self.canvas)

		self.createToolBar()


	def createToolBar(self):
		toolBar = QToolBar()

		self.action = QAction(self)
		self.updateColor()
		self.action.triggered.connect(self.chooseColor)

		slider = QSlider()
		slider.setOrientation(Qt.Horizontal)
		slider.setMinimum(1)
		slider.setMaximum(20)
		slider.valueChanged.connect(self.setWidth)

		button = QPushButton('Clear')
		button.clicked.connect(self.clearCanvas)

		toolBar.addAction(self.action)
		toolBar.addWidget(slider)
		toolBar.addWidget(button)

		self.addToolBarBreak(Qt.TopToolBarArea)
		self.addToolBar(toolBar)



	def updateColor(self):
		pixmap = QPixmap(20, 20)
		pixmap.fill(self.canvas.pen_color)
		icon = QIcon(pixmap)
		self.action.setIcon(icon)

	def chooseColor(self):
		color = QColorDialog.getColor(self.canvas.pen_color)
		if color.isValid():
			self.canvas.set_pen_color(color)
			self.updateColor()
			
			
	def setWidth(self, width):
		self.canvas.set_pen_width(width)
		
	def clearCanvas(self):
		self.canvas.traces = []
		self.canvas.update()


	def mousePressEvent(self, event):
		self.canvas.press(event)
		
	def mouseMoveEvent(self, event):
		self.canvas.drag(event)
		
	def mouseReleaseEvent(self, event):
		self.canvas.release(event)


	


def main(args):
	print(args)
	app = QApplication(args)
	dessin= Dessin()
	dessin.show()
	
	app.exec_()
	return



if __name__ == '__main__':
  main(sys.argv)

