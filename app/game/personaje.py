import random

class Personaje:
    def __init__(self):
        self.stats = self.crear_personaje_base()

    def crear_personaje_base(self):
        id_personaje = random.randint(10000, 99999)
        return {
            "id": id_personaje,
            "nombre": "Nombre_Personaje",
            "clase": "Clase_Personaje",
            "genero": "Genero_Personaje",
            "salud_maxima": 100,
            "salud_actual": 100,
            "ataque": 10,
            "defensa": 5,
            "magia": 5,
            "fuerza": 10,
            "destreza": 10,
            "constitucion": 10,
            "inteligencia": 10,
            "sabiduria": 10,
            "habilidad": 10,
            "carisma": 10
        }
