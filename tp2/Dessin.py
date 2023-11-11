import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from CanvasDessin import CanvasDessin

""" Exercice 2 : Zone de dessin"""

"""1e Etape: Créer un nouveau projet affichant une zone de dessin"""

class Dessin(QMainWindow):

	def __init__(self):
		super().__init__()
		self.canvas = CanvasDessin()
		self.setCentralWidget(self.canvas)

		self.createToolBar()


	def createToolBar(self):
		toolBar = QToolBar()

		action = QAction('Color', self)
		action.triggered.connect(self.chooseColor)

		slider = QSlider()
		slider.setOrientation(Qt.Horizontal)
		slider.setMinimum(1)
		slider.setMaximum(20)
		slider.valueChanged.connect(self.setWidth)

		button = QPushButton('Clear')
		button.clicked.connect(self.clearCanvas)

		toolBar.addAction(action)
		toolBar.addWidget(slider)
		toolBar.addWidget(button)

		self.addToolBar(toolBar)


	def chooseColor(self):
		color = QColorDialog.getColor()
		if color.isValid():
			self.canvas.set_pen_color(color)
			
	def setWidth(self, width):
		self.canvas.set_pen_width(width)
		
	def clearCanvas(self):
		self.canvas.traces = []
		self.canvas.update()


def main(args):
	print(args)
 
    """window = QMainWindow()"""

	app = QApplication(args)
	dessin= Dessin()

	dessin.show()

	"""window.show()"""
	
	app.exec_()
	return



if __name__ == '__main__':
  main(sys.argv)

