class Inventario:
    def __init__(self):
        self.lista_de_productos = []
    
    def agragar_producto(self, producto):
        self.lista_de_productos.append(producto)

    def actualizar_inventario(self, producto, cantidad):
        for prod in self.lista_de_productos:
            if prod.nombre == producto.nombre:
                prod.actualizar_cantidad(cantidad)

    def generar_alerta(self, umbrall_minimo):
        alertas = [prod.nombre for prod in self.lista_de_productos if prod.cantidad < umbrall_minimo]
        return f"Productos por debajo del umbral: {', '.join(alertas)}"if alertas  else "no hay ningun producto por debajo del umbrall minimo "