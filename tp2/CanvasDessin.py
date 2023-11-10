import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Trace import Trace


class CanvasDessin(QWidget):

	def __init__(self):
		super().__init__()
		self.widget = QWidget(None).setMinimumSize(150,200)
		self.list = [Trace]



	def paintEvent(self, event):

		painter = QPainterPath()
		for i in list :
			painter.setBrush(Qt.red)







"""3e Etape: dessiner un tracé interactivement"""


"""4e Etape: spécifier des attributs graphiques"""


"""5e Etape: choisir interactivement les attributs graphiques"""


"""6e Etape: mettre à jour l'affichage du bouton qui permet de choisir la couleur"""

