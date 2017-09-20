from PySide.QtCore import *
from PySide.QtGui import *
from ui_files import pyEditWindow

import os.path
import time
import sys
import logging
import sqlite3
import re
import main


myEDIPI = ""
dataPath = os.getcwd()+"/data/"

class EditUserDialog(QDialog, pyEditWindow.Ui_editProfileDialog):
	
	#Set the path for the database and create a connection
	dbPath = dataPath + "pData.db"
	dbConn = sqlite3.connect(dbPath)
	
	
	def __init__(self, EDIPI): #parent=None):
		super(EditUserDialog, self).__init__(None)
		self.setupUi(self)
		self.isNewAccount = False


		self.dbCursor = self.dbConn.cursor()
		
		#Rank box populating
		self.rankBox.addItem("Pvt")
		self.rankBox.addItem("PFC")
		self.rankBox.addItem("LCpl")
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
		self.suffixBox.addItem("VII")
		self.suffixBox.addItem("VIII")
		self.suffixBox.addItem("IX")
		self.suffixBox.addItem("X")
		
		
		#Superviser rank box
		self.superRankBox.addItem("Pvt")
		self.superRankBox.addItem("PFC")
		self.superRankBox.addItem("LCpl")
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
		
		
		
		myEDIPI = EDIPI
		#print "Value: " + self.rankBox.currentText() + ""
		if(myEDIPI == "new"):
			print "Initializing"
			self.isNewAccount = True
		elif myEDIPI:
			print "Loading data"	
			#Load values from the database
			self.dbCursor.execute("SELECT * FROM Main WHERE edipi=(?)", (myEDIPI, ))
			records = self.dbCursor.fetchall()
		
			for record in records:
				#self.edipiEdit = edipi
								
				index = self.rankBox.findText(record[1], Qt.MatchFixedString)
				if index >= 0:
					self.rankBox.setCurrentIndex(index)
					
				self.firstEdit.setText(record[2])
				self.middleEdit.setText(record[3])
				self.lastEdit.setText(record[4])
				
				index = self.suffixBox.findText(record[5], Qt.MatchFixedString)
				if index >= 0:
					self.suffixBox.setCurrentIndex(index)
					
				self.mealCardEdit.setText(record[6])				
				
				index = self.superRankBox.findText(record[7], Qt.MatchFixedString)
				if index >= 0:
					self.superRankBox.setCurrentIndex(index)
				
				self.superLastEdit.setText(record[8])
				
				index = self.billetBox.findText(record[9], Qt.MatchFixedString)
				if index >= 0:
					self.billetBox.setCurrentIndex(index)
				
				self.billetEdit.setText(record[10])
				self.mosEdit.setText(str(record[11]))
				self.residentialEdit.setText(record[12])
				self.mailingEdit.setText(record[13])
				
				tempDate = record[14]
				self.easEdit.setDate(QDate(int(tempDate.split('/')[0]), int(tempDate.split('/')[1]), int(tempDate.split('/')[2])))
				
				self.last4Edit.setText(str(record[15]))
				self.homePhoneEdit.setText(str(record[16]))
				self.lineEdit_3.setText(record[17])
				self.emailEdit.setText(record[18])
				
				tempDate = record[19]
				self.dobEdit.setDate(QDate(int(tempDate.split('/')[0]), int(tempDate.split('/')[1]), int(tempDate.split('/')[2])))
				#self.dobEdit.setText(record[19])
				
				
				index = self.bloodBox.findText(record[20], Qt.MatchFixedString)
				if index >= 0:
					self.bloodBox.setCurrentIndex(index)
				
				
				
				self.allergyEdit = record[21]
				self.rfidEdit = record[22]				
				
		else:
			raise ValueError('Error finding or creating account')

		
		
		
	def StandardButtonPress(self, button):
		sb = self.buttonBox.standardButton(button)
		if sb == QDialogButtonBox.Save:
			self.SaveData()
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
		
		
	def SaveData(self):
		#ADD DATA CHECKS/PROTECTION
		params = (
				self.edipiEdit.text(),
				self.rankBox.currentText(),
				self.firstEdit.text(),
				self.middleEdit.text(),
				self.lastEdit.text(),
				self.suffixBox.currentText(),
				self.mealCardEdit.text(),
				self.superRankBox.currentText(),
				self.superLastEdit.text(),
				self.billetBox.currentText(),
				self.billetEdit.text(),
				int(self.mosEdit.text()),
				self.residentialEdit.toPlainText(),
				self.mailingEdit.toPlainText(),
				self.easEdit.text(),
				int(self.last4Edit.text()),
				self.homePhoneEdit.text(),
				self.lineEdit_3.text(),
				self.emailEdit.text(),
				self.dobEdit.text(),
				
				self.bloodBox.currentText(),
				self.allergyEdit.toPlainText(),
				self.rfidEdit.toPlainText(),
		)
		if(self.isNewAccount):
			print "Creating entry"
			self.dbCursor.execute("""INSERT INTO Main VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""", params)
				#Add one for marritalStatus
		else:
			print "Updating Entry"
			self.dbCursor.execute("""UPDATE Main SET edipi = ?, 
				rank = ?,
				firstName = ?, 
				middleName = ?, 
				lastName = ?, 
				suffix = ?,
				mealCard = ?, 
				superRank = ?, 
				superName = ?, 
				billet = ?,
				billetText = ?,
				mos = ?, 
				livingAddress = ?, 
				mailingAddress = ?, 
				easDate = ?, 
				lastFour = ?, 
				phoneNumber = ?,
				cellNumber = ?, 
				personalEmail = ?, 
				birthDate = ?, 
				marritalStatus = ?
				bloodType = ?, 
				allergies = ?, 
				rfidCard = ?""", params)
				
		self.dbConn.commit()
		print "Saved"
