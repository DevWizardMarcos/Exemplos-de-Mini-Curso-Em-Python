import qrcode

def gerar_qr_code(link, nome_arquivo="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)   
    
    img = qr.make_image(fill="black", back_color="white")
    img.save(nome_arquivo)
    print(f"QR Code salvo como {nome_arquivo}")

# Exemplo de uso
link = "https://github.com/DevWizardMarcos"
gerar_qr_code(link)
