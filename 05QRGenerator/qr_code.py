import qrcode
from PIL import Image


# to introducte text for qr code

url  = input("put your url here for generate QR Code: ")
qr = qrcode.make(url)

#to create image

qr_name = input("introduce name for image ")+'.png'
qr_file  = open(qr_name, 'wb')

qr.save(qr_file )
qr_file.close

qr_route = './'+qr_name
Image.open(qr_route).show()

