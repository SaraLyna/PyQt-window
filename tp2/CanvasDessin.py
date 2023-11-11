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
		self.current_trace = None



	def paintEvent(self, event):
		
		painter = QPainter(self)

		for trace in self.traces :

			path = QPainterPath()
			pen = QPen(trace.color, trace.width,cap=Qt.RoundCap, join=Qt.RoundJoin )
			painter.setPen(pen)
			path.moveTo(trace.points[0])

			for point in trace.points[1:]:
				path.lineTo(point)

			painter.drawPath(path)

		if self.current_trace:

			path2 = QPainterPath()
            pen2 = QPen(self.current_trace.color, self.current_trace.width, cap=Qt.RoundCap, join=Qt.RoundJoin)
            painter.setPen(pen2)
            path2.moveTo(self.current_trace.points[0])

            for point in self.current_trace.points[1:]:
                path2.lineTo(point)

            painter.drawPath(path2)


	def press(self, event):
		self.current_trace = Trace([event.pos()], 3, Qt.red)
		self.update()


	def drag(self, event):
		if self.current_trace:
			self.current_trace.points.append(event.pos())
			self.update()


	def release(self, event):
		if self.current_trace:
			self.traces.append(self.current_trace)
			self.current_trace = None
			self.update()







"""3e Etape: dessiner un tracé interactivement"""


"""4e Etape: spécifier des attributs graphiques"""


"""5e Etape: choisir interactivement les attributs graphiques"""


"""6e Etape: mettre à jour l'affichage du bouton qui permet de choisir la couleur"""

