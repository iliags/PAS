#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:24:33 2017

@author: rias
"""

import usb.core
import usb.util
import sys


import os
os.environ['PYUSB_DEBUG'] = 'debug'

import usb.core
usb.core.find()


"""
# find our device
dev = usb.core.find(idVendor=0xffff, idProduct=0x0035)

# was it found?
if dev is None:
    raise ValueError('Device not found')

if dev.is_kernel_driver_active(0): 
	try:
		dev.detach_kernel_driver(0)
	except usb.core.USBError as e:
		sys.exit("Could not detatch kernel driver: %s" % str(e)) 

	
endpoint = dev[0][(0,0)][0] 
print str(endpoint.read(endpoint.wMaxPacketSize)

"""

#print str(dev)