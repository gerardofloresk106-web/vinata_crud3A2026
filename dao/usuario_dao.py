from databases.conexion import Conexion
from models.usuario import Usuario


class UsuarioDAO:

    #########################################
    # REGISTRAR USUARIO
    #########################################

    def registrar(self, usuario):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """
            INSERT INTO usuarios
            (nombre,correo,password,rol)

            VALUES
            (%s,%s,%s,%s)
        """

        valores = (
            usuario.nombre,
            usuario.correo,
            usuario.password,
            usuario.rol
        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Usuario registrado correctamente.")

    #########################################
    # LISTAR USUARIOS
    #########################################

    def obtener_todos(self):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """
            SELECT *
            FROM usuarios
            ORDER BY usuario_id
        """

        cursor.execute(sql)

        registros = cursor.fetchall()

        usuarios = []

        for fila in registros:

            usuario = Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4]
            )

            usuarios.append(usuario)

        cursor.close()

        conexion.close()

        return usuarios
    
    #########################################
    # BUSCAR USUARIO
    #########################################

    def buscar_por_id(self, usuario_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """
            SELECT *
            FROM usuarios
            WHERE usuario_id=%s
        """

        cursor.execute(sql, (usuario_id,))

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila:

            return Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4]
            )

        return None

    #########################################
    # ACTUALIZAR
    #########################################

    def actualizar(self, usuario):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """
            UPDATE usuarios

            SET
                nombre=%s,
                correo=%s,
                password=%s,
                rol=%s

            WHERE usuario_id=%s
        """

        valores = (

            usuario.nombre,

            usuario.correo,

            usuario.password,

            usuario.rol,

            usuario.usuario_id

        )

        cursor.execute(sql, valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Usuario actualizado correctamente.")

    #########################################
    # ELIMINAR
    #########################################

    def eliminar(self, usuario_id):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """
            DELETE FROM usuarios
            WHERE usuario_id=%s
        """

        cursor.execute(sql, (usuario_id,))

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Usuario eliminado.")

    #########################################
    # LOGIN
    #########################################

    def login(self, correo, password):

        conexion = Conexion.obtener_conexion()
        if conexion is None:
            print("Error: No se pudo establecer la conexión a la base de datos.")
            return None

        cursor = conexion.cursor()

        sql = """
            SELECT *
            FROM usuarios

            WHERE correo=%s
            AND password=%s
        """

        cursor.execute(sql, (correo, password))

        fila = cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila:

            return Usuario(
                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4]
            )

        return None
