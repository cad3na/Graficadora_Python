#################################################################################
#Proyecto: Graficadora Python
#Archivo: graficar.py
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
from Tkinter import *
import ttk

class Graficadora(Frame):
	"""

	Esta clase provee un metodo facil para graficar un conjunto de puntos.

	"""
	def __init__(self):
		"""Inicializa el entorno ttk"""
		self.root = Tk()
		self.root.geometry("640x480")
		self.root.columnconfigure(0, weight = 1)
		self.root.rowconfigure(0, weight = 1)
		
	def dibujar_linea_de_grafica(self, x_ini, y_ini, x_fin, y_fin, escala_x = 1, escala_y = 1):
		"""Dibuja una linea entre punto y punto de la grafica, tomando en cuenta el autoescalamiento"""
		self.canvas.create_line(x_ini * escala_x, y_ini * escala_y, x_fin * escala_x, y_fin * escala_y)

	def dibujar_ejes(self, max_x, min_x, max_y, min_y):
		"""Dibuja los ejes x y y"""
		self.canvas.create_line(min_x, 0, max_x, 0)
		self.canvas.create_line(0, min_y, 0, max_y)

	def obtener_maximos(self, lista_x, lista_y):
		"""Obtiene el maximo y el minimo tanto de los puntos de x como de y"""
		max_x = max(lista_x)
		max_y = max(lista_y)
		min_x = min(lista_x)
		min_y = min(lista_y)
		return max_x, min_x, max_y, min_y

	def obtener_escala(self, max_x, min_x, max_y, min_y):
		"""Obtiene la escala para que la grafica abarque todo el espacio disponible"""
		rango_x = float(max_x - min_x)
		rango_y = float(max_y - min_y)

		escala_x = int(self.canvas.cget("width")) / rango_x
		escala_y = int(self.canvas.cget("height")) / rango_y
		return escala_x, escala_y

	def crear_superficie_de_dibujo(self):
		"""Crea el canvas sobre el que se dibujara la grafica"""
		self.canvas = Canvas(self.root)
		self.canvas.grid(column = 0, row = 0, sticky = (N, W, E, S))

	def invertir_eje_y(self, ys, escala_y):
		"""Invierte el eje y para que se muestre la grafica como debe de ser"""
		ys_inv = []
		altura_area_de_dibujo = int(self.canvas.cget("height"))
		for i in range(len(ys)):
			ys_inv.append(-1 * ys[i])
		for i in range(len(ys_inv)):
			ys_inv[i] += altura_area_de_dibujo / escala_y

		return ys_inv

	def graficar(self, xs, ys):
		"""Llama los metodos anteriores en el orden adecuado para dibujar correctamente la grafica"""
		if len(xs) == len(ys):
			self.xs, self.ys = xs, ys
		else:
			print "La longitud del primer arreglo no coincide con el del segundo."

		self.crear_superficie_de_dibujo()
		max_x, min_x, max_y, min_y = self.obtener_maximos(xs, ys)
		self.dibujar_ejes(max_x, min_x, max_y, min_y)
		esc_x, esc_y = self.obtener_escala(max_x, min_x, max_y, min_y)
		ys_inv = self.invertir_eje_y(ys, esc_y)

		for i in range(len(xs) - 1):
			self.dibujar_linea_de_grafica(xs[i], ys_inv[i], xs[i + 1], ys_inv[i + 1], esc_x, esc_y)

		self.root.mainloop()