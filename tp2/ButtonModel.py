import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *




""" 3e Etape: Classe ButtonModel"""

class ButtonModel():

	idle = 0
	hover = 1
	pressIn = 2
	pressOut = 3

	def __init__(self):
		self.state = ButtonModel.idle
		
		
	def enter(self):
		if self.state == ButtonModel.idle :
			self.state = ButtonModel.hover 
		elif self.state == ButtonModel.pressOut :
			self.state = ButtonModel.pressIn
	
	def leave(self):
		if self.state == ButtonModel.hover : 
			self.state = ButtonModel.idle 
		elif self.state == ButtonModel.pressIn :
			self.state = ButtonModel.pressOut
	
	def press(self):
		if self.state == ButtonModel.hover:
			self.state = ButtonModel.pressIn
	
	
	def release(self):
		if self.state == ButtonModel.pressOut :
			self.state = ButtonModel.idle 
		elif self.state == ButtonModel.pressIn :
			self.state = ButtonModel.action(self)
	
	
	
	def action(self):
		print("action")
		return self.hover
	
	
	
