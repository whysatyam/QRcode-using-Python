import qrcode

img = qrcode.make("https://twitter.com/whysatyam")
img.save("Satyam'sQRcode.jpg")
