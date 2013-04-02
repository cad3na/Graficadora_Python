#################################################################################
#Proyecto: Graficadora Python
#Archivo: prueba.py
#Descripcion: En este archivo se encuentra un ejemplo de como llamar a un objeto
#             de la clase graficadora y despues su metodo graficar.
#Autor: Cadena Vega Roberto
#Version: 0.1
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