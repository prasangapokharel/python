import qrcode
qr = qrcode.QRCode(
    version=1,
    box_size=10,
    border=4,
)

#Add data in qr code
qr.add_data('I am prasanga')
qr.make(fit=True)

#create image from qr code
img = qr.make_image(fill_colors="black", back_color="white")

#save the image
img.save(r'C:\Users\godsu\Desktop\python\New folder\qrcode.jpg')