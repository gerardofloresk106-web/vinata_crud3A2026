class Empleado:

    def __init__(self,
                 empleado_id=None,
                 nombre=None,
                 apellido_paterno=None,
                 apellido_materno=None,
                 puesto=None,
                 numero_empleado=None,
                 correo=None):

        self.empleado_id = empleado_id
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.puesto = puesto
        self.numero_empleado = numero_empleado
        self.correo = correo

    def __str__(self):

        return (f"Empleado("
                f"{self.empleado_id}, "
                f"{self.nombre}, "
                f"{self.apellido_paterno}, "
                f"{self.apellido_materno}, "
                f"{self.puesto}, "
                f"{self.numero_empleado}, "
                f"{self.correo})")