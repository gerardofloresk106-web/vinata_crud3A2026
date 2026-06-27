import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

class Conexion:
    
    @staticmethod
    def obtener_conexion():
        try:
            # Forzamos la conexión usando parámetros limpios decodificados
            conn = psycopg2.connect(
                host=os.getenv("DB_HOST"),
                database=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                port=os.getenv("DB_PORT")
            )
            # Línea clave: obliga a la conexión a comunicarse en UTF8 de forma segura
            conn.set_client_encoding('UTF8')
            return conn
        except Exception as e:
            print("\n❌ NO SE PUDO CONECTAR A POSTGRESQL ❌")
            # Convertimos el error a texto de forma segura sin importar los acentos de Windows
            error_seguro = repr(e)
            print(f"Detalle técnico: {error_seguro}")
            print("👉 Revisa que los datos de tu archivo .env coincidan exactamente con pgAdmin.")
            return None