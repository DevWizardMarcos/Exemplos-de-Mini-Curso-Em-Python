import qrcode

def gerar_qr_code(link):
    img = qrcode.make(link)
    img.save("meu github.png")
    print("QR Code salvo como qrcode.png")

gerar_qr_code("https://github.com/DevWizardMarcos?tab=repositories ")


# pip install qrcode[pil]