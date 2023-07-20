from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import legal
ancho, alto = legal
lista = []
productos = []

for i in range(6):
    lista.append(i)
    productos.append(input("Ingresa tu producto "))
#CAMBIEN SU RUTA
ruta = "C:/Users/Kevo/Escritorio/listas/"
c = canvas.Canvas(ruta+'variosProductos.pdf')
c.setPageSize((ancho, alto))
decremento = 20
inicialX = 200
inicialY = 950
incremento = 60
contadorElementos = 0
for i in range(len(lista)):
    c.setFont('Helvetica', 15)
    contadorElementos+=1
    c.drawString(inicialX, inicialY,str(lista[i]))
    c.drawString(inicialX + incremento, inicialY,str(productos[i]))
    inicialY = inicialY-decremento
    if(contadorElementos==2):
        c.showPage()
        inicialY = 950
        contadorElementos=0   

c.save()