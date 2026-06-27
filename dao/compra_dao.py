from databases.conexion import Conexion

from models.compra import Compra

from models.detalle_compra import DetalleCompra

class CompraDAO:

    def registrar_compra(self, compra):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO compras(

            proveedor_id,

            fecha,

            total,

            observaciones

        )

        VALUES(%s,%s,%s,%s)

        RETURNING compra_id

        """

        valores=(

            compra.proveedor_id,

            compra.fecha,

            compra.total,

            compra.observaciones

        )

        cursor.execute(sql,valores)

        compra_id=cursor.fetchone()[0]

        conexion.commit()

        cursor.close()

        conexion.close()

        return compra_id
    def registrar_detalle(self, detalle):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO detalle_compra(

            compra_id,

            producto_id,

            cantidad,

            precio_compra,

            subtotal

        )

        VALUES(%s,%s,%s,%s,%s)

        """

        valores=(

            detalle.compra_id,

            detalle.producto_id,

            detalle.cantidad,

            detalle.precio_compra,

            detalle.subtotal

        )

        cursor.execute(sql,valores)

        conexion.commit()

        cursor.close()

        conexion.close()

    def actualizar_stock(self,
                         producto_id,
                         cantidad):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        sql="""

        UPDATE productos

        SET stock=stock+%s

        WHERE producto_id=%s

        """

        cursor.execute(sql,(cantidad,
                            producto_id))

        conexion.commit()

        cursor.close()

        conexion.close()

    def obtener_compras(self):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM compras

        ORDER BY compra_id DESC

        """)

        registros=cursor.fetchall()

        cursor.close()

        conexion.close()

        return registros
