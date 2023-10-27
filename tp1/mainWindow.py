import sys
from PyQt5.QtWidgets import *


class MainWindow(QMainWindow):

	def __init__(self):
		super().__init__()


def main(args):
	print(args)
	app = QApplication(args)
	window= MainWindow()
	window.show()
	app.exec_()



if __name__ == "__main__":
	print("Exécution du programme")
	main(sys.argv)




	