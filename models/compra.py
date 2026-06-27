from datetime import datetime

class Compra:

    def __init__(self,
                 compra_id=None,
                 proveedor_id=None,
                 fecha=None,
                 total=0,
                 observaciones=""):

        self.compra_id = compra_id
        self.proveedor_id = proveedor_id
        self.fecha = fecha if fecha else datetime.now()
        self.total = total
        self.observaciones = observaciones

    def __str__(self):

        return (f"{self.compra_id} | "
                f"Proveedor:{self.proveedor_id} | "
                f"${self.total}")