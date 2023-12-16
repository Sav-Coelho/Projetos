### No presente código irei gerar uma solução em python visando automatizar criação de códigos QR###

import qrcode


def gerar_qrcode(text):
    qr = qrcode.QRCode(
        version=1,
        error_correction= qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4

    )

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color="yellow", back_color="black")
    img.save("qrimg001.png")


url = input("Digite sua URL: ")
gerar_qrcode(url)
