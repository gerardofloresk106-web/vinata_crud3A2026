class Producto:

    def __init__(self,
                 producto_id=None,
                 nombre=None,
                 categoria=None,
                 marca=None,
                 codigo_barras=None,
                 precio_compra=None,
                 precio_venta=None,
                 stock=None,
                 stock_minimo=None,
                 unidad_medida=None,
                 fecha_caducidad=None,
                 disponible=True):

        self.producto_id = producto_id
        self.nombre = nombre
        self.categoria = categoria
        self.marca = marca
        self.codigo_barras = codigo_barras
        self.precio_compra = precio_compra
        self.precio_venta = precio_venta
        self.stock = stock
        self.stock_minimo = stock_minimo
        self.unidad_medida = unidad_medida
        self.fecha_caducidad = fecha_caducidad
        self.disponible = disponible

    def __str__(self):

        return (
            f"{self.producto_id} | "
            f"{self.nombre} | "
            f"{self.categoria} | "
            f"{self.marca} | "
            f"${self.precio_venta} | "
            f"Stock:{self.stock}"
        )