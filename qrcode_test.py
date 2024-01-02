### No presente código irei gerar uma solução em python visando automatizar criação de códigos QR###

import qrcode
import random


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
    lista1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k' ,'l' ,'m', 'n', 'q', 'o', 'p', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
    lista2 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    caract1= random.choice(lista1)
    caract2= random.choice(lista2)
    caract3= ".png"
    img.save(caract1 + caract2 + caract3)


url = input("Digite sua URL: ")
gerar_qrcode(url)
