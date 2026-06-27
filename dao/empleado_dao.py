
from databases.conexion import Conexion
from models.empleado import Empleado


class EmpleadoDAO:

    ###############################################
    # REGISTRAR EMPLEADO
    ###############################################

    def registrar(self, empleado):

        conexion = Conexion.obtener_conexion()
        cursor = conexion.cursor()

        sql = """
            INSERT INTO empleados
            (
                nombre,
                apellido_paterno,
                apellido_materno,
                puesto,
                numero_empleado,
                correo
            )

            VALUES
            (%s,%s,%s,%s,%s,%s)
        """

        valores = (

            empleado.nombre,
            empleado.apellido_paterno,
            empleado.apellido_materno,
            empleado.puesto,
            empleado.numero_empleado,
            empleado.correo

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()
        conexion.close()

        print("Empleado registrado correctamente.")

    ###############################################
    # LISTAR EMPLEADOS
    ###############################################

    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        cursor.execute("""

            SELECT *

            FROM empleados

            ORDER BY empleado_id

        """)

        registros = cursor.fetchall()

        empleados = []

        for fila in registros:

            empleado = Empleado(

                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6]

            )

            empleados.append(empleado)

        cursor.close()

        conexion.close()

        return empleados

    ###############################################
    # BUSCAR EMPLEADO
    ###############################################

    def buscar_por_id(self, empleado_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

            SELECT *

            FROM empleados

            WHERE empleado_id=%s

        """

        cursor.execute(sql, (empleado_id,))

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila:

            return Empleado(

                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6]

            )

        return None

    ###############################################
    # ACTUALIZAR EMPLEADO
    ###############################################

    def actualizar(self, empleado):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

            UPDATE empleados

            SET

                nombre=%s,

                apellido_paterno=%s,

                apellido_materno=%s,

                puesto=%s,

                numero_empleado=%s,

                correo=%s

            WHERE empleado_id=%s

        """

        valores = (

            empleado.nombre,

            empleado.apellido_paterno,

            empleado.apellido_materno,

            empleado.puesto,

            empleado.numero_empleado,

            empleado.correo,

            empleado.empleado_id

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Empleado actualizado correctamente.")

    ###############################################
    # ELIMINAR EMPLEADO
    ###############################################

    def eliminar(self, empleado_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

            DELETE FROM empleados

            WHERE empleado_id=%s

        """

        cursor.execute(sql, (empleado_id,))

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Empleado eliminado.")
