class Proveedor:

    def __init__(self,
                 proveedor_id=None,
                 nombre=None,
                 contacto=None,
                 telefono=None,
                 correo=None,
                 direccion=None):

        self.proveedor_id = proveedor_id
        self.nombre = nombre
        self.contacto = contacto
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):

        return (
            f"{self.proveedor_id} | "
            f"{self.nombre} | "
            f"{self.contacto} | "
            f"{self.telefono}"
        )