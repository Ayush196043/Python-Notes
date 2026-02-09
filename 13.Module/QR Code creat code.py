import qrcode
#enter your data use to make code.
data = input("enter your code: ")
#Enter the class.
img = qrcode.QRCode(version= 2,
                    error_correction= qrcode.constants.ERROR_CORRECT_H,
                    box_size=10,
                    border=5)
#Add the data in class.
img.add_data(data)

img.make(fit = True)

#fill the color.
qr =img.make_image(fill_color="green",back="white")

#save the file.
qr.save("Python.png")
