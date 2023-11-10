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


def main(args):
	print(args)

	app = QApplication(args)
	dessin= Dessin()

	dessin.show()
	app.exec_()
	return



if __name__ == '__main__':
  main(sys.argv)

