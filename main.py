#funciones par ala interface de  la consola 

from clases.mascota import Perro
from clases.cliente import Cliente
from clases.venta import Venta
from clases.inventario import Inventario
from clases.producto import Producto
from clases.mascota import Gato

def registrar_mascota():
    tipo = input ("ingrese el tipo de mascota perro/gato: ").strip().lower()
    nombre = input ("ingrese el nombre: ")
    edad = int(input ("edad de la mascota: "))
    salud = input ("Estado salud de la mascota: ")
    precio = float(input ("Precio de la mascota: "))

    if tipo == 'perro':
        raza = input("Raza de la mascota")
        nivel_de_energia = input("nivel de energia")
        mascota = Perro(nombre, edad, salud, precio, raza, nivel_de_energia)

    elif tipo == 'gato':
        raza = input("Raza de la mascota: ")
        independencia = input("Nivel de independencia del gato: ")
        mascota = Perro(nombre, edad, salud, precio, raza, independencia )

    else:
        print("Tipo de mascota no encontrada: ")

        return mascota

def registrar_cliente():
    nombre = input ("ingrese el nombre: ")
    direccion = input ("ingrese la direccion: ")
    telefono = input ("Telefono del cliente: ")
    cliente = Cliente(nombre, direccion, telefono)
    return cliente

def registrar_producto():
    nombre = input ("Nombre del producto: ")
    categoria = input ("Categoria del producto: ")
    precio = input ("Precio del produco: ")
    cantidad = int(input ("Cantidad de producto: "))
    producto = Producto(nombre, categoria, precio, cantidad)
    return producto

def registrar_venta(cliente, inventario):
    nombre_cliente = input("Nombre del cliente: ")
    cliente - next((c for c in cliente if c.nombre == nombre_cliente), None)
    if not cliente:
        print("Cliente no encontrado: ")
        return
    
    productos = []

    while True:
        nombre_prodcutos = input("Nombre del producto (deja vacio para finalizar): ")
        if not nombre_prodcutos:
            break
        producto = next((p for p in inventario.lista_de_productos if p.nombre == nombre_prodcutos ), None)
        if producto:
            producto.append(producto)
        else:
            print("Producto no encontrado: ")

        if productos:
            venta = Venta(cliente, producto)
            venta.registrar_venta()
            print("La venta se ha registrado con exito")
        else:
            print("No se ha registrado venta ")

def mostrar_menu():
    print("\n  ---- Menu de gestion patas felices ----")
    print("1) Registrar mascota")
    print("2) Registrar cliente")
    print("3) Registrar producto")
    print("4) Registrar venta")
    print("5) Mostrar informacion de mascota")
    print("6) Mostrar informacion de cliente ")
    print("7) Mostrar informacion de producto")
    print("8) Generar alerta inventario")
    print("9) Salir")

def main():
    mascotas = []
    clientes = []
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("selecciona una opcion: ")

        if opcion == '1':
            mascota = registrar_mascota()
            if mascota:
                mascota.append(mascota)
                print("Mascota registrda")
        elif opcion == '2':
            cliente = registrar_cliente()
            if cliente:
                cliente.append(cliente)
                print("cliente registrdo")
        elif opcion == '3':
            producto = registrar_producto()
            if producto:
                inventario.agragar_producto(producto)
                print("producto registrdo")
        elif opcion == '4':
            registrar_venta(clientes, inventario)
        elif opcion == '5':
            for mascota in mascotas:
                print(mascota.mostrar_informacion())
                if isinstance(mascota, Perro) or isinstance (mascota, Gato):
                    print(mascota.mostrar_caracteristicas())
        elif opcion == '6':
            for cliente in clientes:
                print (cliente.mostrar_informacion())
        elif opcion == '7':
            for producto in inventario.lista_de_productos:
                print (producto.mostrar_informacion())
        elif opcion == '8':
            umbrall_minimo = int(input("ingrese el umbrall minimo: "))
            print(inventario.generar_alerta(umbrall_minimo))
        elif opcion == '9':
            print("Saliendo del sistema: ")
            break
        else:
            print("opcion no valida, intentenlo nuevament: ")

if __name__ == '__main__':
    main()
      




    

