#################################################################################
#Proyecto: Graficadora Python
#Archivo: prueba.py
#Descripcion: En este archivo se encuentran definidas todas las clases necesarias
#             para el funcionamiento basico de las matematicas asociadas al 
#             dibujo de formas basicas y la extraccion de parametros asociados a
#             estas.
#Autor: Cadena Vega Roberto
#Version: 0.2
#Notas de la Version: Clases Vector y Linea terminadas, clase Poligono 
#                     aun no concluida; para los metodos extraer_vertices,
#                     calcular_area y revisar_lados aun no se tienen maneras
#                     eficientes de implementar.
#Fecha: 14/02/13
#################################################################################
from graficar import Graficadora
from math import sin, pi

def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step

tau = 2 * pi
temp = drange(0.0, tau, 0.01)

xs = [n for n in temp]
ys = [sin(n) for n in xs]

pizza = Graficadora()

pizza.graficar(xs, ys)