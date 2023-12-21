import qrcode
import image

qr = qrcode.QRCode (
    version = 15, 
     box_size = 10,
     border = 5 # It is the white part of the image --border in all 4 sides with white color

)

data = "https://github.com/komlalex"

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "white")
img.save("komla_qr_code.png")
