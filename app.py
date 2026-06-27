import os
import sys
run_path = os.path.dirname(os.path.abspath(__file__))
sys.path.append(run_path)

from dao.usuario_dao import UsuarioDAO
from dao.empleado_dao import EmpleadoDAO
from dao.producto_dao import ProductoDAO
from dao.proveedor_dao import ProveedorDAO
from dao.compra_dao import CompraDAO
from dao.venta_dao import VentaDAO

from models.usuario import Usuario
from models.empleado import Empleado
from models.producto import Producto
from models.proveedor import Proveedor

import os

os.system("cls")

usuarioDAO = UsuarioDAO()
empleadoDAO = EmpleadoDAO()
productoDAO = ProductoDAO()
proveedorDAO = ProveedorDAO()
compraDAO = CompraDAO()
ventaDAO = VentaDAO()

def menu():

    while True:

        print("\n")

        print("="*60)
        print("        SISTEMA VINATA")
        print("="*60)

        print("1. Login")
        print("2. Usuarios")
        print("3. Empleados")
        print("4. Productos")
        print("5. Proveedores")
        print("6. Compras")
        print("7. Ventas")
        print("8. Reportes")
        print("9. Salir")

        opcion = input("\nSeleccione una opción: ")

        if opcion=="1":
            login()

        elif opcion=="2":
            menu_usuarios()

        elif opcion=="3":
            menu_empleados()

        elif opcion=="4":
            menu_productos()

        elif opcion=="5":
            menu_proveedores()

        elif opcion=="6":
            print("Módulo Compras en construcción")

        elif opcion=="7":
            print("Módulo Ventas en construcción")

        elif opcion=="8":
            print("Módulo Reportes en construcción")

        elif opcion=="9":

            print("\nGracias por usar VINATA")

            break

        else:

            print("Opción incorrecta.")

def login():

    print("\nLOGIN")

    correo = input("Correo: ")

    password = input("Contraseña: ")

    usuario = usuarioDAO.login(correo,password)

    if usuario:

        print("\nBienvenido",usuario.nombre)

        print("Rol:",usuario.rol)

    else:

        print("Usuario incorrecto.")

def menu_usuarios():

    while True:

        print("\n")

        print("===== USUARIOS =====")

        print("1 Registrar")

        print("2 Mostrar")

        print("3 Regresar")

        opcion=input("Seleccione: ")

        if opcion=="1":

            nombre=input("Nombre: ")

            correo=input("Correo: ")

            password=input("Contraseña: ")

            rol=input("Rol: ")

            usuario=Usuario(

                None,

                nombre,

                correo,

                password,

                rol

            )

            usuarioDAO.registrar(usuario)

        elif opcion=="2":

            usuarios=usuarioDAO.obtener_todos()

            for u in usuarios:

                print(u)

        elif opcion=="3":

            break
def menu_productos():

    while True:

        print("\n===== PRODUCTOS =====")

        print("1 Registrar")

        print("2 Mostrar")

        print("3 Regresar")

        opcion=input("Seleccione: ")

        if opcion=="1":

            nombre=input("Nombre: ")

            categoria=input("Categoría: ")

            marca=input("Marca: ")

            codigo=input("Código Barras: ")

            compra=float(input("Precio Compra: "))

            venta=float(input("Precio Venta: "))

            stock=int(input("Stock: "))

            minimo=int(input("Stock mínimo: "))

            unidad=input("Unidad: ")

            fecha=input("Caducidad (AAAA-MM-DD): ")

            producto=Producto(

                None,

                nombre,

                categoria,

                marca,

                codigo,

                compra,

                venta,

                stock,

                minimo,

                unidad,

                fecha,

                True

            )

            productoDAO.registrar(producto)

        elif opcion=="2":

            productos=productoDAO.obtener_todos()

            for p in productos:

                print(p)

        elif opcion=="3":

            break
if __name__=="__main__":

    menu()