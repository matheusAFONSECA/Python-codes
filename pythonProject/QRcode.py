import qrcode   # importa a biblioteca que cria o QRcode

# define o link do objeto que cria o QRcode
img = qrcode.make(
    'https://github.com/matheusAFONSECA'
)

# salva a imagem do QRcode
img.save('myQRcode.png')
