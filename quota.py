#!/usr/bin/env python

import os

def tonumber(somestring):
	# convert the decimals in "somestring" into one number.
	return int(''.join(ch for ch in somestring if ch.isdigit()))

def getquota():
	cmd = "quota"	# To do: check if "quota" command exists
	for thisline in os.popen(cmd).readlines():
		'''
		# no quota for user
		Disk quotas for user sander (uid 1000): none
		'''
		'''
		Disk quotas for user piet (uid 1001):
		     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
		 /dev/mmcblk0p2    9032   20000   30000              55       0       0
		'''
		''' 
		# 'blocks' contains a star when above 'quota'
		Disk quotas for user piet (uid 1001): 
		     Filesystem  blocks   quota   limit   grace   files   quota   limit   grace
		 /dev/mmcblk0p2   24392*  20000   30000   7days      58       0       0        
		'''
		myline = thisline.rstrip()
		if myline.find("/") >= 0:
			# for each filesystem there is one line ...
			print "Debug: line is", myline
			(filesystem, blocksused, softmax, hardmax) = myline.split()[:4]
			print "used (kB):", tonumber(blocksused)	# used
			if softmax > 0:
				print "available (kB):", tonumber(softmax) - tonumber(blocksused)
			if hardmax > 0:
				print "availablegrace (kB):", tonumber(hardmax) - tonumber(blocksused) 

# Main
if __name__ == "__main__":
	getquota()

