# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlatoonAdminstrationSoftware.ui'
#
# Created: Thu Aug 10 08:48:16 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(255)
        sizePolicy.setVerticalStretch(255)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Pictures/GearIcon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(True)
        self.centralwidget = QtGui.QWidget(MainWindow)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setSizeIncrement(QtCore.QSize(0, 0))
        self.centralwidget.setBaseSize(QtCore.QSize(0, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_information = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_information.sizePolicy().hasHeightForWidth())
        self.tab_information.setSizePolicy(sizePolicy)
        self.tab_information.setObjectName("tab_information")
        self.gridLayout_4 = QtGui.QGridLayout(self.tab_information)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.infoListWidget = QtGui.QListWidget(self.tab_information)
        self.infoListWidget.setObjectName("infoListWidget")
        self.gridLayout_4.addWidget(self.infoListWidget, 0, 0, 1, 1)
        self.infoCalendarWidget = QtGui.QCalendarWidget(self.tab_information)
        self.infoCalendarWidget.setObjectName("infoCalendarWidget")
        self.gridLayout_4.addWidget(self.infoCalendarWidget, 0, 1, 2, 1)
        self.infoTextBrowser = QtGui.QTextBrowser(self.tab_information)
        self.infoTextBrowser.setObjectName("infoTextBrowser")
        self.gridLayout_4.addWidget(self.infoTextBrowser, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_information, "")
        self.tab_calendar = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_calendar.sizePolicy().hasHeightForWidth())
        self.tab_calendar.setSizePolicy(sizePolicy)
        self.tab_calendar.setMaximumSize(QtCore.QSize(10000, 1000))
        self.tab_calendar.setObjectName("tab_calendar")
        self.gridLayout_2 = QtGui.QGridLayout(self.tab_calendar)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.aptCalendarWidget = QtGui.QCalendarWidget(self.tab_calendar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aptCalendarWidget.sizePolicy().hasHeightForWidth())
        self.aptCalendarWidget.setSizePolicy(sizePolicy)
        self.aptCalendarWidget.setMaximumSize(QtCore.QSize(10000, 1000))
        self.aptCalendarWidget.setObjectName("aptCalendarWidget")
        self.gridLayout_2.addWidget(self.aptCalendarWidget, 0, 1, 4, 1)
        self.aptTextBrowser = QtGui.QTextBrowser(self.tab_calendar)
        self.aptTextBrowser.setObjectName("aptTextBrowser")
        self.gridLayout_2.addWidget(self.aptTextBrowser, 2, 0, 1, 1)
        self.aptListWidget = QtGui.QListWidget(self.tab_calendar)
        self.aptListWidget.setObjectName("aptListWidget")
        self.gridLayout_2.addWidget(self.aptListWidget, 1, 0, 1, 1)
        self.tabWidget.addTab(self.tab_calendar, "")
        self.tab_structure = QtGui.QWidget()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab_structure.sizePolicy().hasHeightForWidth())
        self.tab_structure.setSizePolicy(sizePolicy)
        self.tab_structure.setObjectName("tab_structure")
        self.tabWidget.addTab(self.tab_structure, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 27))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuGenerate_Report = QtGui.QMenu(self.menubar)
        self.menuGenerate_Report.setObjectName("menuGenerate_Report")
        self.menuTools = QtGui.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtGui.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAppointment_Calendar = QtGui.QAction(MainWindow)
        self.actionAppointment_Calendar.setObjectName("actionAppointment_Calendar")
        self.actionInformation_Board = QtGui.QAction(MainWindow)
        self.actionInformation_Board.setObjectName("actionInformation_Board")
        self.actionGenerate_All_Reports = QtGui.QAction(MainWindow)
        self.actionGenerate_All_Reports.setObjectName("actionGenerate_All_Reports")
        self.actionEdit_Database = QtGui.QAction(MainWindow)
        self.actionEdit_Database.setObjectName("actionEdit_Database")
        self.actionUpdate_Information_Board = QtGui.QAction(MainWindow)
        self.actionUpdate_Information_Board.setObjectName("actionUpdate_Information_Board")
        self.actionEdit_Database_2 = QtGui.QAction(MainWindow)
        self.actionEdit_Database_2.setObjectName("actionEdit_Database_2")
        self.menuFile.addAction(self.actionExit)
        self.menuGenerate_Report.addAction(self.actionGenerate_All_Reports)
        self.menuTools.addAction(self.actionUpdate_Information_Board)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuGenerate_Report.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Platoon Administration Software", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_information), QtGui.QApplication.translate("MainWindow", "Information", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_calendar), QtGui.QApplication.translate("MainWindow", "Appointments Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_structure), QtGui.QApplication.translate("MainWindow", "Platoon Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFile.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuGenerate_Report.setTitle(QtGui.QApplication.translate("MainWindow", "Generate Report", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTools.setTitle(QtGui.QApplication.translate("MainWindow", "Tools", None, QtGui.QApplication.UnicodeUTF8))
        self.actionExit.setText(QtGui.QApplication.translate("MainWindow", "Exit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAppointment_Calendar.setText(QtGui.QApplication.translate("MainWindow", "Appointment Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionInformation_Board.setText(QtGui.QApplication.translate("MainWindow", "Information Board", None, QtGui.QApplication.UnicodeUTF8))
        self.actionGenerate_All_Reports.setText(QtGui.QApplication.translate("MainWindow", "Generate All Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Database.setText(QtGui.QApplication.translate("MainWindow", "Edit Database", None, QtGui.QApplication.UnicodeUTF8))
        self.actionUpdate_Information_Board.setText(QtGui.QApplication.translate("MainWindow", "Update Information Board", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEdit_Database_2.setText(QtGui.QApplication.translate("MainWindow", "Edit Database", None, QtGui.QApplication.UnicodeUTF8))
