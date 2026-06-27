from databases.conexion import Conexion
from models.producto import Producto


class ProductoDAO:

    def registrar(self, producto):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO productos(

            nombre,

            categoria,

            marca,

            codigo_barras,

            precio_compra,

            precio_venta,

            stock,

            stock_minimo,

            unidad_medida,

            fecha_caducidad,

            disponible

        )

        VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)

        """

        valores=(

            producto.nombre,

            producto.categoria,

            producto.marca,

            producto.codigo_barras,

            producto.precio_compra,

            producto.precio_venta,

            producto.stock,

            producto.stock_minimo,

            producto.unidad_medida,

            producto.fecha_caducidad,

            producto.disponible

        )

        cursor.execute(sql,valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Producto registrado correctamente.")

    def obtener_todos(self):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

            SELECT *

            FROM productos

            ORDER BY producto_id

        """)

        registros=cursor.fetchall()

        productos=[]

        for fila in registros:

            productos.append(

                Producto(

                    fila[0],
                    fila[1],
                    fila[2],
                    fila[3],
                    fila[4],
                    fila[5],
                    fila[6],
                    fila[7],
                    fila[8],
                    fila[9],
                    fila[10],
                    fila[11]

                )

            )

        cursor.close()

        conexion.close()

        return productos

    def buscar_por_id(self,id_producto):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM productos

        WHERE producto_id=%s

        """,(id_producto,))

        fila=cursor.fetchone()

        cursor.close()

        conexion.close()

        if fila:

            return Producto(

                fila[0],
                fila[1],
                fila[2],
                fila[3],
                fila[4],
                fila[5],
                fila[6],
                fila[7],
                fila[8],
                fila[9],
                fila[10],
                fila[11]

            )

        return None

    def eliminar(self,id_producto):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

            DELETE FROM productos

            WHERE producto_id=%s

        """,(id_producto,))

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Producto eliminado.")

    def actualizar(self,producto):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        sql="""

        UPDATE productos

        SET

            nombre=%s,

            categoria=%s,

            marca=%s,

            codigo_barras=%s,

            precio_compra=%s,

            precio_venta=%s,

            stock=%s,

            stock_minimo=%s,

            unidad_medida=%s,

            fecha_caducidad=%s,

            disponible=%s

        WHERE producto_id=%s

        """

        valores=(

            producto.nombre,

            producto.categoria,

            producto.marca,

            producto.codigo_barras,

            producto.precio_compra,

            producto.precio_venta,

            producto.stock,

            producto.stock_minimo,

            producto.unidad_medida,

            producto.fecha_caducidad,

            producto.disponible,

            producto.producto_id

        )

        cursor.execute(sql,valores)

        conexion.commit()

        cursor.close()

        conexion.close()

        print("Producto actualizado.")

    def inventario_bajo(self):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM productos

        WHERE stock<=stock_minimo

        """)

        registros=cursor.fetchall()

        cursor.close()

        conexion.close()

        return registros

    def buscar_codigo(self,codigo):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM productos

        WHERE codigo_barras=%s

        """,(codigo,))

        fila=cursor.fetchone()

        cursor.close()

        conexion.close()

        return fila
