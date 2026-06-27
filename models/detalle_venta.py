class DetalleVenta:

    def __init__(self,
                 detalle_id=None,
                 venta_id=None,
                 producto_id=None,
                 cantidad=0,
                 precio=0,
                 subtotal=0):

        self.detalle_id = detalle_id
        self.venta_id = venta_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio = precio
        self.subtotal = subtotal

    def __str__(self):

        return (f"{self.producto_id} "
                f"x {self.cantidad}")