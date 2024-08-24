#gerador de qrcode
import qrcode

imagem = qrcode.make("github.com/josedarlancarvalho")
imagem.save("qrcode.png")