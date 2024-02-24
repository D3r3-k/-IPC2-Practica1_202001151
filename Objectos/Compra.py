from Objectos.Cliente import Cliente
from Objectos.Producto import Producto


class Compra:
    def __init__(self, id: int, cliente: Cliente):
        self.id: int = id
        self.cliente: Cliente = cliente
        self.lista_productos: list[Producto] = []
        self.total: float = 0
        self.impuesto: float = 0

    def agregar_producto(self, producto: Producto):
        self.lista_productos.append(producto)
        self.total += producto.price
        self.calcular_impuesto()

    def calcular_impuesto(self):
        self.impuesto = round(self.total * 0.12, 2)
