#lets make qrcode in 3line

#import qrcode "pip install qrcode"
import qrcode
img= qrcode.make('i am')
img.save(r'C:\Users\godsu\Desktop\python\New folder\qr.jpg')