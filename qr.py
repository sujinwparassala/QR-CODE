import pyqrcode
s=input("PLEASE ENTER CHARACTER")
b=pyqrcode.create(s)
x = input("Enter the size you want")
b.svg('qr.svg',scale=int(x))
