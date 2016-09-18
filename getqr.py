import qrtools
import sys

qr = qrtools.QR()



qr.decode(sys.argv[1])
print qr.data

#"""

"""
for param in sys.argv:
	qr.decode(param)
	print qr.data


#"""