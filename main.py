# Objetos
from Objectos.Producto import Producto
from Objectos.Cliente import Cliente
from Objectos.Compra import Compra

# Listas
db_productos: list[Producto] = []
db_clientes: list[Cliente] = []
db_compras: list[Compra] = []

# Funciones


def main():
    salir = False
    while not salir:
        try:
            limpiar()
            print("|===============[ MENÚ PRINCIPAL ]===============|"
                  "\n| 1. Registrar Producto"
                  "\n| 2. Registrar Cliente"
                  "\n| 3. Realizar Compra"
                  "\n| 4. Reporte de Compra"
                  "\n| 5. Datos del Estudiante"
                  "\n| 6. Salir"
                  "\n|===============[ MENÚ PRINCIPAL ]===============|")
            option = int(input("Ingrese una opción: "))
            match option:
                case 1:
                    try:
                        menu_registrar_producto()
                    except Exception as e:
                        input(f"\nErr: {e}"
                              "\nPresione una tecla para continuar...")
                case 2:
                    try:
                        menu_registrar_cliente()
                    except Exception as e:
                        input(f"\nErr: {e}"
                              "\nPresione una tecla para continuar...")
                case 3:
                    try:
                        menu_realizar_compra()
                    except Exception as e:
                        input(f"\nErr: {e}"
                              "\nPresione una tecla para continuar...")
                case 4:
                    try:
                        menu_reporte_compra()
                    except Exception as e:
                        input(f"\nErr: {e}"
                              "\nPresione una tecla para continuar...")
                case 5:
                    datos_estudiante()
                case 6:
                    salir = True
                case _:
                    input("\nOpción no válida"
                          "\nPresione una tecla para continuar...")
        except Exception as e:
            input(f"\nSolo se admiten números enteros. Intente de nuevo."
                  f"\nErr: {e}"
                  "\nPresione una tecla para continuar...")


def menu_registrar_producto():
    limpiar()
    print("|===============[ REGISTRAR PRODUCTO ]===============|"
          "\n| Por favor ingrese los datos del producto:")
    code = input("| Código del Producto: ")
    for producto in db_productos:
        if producto.code == code:
            input("\n|===============[ ERROR ]===============|"
                  "\n|   El código de producto ya existe.    |"
                  "\n|  Presione una tecla para continuar... |")
            return
    nombre = input("| Nombre del Producto: ")
    desc = input("| Descripción: ")
    precio = float(input("| Precio Unitario: "))
    nuevo = Producto(code, nombre, desc, precio)
    db_productos.append(nuevo)
    input("|===============[ REGISTRAR PRODUCTO ]===============|"
          "\n\nProducto registrado con éxito."
          "\nPresione una tecla para continuar...")


def menu_registrar_cliente():
    limpiar()
    print("|===============[ REGISTRAR CLIENTE ]===============|"
          "\n| Por favor ingrese los datos del cliente:")
    nombre = input("| Nombre del Cliente: ")
    email = input("| Correo Electrónico: ")
    nit = input("| NIT: ")
    nuevo = Cliente(nombre, email, nit)
    db_clientes.append(nuevo)
    input("|===============[ REGISTRAR CLIENTE ]===============|"
          "\n\n Cliente registrado con éxito."
          "\n Presione una tecla para continuar...")


def menu_realizar_compra():
    limpiar()
    print("|===============[ REALIZAR COMPRA ]===============|")
    nit = input("| NIT del Cliente: ")
    cliente: Cliente = buscar_cliente(nit)
    if cliente is None:
        input("\n|===============[ ERROR ]===============|"
              "\n|      Cliente no encontrado.           |"
              "\n|  Presione una tecla para continuar... |"
              "\n|=======================================|")
        return
    menu_opciones_compra(cliente)


def menu_opciones_compra(cliente: Cliente):
    limpiar()
    factura: Compra = Compra(len(db_compras)+1, cliente)
    salir = False
    while not salir:
        limpiar()
        print("|===============[ MENÚ COMPRA ]===============|"
              "\n| 1. Agregar Producto"
              "\n| 2. Terminar Compra y Generar Factura"
              "\n|==================[ MENÚ COMPRA ]===============|")
        option = int(input("Ingrese una opción: "))
        match option:
            case 1:
                print("\n|===============[ BIENVENIDO ]===============|"
                      f"\n| Nombre: {cliente.name}"
                      f"\n| NIT: {cliente.nit}"
                      f"\n| Correo: {cliente.email}"
                      f"\n|=========================================================|"
                      f"\n|                      PRODUCTOS                          |"
                      f"\n|=========================================================|")
                for producto in db_productos:
                    print(f"|"
                          f"\n|===[Nombre: {producto.name}]"
                          f"\n| Código: {producto.code}"
                          f"\n| Descripción: {producto.description}"
                          f"\n| Precio: {producto.price}")
                code = input("\n|>| Código del Producto: ")
                producto: Producto = buscar_producto(code)
                if producto is None:
                    input("\n|===============[ ERROR ]===============|"
                          "\n|      Producto no encontrado.           |"
                          "\n|  Presione una tecla para continuar... |"
                          "\n|=======================================|")
                    continue
                factura.agregar_producto(producto)
                input(f"\n\n Producto agregado con éxito."
                      f"\n Presione una tecla para continuar...")
            case 2:
                if len(factura.lista_productos) == 0:
                    input("\n|===============[ ERROR ]===============|"
                          "\n|      No hay productos en la factura. |"
                          "\n|  Presione una tecla para continuar... |"
                          "\n|=======================================|")
                    return
                db_compras.append(factura)
                salir = True
            case _:
                input("\nOpción no válida"
                      "\nPresione una tecla para continuar...")
    input("\n|===============[ COMPRA TERMINADA ]===============|"
          "\n|      Factura generada con éxito.                 |"
          "\n|      Presione una tecla para continuar...        |"
          "\n|==================================================|")


def menu_reporte_compra():
    limpiar()
    if len(db_compras) == 0:
        input("|===============[ ERROR ]===============|"
              "\n|      No hay facturas registradas.     |"
              "\n|  Presione una tecla para continuar... |"
              "\n|=======================================|")
        return
    print("|===============[ REPORTES DE COMPRA ]===============|")
    for compra in db_compras:
        print(f"| ID: {compra.id}")
    id = int(input("\n|>| Ingrese el ID de la Compra: "))
    compra: Compra = buscar_compra(id)
    if compra is None:
        input("\n|===============[ ERROR ]===============|"
              "\n|      Factura no encontrada.           |"
              "\n|  Presione una tecla para continuar... |"
              "\n|=======================================|")
        return
    print(f"|===============[ REPORTE DE COMPRA #{compra.id} ]===============|"
          f"\n|"
          f"\n| CLIENTE:"
          f"\n|     |>| Nombre: {compra.cliente.name}"
          f"\n|     |>| Correo: {compra.cliente.email}"
          f"\n|     |>| NIT: {compra.cliente.nit}"
          f"\n| ARTÍCULOS COMPRADOS:")
    for producto in compra.lista_productos:
        print(f"|     |>| Nombre: {producto.name}"
              f"\n|         |>| Código: {producto.code}"
              f"\n|         |>| Descripción: {producto.description}"
              f"\n|         |>| Precio: {producto.price}")
    print(f"| Total: Q{compra.total}"
          f"\n| Impuestos: Q{compra.impuesto}")
    input("|===============[ REPORTE DE COMPRA ]===============|"
          "\n\n Presione una tecla para continuar...")


def buscar_compra(id: int):
    for compra in db_compras:
        if compra.id == id:
            return compra
    return None


def buscar_cliente(nit: str):
    for cliente in db_clientes:
        if cliente.nit.strip() == nit.strip():
            return cliente
    return None


def buscar_producto(code: str):
    for producto in db_productos:
        if producto.code.strip() == code.strip():
            return producto
    return None


def datos_estudiante():
    limpiar()
    input("|===============[ LABORATORIO IPC2 N ]===============|"
          "\n| Nombre: Derek Francisco Orellana Ibáñez"
          "\n| Carné: 202001151"
          "\n| Carrera: Ingeniería en Ciencias y Sistemas"
          "\n|===============[ LABORATORIO IPC2 N  ]===============|"
          "\n\nPresione una tecla para continuar...")


def limpiar():
    print("\033c", end="")


if __name__ == "__main__":
    main()
