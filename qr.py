import pyqrcode
s=input("PLEASE ENTER CHARACTER")
b=pyqrcode.create(s)
b.svg('qr.svg',scale=5)
