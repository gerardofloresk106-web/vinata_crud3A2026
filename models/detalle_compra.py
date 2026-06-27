class DetalleCompra:

    def __init__(self,
                 detalle_id=None,
                 compra_id=None,
                 producto_id=None,
                 cantidad=0,
                 precio_compra=0,
                 subtotal=0):

        self.detalle_id = detalle_id
        self.compra_id = compra_id
        self.producto_id = producto_id
        self.cantidad = cantidad
        self.precio_compra = precio_compra
        self.subtotal = subtotal

    def __str__(self):

        return (f"{self.producto_id} "
                f"x {self.cantidad}")