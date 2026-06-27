from databases.conexion import Conexion
from models.proveedor import Proveedor


class ProveedorDAO:

    def registrar(self, proveedor):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO proveedores(

            nombre,

            contacto,

            telefono,

            correo,

            direccion

        )

        VALUES(%s,%s,%s,%s,%s)

        """

        valores = (

            proveedor.nombre,

            proveedor.contacto,

            proveedor.telefono,

            proveedor.correo,

            proveedor.direccion

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Proveedor registrado correctamente.")
    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""

            SELECT *

            FROM proveedores

            ORDER BY proveedor_id

        """)

        registros = cursor.fetchall()

        proveedores = []

        for fila in registros:

            proveedor = Proveedor(

                fila[0],

                fila[1],

                fila[2],

                fila[3],

                fila[4],

                fila[5]

            )

            proveedores.append(proveedor)

        cursor.close()

        conexion.close()

        return proveedores

    def buscar_por_id(self, proveedor_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM proveedores

        WHERE proveedor_id=%s

        """, (proveedor_id,))

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila:

            return Proveedor(

                fila[0],

                fila[1],

                fila[2],

                fila[3],

                fila[4],

                fila[5]

            )

        return None

    def actualizar(self, proveedor):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        UPDATE proveedores

        SET

            nombre=%s,

            contacto=%s,

            telefono=%s,

            correo=%s,

            direccion=%s

        WHERE proveedor_id=%s

        """

        valores = (

            proveedor.nombre,

            proveedor.contacto,

            proveedor.telefono,

            proveedor.correo,

            proveedor.direccion,

            proveedor.proveedor_id

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Proveedor actualizado.")

    def eliminar(self, proveedor_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""

        DELETE FROM proveedores

        WHERE proveedor_id=%s

        """, (proveedor_id,))

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Proveedor eliminado.")
    