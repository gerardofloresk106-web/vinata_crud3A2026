class Usuario:

    def __init__(self,
                 usuario_id=None,
                 nombre=None,
                 correo=None,
                 password=None,
                 rol=None):

        self.usuario_id = usuario_id
        self.nombre = nombre
        self.correo = correo
        self.password = password
        self.rol = rol

    def __str__(self):
        return (f"Usuario("
                f"{self.usuario_id}, "
                f"{self.nombre}, "
                f"{self.correo}, "
                f"{self.rol})")