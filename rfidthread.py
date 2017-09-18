#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 17:36:15 2017

"""
from PySide import QtCore
from Queue import Queue, Empty
from PySide.QtCore import Signal, Slot

import usb.core
import usb.util
import usb.control

import sys
import time


"""
This is a thread that runs in the background of the main application because
we would lock up the GUI when this is running otherwise. Multithreading in python
2.7 is for this reason only and not for increasing performance since it still
is an interpreted language. 

The initial RFID reader used returned the card number in a binary array format
that needs to be converted to decimal values before use. By default the RFID 
reader adds a newline character (the number 40) at the end but we don't need it
"""


class Worker_RFID(QtCore.QObject):
	
	notify = Signal(str)
	
	def __init__(self, queue, *args, **kwargs):
		QtCore.QObject.__init__(self, *args, **kwargs)
		self.queue = queue
		global  gCard;
	
		#This can be found by typing 'lsusb' and it will be listed as xxxx:xxxx
		#so it's read as <VendorID> : <ProductID>
		self.device = usb.core.find(idVendor=0xffff, idProduct=0x0035)
		
		#Make sure the device is connected and we can access it
		if self.device is None:
			raise ValueError('RFID reader not found')
		elif self.device.is_kernel_driver_active(0): 
			try:
				self.device.detach_kernel_driver(0)
			except usb.core.USBError as e:
				raise ValueError("Could not detatch kernel driver: %s" % str(e)) 
		
		#Create the endpoint (so I/O commands can be run)
		self.endpoint = self.device[0][(0,0)][0] 
		
		
	#Thread loop
	def run(self):
		self.active = True
		
		self.cardString = ""
		
		#Conversion chart which is a dictionary "Input: "Output"
		self.converter = {
				"30": "1",
				"31": "2",
				"32": "3",
				"33": "4",
				"34": "5",
				"35": "6",
				"36": "7",
				"37": "8",
				"38": "9",
				"39": "0"
			}
		
		while self.active:
			data = None
			
			#I am not certain what causes it but pyUSB throws a timeout error
			#which is harmless but still blocks the program so this is the 
			#workaround
			try:
				#If a card is detected then store it to an array for usage
				data = self.endpoint.read(self.endpoint.wMaxPacketSize, timeout=2)			
			except:
				pass
			
			#If we have data that isn't null
			if data:
				time.sleep(0.05)
				temp = str(data)
				data = None
				for x in range(0, len(temp)):
					if x+1 < len(temp):
						self.cardString += self.converter.get(temp[x]+temp[x+1], "")
			
				#If the card read is complete then send it up for verification
				
				
				if len(self.cardString) >= 7:
					#print "Pre-emit"
					#Send it up
					gCard = self.cardString
					self.notify.emit(gCard)
					#print "Post-emit"
					#Reset the string
					self.cardString = ""	
					#print "Reset"
			
			
		print "Finished Thread"
		
