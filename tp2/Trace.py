import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




"""2e Etape: créer une classe Trace"""

class Trace():

	def __init__(self, points, width, color):
		self.points = points
		self.width = width
		self.color = color
