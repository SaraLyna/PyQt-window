import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Trace import Trace


class CanvasDessin(QWidget):

	def __init__(self):
		super().__init__()
		self.setMinimumSize(800,600)
		self.traces = []



	def paintEvent(self, event):
		
		painter = QPainter(self)
		path = QPainterPath()
		for trace in self.traces :
			path.setBrush(Qt.red)

		painter.drawPath(path)


	def press(self, event):


		self.update()


	def drag(self, event):


		self.update()


	def release(self, event):


		self.update()







"""3e Etape: dessiner un tracé interactivement"""


"""4e Etape: spécifier des attributs graphiques"""


"""5e Etape: choisir interactivement les attributs graphiques"""


"""6e Etape: mettre à jour l'affichage du bouton qui permet de choisir la couleur"""

