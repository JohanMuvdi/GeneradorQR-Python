import qrcode
from PIL import Image

# Valores de entrada
nombre_del_participante = input("Nombre y Apellido: ")
documento_identificacion = input('Documento de identidad: ')
datos_del_participante = nombre_del_participante + ' ' + documento_identificacion
codigo_qr = qrcode.make(datos_del_participante)

# Valores del codigo QR
nombre_imagen = nombre_del_participante + '.png'
archivo_imagen = open(nombre_imagen, 'wb')
codigo_qr.save(archivo_imagen)
archivo_imagen.close()