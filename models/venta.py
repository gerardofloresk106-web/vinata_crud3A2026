from datetime import datetime

class Venta:

    def __init__(self,
                 venta_id=None,
                 usuario_id=None,
                 fecha=None,
                 subtotal=0,
                 descuento=0,
                 total=0,
                 metodo_pago="EFECTIVO",
                 estado="ACTIVA"):

        self.venta_id = venta_id
        self.usuario_id = usuario_id
        self.fecha = fecha if fecha else datetime.now()
        self.subtotal = subtotal
        self.descuento = descuento
        self.total = total
        self.metodo_pago = metodo_pago
        self.estado = estado

    def __str__(self):

        return (f"Venta #{self.venta_id} "
                f"Total: ${self.total}")