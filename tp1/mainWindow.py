import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

class MainWindow(QMainWindow):

	def __init__(self):
		QMainWindow.__init__(self)
		bar=self.menuBar()
		fileMenu = bar.addMenu( "File" )
		

		zoneCentrale =QTextEdit(self)
		self.setCentralWidget(zoneCentrale)


		status=self.statusBar()
	

		newAct1 = QAction(QIcon("open.png"), "Open…", self )
		newAct1.setShortcut( "Ctrl+N" )
		newAct1.setToolTip(str("Open File"))
		newAct1.setStatusTip(str("Open File"))
		fileMenu.addAction(newAct1)
		


		newAct2 = QAction(QIcon("save.png"), "Save…", self )
		newAct2.setShortcut( "Ctrl+S" )
		newAct2.setToolTip(str("Save File"))
		newAct2.setStatusTip(str("Save File"))
		fileMenu.addAction(newAct2)
		
		newAct3 = QAction(QIcon("copy.png"), "Copy…", self )
		newAct3.setShortcut( "Ctrl+C" )
		newAct3.setToolTip(str("Copy File"))
		newAct3.setStatusTip(str("Copy File"))
		fileMenu.addAction(newAct3)
		

		newAct4 = QAction(QIcon("quit.png"), "Quit…", self )
		newAct4.setShortcut( "Ctrl+Q" )
		newAct4.setToolTip(str("Quit File"))
		newAct4.setStatusTip(str("Quit File"))
		fileMenu.addAction(newAct4)
		

		newAct5 = QAction(QIcon("cut.png"), "Cut…", self )
		newAct5.setShortcut( "Ctrl+N" )
		newAct5.setToolTip(str("Cut File"))
		newAct5.setStatusTip(str("Cut File"))
		fileMenu.addAction(newAct5)
		

		newAct6 = QAction(QIcon("new.png"), "New…", self )
		newAct6.setShortcut( "Ctrl+N" )
		newAct6.setToolTip(str("New File"))
		newAct6.setStatusTip(str("New File"))
		fileMenu.addAction(newAct6)
		

		newAct7 = QAction(QIcon("paste.png"), "Paste…", self )
		newAct7.setShortcut( "Ctrl+V" )
		newAct7.setToolTip(str("Paste File"))
		newAct7.setStatusTip(str("Paste File"))
		fileMenu.addAction(newAct7)
		




def main(args):
	print(args)
	app = QApplication(args)
	window= MainWindow()
	window.resize(500,500)
	window.show()
	app.exec_()



if __name__ == "__main__":
	print("Exécution du programme")
	main(sys.argv)




	