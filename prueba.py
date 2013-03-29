from graficar import Graficadora

xs = range(100)
ys = [n**2 for n in xs]

pizza = Graficadora()

pizza.graficar(xs, ys)
pizza.graficar(xs, xs)