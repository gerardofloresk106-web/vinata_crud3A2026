from databases.conexion import Conexion

from models.venta import Venta

from models.detalle_venta import DetalleVenta

class VentaDAO:

    def registrar_venta(self, venta):

        conexion = Conexion.obtener_conexion()

        cursor = conexion.cursor()

        sql = """

        INSERT INTO ventas(

            usuario_id,

            fecha,

            subtotal,

            descuento,

            total,

            metodo_pago,

            estado

        )

        VALUES(%s,%s,%s,%s,%s,%s,%s)

        RETURNING venta_id

        """

        valores=(

            venta.usuario_id,

            venta.fecha,

            venta.subtotal,

            venta.descuento,

            venta.total,

            venta.metodo_pago,

            venta.estado

        )

        cursor.execute(sql,valores)

        venta_id=cursor.fetchone()[0]

        conexion.commit()

        cursor.close()

        conexion.close()

        return venta_id

    def registrar_detalle(self, detalle):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        sql="""

        INSERT INTO detalle_venta(

            venta_id,

            producto_id,

            cantidad,

            precio,

            subtotal

        )

        VALUES(%s,%s,%s,%s,%s)

        """

        valores=(

            detalle.venta_id,

            detalle.producto_id,

            detalle.cantidad,

            detalle.precio,

            detalle.subtotal

        )

        cursor.execute(sql,valores)

        conexion.commit()

        cursor.close()

        conexion.close()

    def descontar_stock(self,
                        producto_id,
                        cantidad):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        sql="""

        UPDATE productos

        SET stock=stock-%s

        WHERE producto_id=%s

        """

        cursor.execute(sql,
                       (cantidad,
                        producto_id))

        conexion.commit()

        cursor.close()

        conexion.close()

    def cancelar_venta(self,
                       venta_id):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        UPDATE ventas

        SET estado='CANCELADA'

        WHERE venta_id=%s

        """,(venta_id,))

        conexion.commit()

        cursor.close()

        conexion.close()

    def obtener_ventas(self):

        conexion=Conexion.obtener_conexion()

        cursor=conexion.cursor()

        cursor.execute("""

        SELECT *

        FROM ventas

        ORDER BY venta_id DESC

        """)

        registros=cursor.fetchall()

        cursor.close()

        conexion.close()

        return registros
