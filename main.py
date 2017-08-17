__application___ = "Platoon Administration Software"
__module__ = "main"


from PySide import QtCore
from PySide import QtGui
from PySide import QtUiTools

#Standard or System Libraries
from Queue import Queue, Empty
import os.path
import time
import sys
import logging
import sqlite3
import re

#Custom Libraries and Data
#import profile as pr
from ui_files import pyMainWindow
import edituserdialog as edituser
import rfidthread as rThread




#Check for the data folder
dataPath = os.getcwd()+"/data/"
if not os.path.exists(dataPath):
	try:
		os.mkdirs(dataPath)
	except Exception:
		dataPath = os.getcwd()

#Setup logging format
logging.basicConfig(filename=dataPath + "mainapp.log", 
		format="%(asctime)-15s: %(name)-18s - %(levelname)-8s - %(module)-15s - %(funcName)-20s - %(lineno)-6d - %(message)s")

logger = logging.getLogger(name="main-gui")





#GUI Time YAAAAAAAAAAAY....fml.
class Main(QtGui.QMainWindow, pyMainWindow.Ui_MainWindow):
	
	#Set the path for the database and create a connection
	dbPath = dataPath + "pData.db"
	dbConn = sqlite3.connect(dbPath)
	
	def __init__(self, parent=None):
		super(Main, self).__init__(parent)
		self.setupUi(self)  
		
		#self.eWin = edituser.EditUserDialog()
		#self.eWin.show()
		
		#Setup the RFID reader thread
		self.queue = Queue()
		self.thread = QtCore.QThread(self)
		self.worker = rThread.Worker_RFID(self.queue)
		self.worker.moveToThread(self.thread)
		self.thread.started.connect(self.worker.run)
		self.thread.start()
		
		#Connect actions
		self.actionExit.triggered.connect(self.close)
		self.actionUpdate_Information_Board.triggered.connect(self.update_info_board)
		
		
		
		
		#Create the database if it doesn't exist
		self.dbCursor = self.dbConn.cursor()
		
		#Main table
		self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Main(edipi TEXT PRIMARY KEY, 
				rank TEXT,
				firstName TEXT, 
				middleName TEXT, 
				lastName TEXT, 
				suffix TEXT,
				mealCardTEXT, 
				squad TEXT, 
				billet TEXT, 
				mos INTEGER, 
				livingAddress TEXT, 
				mailingAddress TEXT, 
				easDate TEXT, 
				lastFour INTEGER, 
				phoneNumber TEXT, 
				personalEmail TEXT, 
				birthDate TEXT, 
				marritalStatus TEXT, 
				bloodType TEXT, 
				allergies TEXT, 
				rfidCard TEXT)""")
		 
		#Weapon table
		self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Weapons(id INTEGER PRIMARY KEY, 
		rifleSerial TEXT, 
		pistolSerial TEXT,
		edipi TEXT)""")
		
		#DLPT table
		self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS DLPT(id INTEGER PRIMARY KEY,
		dlptTitle TEXT,
		dlptDate TEXT,
		dlptScore TEXT,
		edipi TEXT)""")
		
		#Dependa table
		self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS Dependa(id INTEGER PRIMARY KEY, 
				firstName TEXT, 
				middleName TEXT, 
				lastName TEXT, 
				livingAddress TEXT, 
				mailingAddress TEXT,
				dob TEXT,
				edipi TEXT)""")
		
		#License table
		self.dbCursor.execute("""CREATE TABLE IF NOT EXISTS License(id INTEGER PRIMARY KEY,
		hmmwv INTEGER,
		sevenTon INTEGER,
		mwrap INTEGER,
		edipi TEXT)""")
		
		#Save the database
		self.dbConn.commit()
		
		
		
	def close(self):
		"""Exit the program (File->Exit)"""
		self.closeEvent()
		
		
	def closeEvent(self, event = None):
		self.worker.active = False
		self.thread.quit()
		self.thread.wait()
		self.dbConn.close()
		time.sleep(0.2)
		exit()
		
	
	def reports_generate_all(self):
		"""Generate all report formats"""
		pass
	
	def update_info_board(self):
		"""Allow the user to update the information board"""
		self.edit_user()
		pass
		
	def edit_user(self):
            self.eWin = edituser.EditUserDialog()
            self.eWin.show()
		

        
	
	#Information board things
	
	#Appointment board things
	
	#Platoon structure things
	
	

def main():
	QtCore.QCoreApplication.setApplicationName("Platoon Administration Software")
	QtCore.QCoreApplication.setApplicationVersion("0.1")
	QtCore.QCoreApplication.setOrganizationName("James Lennon")
	
	app = QtGui.QApplication(sys.argv)
	form = Main()
	form.show()
	sys.exit(app.exec_())
	app.deleteLater()
	

#Execute the application
if __name__ == "__main__":
	main()


