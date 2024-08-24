import qrcode
from qrcode.image.styledpil import StyledPilImage

qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
qr.add_data("github.com/josedarlancarvalho")

imagem = qr.make_image(
    image_factory=StyledPilImage,
    embedded_image_path="logo.png"
)

imagem.save("qrcode_logo.png")
