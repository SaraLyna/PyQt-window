import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MainWindow(QMainWindow):
    
	def __init__(self):
		QMainWindow.__init__(self)
		bar=self.menuBar()
		fileMenu = bar.addMenu( "File" )

		status=self.statusBar()
		tools=QToolBar()
		self.addToolBar(tools)


		self.zoneCentrale =QTextEdit(self)
		self.setCentralWidget(self.zoneCentrale)



		newAct1 = QAction(QIcon("open.png"), "Open…", self )
		newAct1.setShortcut( "Ctrl+N" )
		newAct1.setToolTip(str("Open File"))
		newAct1.setStatusTip(str("Open File"))
		fileMenu.addAction(newAct1)
		tools.addAction(newAct1)
		newAct1.triggered.connect(self.openFile)



		newAct2 = QAction(QIcon("save.png"), "Save…", self )
		newAct2.setShortcut( "Ctrl+S" )
		newAct2.setToolTip(str("Save File"))
		newAct2.setStatusTip(str("Save File"))
		fileMenu.addAction(newAct2)
		tools.addAction(newAct2)
		newAct2.triggered.connect(self.saveFile)


		newAct3 = QAction(QIcon("copy.png"), "Copy…", self )
		newAct3.setShortcut( "Ctrl+C" )
		newAct3.setToolTip(str("Copy File"))
		newAct3.setStatusTip(str("Copy File"))
		fileMenu.addAction(newAct3)
		tools.addAction(newAct3)
		newAct3.triggered.connect(self.copyFile)


		newAct4 = QAction(QIcon("quit.png"), "Quit…", self )
		newAct4.setShortcut( "Ctrl+Q" )
		newAct4.setToolTip(str("Quit File"))
		newAct4.setStatusTip(str("Quit File"))
		fileMenu.addAction(newAct4)
		tools.addAction(newAct4)
		newAct4.triggered.connect(self.quitApp)


		newAct5 = QAction(QIcon("cut.png"), "Cut…", self )
		newAct5.setShortcut( "Ctrl+N" )
		newAct5.setToolTip(str("Cut File"))
		newAct5.setStatusTip(str("Cut File"))
		fileMenu.addAction(newAct5)
		tools.addAction(newAct5)
		newAct5.triggered.connect(self.cutFile)



		newAct6 = QAction(QIcon("new.png"), "New…", self )
		newAct6.setShortcut( "Ctrl+N" )
		newAct6.setToolTip(str("New File"))
		newAct6.setStatusTip(str("New File"))
		fileMenu.addAction(newAct6)
		tools.addAction(newAct6)
		newAct6.triggered.connect(self.newFile)


		newAct7 = QAction(QIcon("paste.png"), "Paste…", self )
		newAct7.setShortcut( "Ctrl+V" )
		newAct7.setToolTip(str("Paste File"))
		newAct7.setStatusTip(str("Paste File"))
		fileMenu.addAction(newAct7)
		tools.addAction(newAct7)
		newAct7.triggered.connect(self.pasteFile)



	def openFile(self):
		fileName = QFileDialog.getOpenFileName( self,"Open File","sara.txt",
		"*.txt")
		print(fileName)

		file=QFile(fileName[0])
		file.open(QFile.ReadOnly)
		qs=QTextStream(file)
		self.zoneCentrale.setPlainText(qs.readAll())



	def saveFile(self):
		fileName2 = QFileDialog.getSaveFileName( self,"Save File","lol.txt",
		"*.txt")
		print(fileName2)
		file2=QFile(fileName2[0])
		file2.open(QFile.WriteOnly)
		qs=QTextStream(file2)
		self.zoneCentrale.toPlainText()
	
	def quitApp(self):
		print("app quit")
		self.close()
		
		
		
		
	def closeEvent(self, event):
		reply = QMessageBox.question(self, 'Confirmation', 'Êtes-vous sûr de vouloir quitter ?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
		if reply == QMessageBox.Yes:
			event.accept()
		else:
			event.ignore()
            
            
            
	def pasteFile(self):
		print("paste File")
		clipboard = QApplication.clipboard()
		text = clipboard.text()
		cursor = self.zoneCentrale.textCursor()
		cursor.insertText(text)
		self.zoneCentrale.setTextCursor(cursor)



	def cutFile(self):
		print("cut file")
		cursor = self.zoneCentrale.textCursor()
		selected_text = cursor.selectedText()
		clipboard = QApplication.clipboard()
		clipboard.setText(selected_text)
		cursor.removeSelectedText()



	def newFile(self):
		print("new file")
		self.zoneCentrale.clear()


	def copyFile(self):
		print("copy file")
		cursor = self.zoneCentrale.textCursor()
		selected_text = cursor.selectedText()
		clipboard = QApplication.clipboard()
		clipboard.setText(selected_text)
		
		



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
