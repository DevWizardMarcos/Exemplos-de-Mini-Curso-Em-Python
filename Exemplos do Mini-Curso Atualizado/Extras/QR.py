import qrcode

def gerar_qr_code(link):
    img = qrcode.make(link)
    img.save("meu whats .png")
    print("QR Code salvo como qrcode.png")

gerar_qr_code(" https://wa.me/qr/6SZGDHDE5XWKI1 ")


# pip install qrcode[pil]