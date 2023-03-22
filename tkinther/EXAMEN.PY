import random
from datetime import datetime

class MatriculaGenerator:
    def __init__(self, nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera):
        self.nombre = nombre
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.ano_nacimiento = ano_nacimiento
        self.carrera = carrera

    def generar_matricula(self):
        # Obtener el año actual
        ano_actual = datetime.now().year % 100

        # Obtener los primeros dos dígitos del año actual
        digitos_ano_actual = str(ano_actual).zfill(2)

        # Obtener los últimos dos dígitos del año de nacimiento
        digitos_ano_nacimiento = str(self.ano_nacimiento)[-2:]

        # Obtener la primera letra del nombre y de cada apellido
        letra_nombre = self.nombre[0]
        letra_apellido_paterno = self.apellido_paterno[0]
        letra_apellido_materno = self.apellido_materno[0]

        # Generar tres dígitos aleatorios
        digitos_aleatorios = str(random.randint(100, 999))

        # Obtener las tres primeras letras de la carrera
        letras_carrera = self.carrera[:3].upper()

        # Concatenar todos los componentes para generar la matrícula
        matricula = digitos_ano_actual + digitos_ano_nacimiento + letra_nombre + letra_apellido_paterno + letra_apellido_materno + digitos_aleatorios + letras_carrera

        return matricula

# Ejemplo de uso
nombre = input("Ingrese el nombre: ")
apellido_paterno = input("Ingrese el apellido paterno: ")
apellido_materno = input("Ingrese el apellido materno: ")
ano_nacimiento = int(input("Ingrese el año de nacimiento: "))
carrera = input("Ingrese la carrera: ")

generator = MatriculaGenerator(nombre, apellido_paterno, apellido_materno, ano_nacimiento, carrera)
matricula = generator.generar_matricula()

mensaje = f"La matrícula generada es: {matricula}"
print(mensaje)