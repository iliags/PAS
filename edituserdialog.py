from PySide.QtCore import *
from PySide.QtGui import *

from ui_files import pyEditWindow

import os.path
import time
import sys
import logging
import sqlite3
import re

dataPath = os.getcwd()+"/data/"
edipi = ""

class EditUserDialog(QDialog, pyEditWindow.Ui_editProfileDialog):
	
	#Set the path for the database and create a connection
	dbPath = dataPath + "pData.db"
	dbConn = sqlite3.connect(dbPath)
	
	def __init__(self, parent=None):
		super(EditUserDialog, self).__init__(parent)
		self.setupUi(self)


		self.dbCursor = self.dbConn.cursor()
		
		#Rank box populating
		self.rankBox.addItem("Pvt")
		self.rankBox.addItem("PFC")
		self.rankBox.addItem("Cpl")
		self.rankBox.addItem("Sgt")
		self.rankBox.addItem("SSgt")
		self.rankBox.addItem("GySgt")
		self.rankBox.addItem("MSgt")
		self.rankBox.addItem("MGySgt")
		self.rankBox.addItem("SgtMaj")
		
		self.rankBox.addItem("WO")
		self.rankBox.addItem("CWO2")
		self.rankBox.addItem("CWO3")
		self.rankBox.addItem("CWO4")
		
		self.rankBox.addItem("2ndLt")
		self.rankBox.addItem("1stLt")
		self.rankBox.addItem("Capt")
		self.rankBox.addItem("Maj")
		self.rankBox.addItem("LtCol")
		self.rankBox.addItem("Col")
		self.rankBox.addItem("BGen")
		self.rankBox.addItem("MajGen")
		self.rankBox.addItem("LtGen")
		self.rankBox.addItem("Gen")
		
		
		#Suffix box
		self.suffixBox.addItem("")
		self.suffixBox.addItem("Jr")
		self.suffixBox.addItem("Sr")
		self.suffixBox.addItem("I")
		self.suffixBox.addItem("II")
		self.suffixBox.addItem("III")
		self.suffixBox.addItem("IV")
		self.suffixBox.addItem("V")
		self.suffixBox.addItem("VI")
		
		
		#Superviser rank box
		self.superRankBox.addItem("Pvt")
		self.superRankBox.addItem("PFC")
		self.superRankBox.addItem("Cpl")
		self.superRankBox.addItem("Sgt")
		self.superRankBox.addItem("SSgt")
		self.superRankBox.addItem("GySgt")
		self.superRankBox.addItem("MSgt")
		self.superRankBox.addItem("MGySgt")
		self.superRankBox.addItem("SgtMaj")
		
		
		#Billets
		self.billetBox.addItem("")
		self.billetBox.addItem("Radio Transmission Operator")
		self.billetBox.addItem("Assistant Team Leader")
		self.billetBox.addItem("Team Leader")
		self.billetBox.addItem("Squad Leader")
		self.billetBox.addItem("Platoon Sergeant")
		
		self.billetBox.addItem("Other")
		
		
		#Blood types
		self.bloodBox.addItem("")
		self.bloodBox.addItem("O-")
		self.bloodBox.addItem("O+")
		self.bloodBox.addItem("B-")
		self.bloodBox.addItem("B+")
		self.bloodBox.addItem("A-")
		self.bloodBox.addItem("A+")
		self.bloodBox.addItem("AB-")
		self.bloodBox.addItem("AB+")
		
		#Action connections
		self.buttonBox.clicked.connect(self.StandardButtonPress)
		self.buttonAdd.clicked.connect(self.AddDLPT)
		self.buttonRemove.clicked.connect(self.RemoveDLPT)
		
		
		
		
		
		
		#Must be last
		edipi = self.edipiEdit.text()
		
		#Load values from the database
		#self.dbCursor.execute("""SELECT * FROM DLPT WHERE edipi = ?""", edipi)
		
		
	def StandardButtonPress(self, button):
		sb = self.buttonBox.standardButton(button)
		if sb == QDialogButtonBox.Save:
			self.dbConn.commit()
		elif sb == QDialogButtonBox.Cancel:
			self.close()
		
		
		
	def AddDLPT(self):
		lang = self.dlptLanguage.text()
		score = self.dlptScore.text()
		date = self.dlptDate.date()
		edipi = self.edipiEdit.text()
		
		if not lang:
			msgBox = QMessageBox.warning(self, self.tr("PAS"), self.tr("Please enter a language"))
			return
		elif not score:
			msgBox = QMessageBox.warning(self, self.tr("PAS"), self.tr("Please enter a score"))
			return
		elif not edipi:
			msgBox = QMessageBox.warning(self, self.tr("PAS"), self.tr("Please enter a valid EDIPI"))
			return
		
		#Update the table
		currentRowCount = self.tableWidget.rowCount()
		
		self.tableWidget.insertRow(currentRowCount)
		self.tableWidget.setItem(currentRowCount, 0, QTableWidgetItem(lang))
		self.tableWidget.setItem(currentRowCount, 1, QTableWidgetItem(date))
		self.tableWidget.setItem(currentRowCount, 2, QTableWidgetItem(score))
		
		#Save the DLPT score in the DLPT db
		parameters = (None, lang, date, score, edipi)
		self.dbCursor.execute("""INSERT INTO DLPT VALUES (?, ?, ?, ?, ?)""", parameters)
		self.dbConn.commit()

	
		
	
	
	def RemoveDLPT(self):
		pass
		
		