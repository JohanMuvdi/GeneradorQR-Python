import xlrd
import qrcode
import smtplib
from PIL import Image # Para cargar Imagenes
from PIL import ImageDraw # Para dibujar sobre Imagenes (Texto, dibujos, lineas)
from PIL import ImageFont # Para configurar las fuentes de los textos

# Para leer el archivo excel
rutaArchivo = ("C:\\Users\\johan\\OneDrive\\Escritorio\\participantes.xls")
 
abrirArchivo = xlrd.open_workbook(rutaArchivo)
hoja = abrirArchivo.sheet_by_index(0)
indice = 1
participante = hoja.cell_value(indice, 0)
numeroDocumento = str(int(hoja.cell_value(indice, 1)))

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

print(f'El codigo QR de {nombre_del_participante} esta Listo!')


