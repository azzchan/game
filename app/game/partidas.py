import json
import os

class GestorPartidas:
    MAX_PARTIDAS = 3
    CARPETA_PARTIDAS = "partidas"
    
    def __init__(self):
        self.partidas = self.listar_partidas()

    def crear_partida(self):
        if len(self.partidas) >= self.MAX_PARTIDAS:
            print("Ya has alcanzado el máximo de partidas.")
            return

        nombre_partida = input("Ingrese el nombre para la nueva partida: ")
        archivo_json = nombre_partida + ".json"
        ruta_archivo = os.path.join(self.CARPETA_PARTIDAS, archivo_json)
        
        if archivo_json in self.partidas:
            respuesta = input("Ya existe una partida con este nombre. ¿Desea sobrescribirla? (s/n): ").lower()
            if respuesta != "s":
                print("No se sobrescribió la partida.")
                self.menu_principal()
                return

        datos_partida = self.crear_personaje_base()
        self.partidas[archivo_json] = datos_partida
        

        if not os.path.exists(self.CARPETA_PARTIDAS):
            os.makedirs(self.CARPETA_PARTIDAS)
        if not os.path.exists(ruta_archivo):
            with open(ruta_archivo, "w") as file:
                json.dump(datos_partida, file, indent=4)
        # os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Partida '{nombre_partida}' creada.")
        self.menu_principal()

    def seleccionar_partida(self):
        if not self.partidas:
            print("No hay partidas disponibles.")
            self.menu_principal()
            return
        while True:
            print("Partidas disponibles:")
            for i, partida in enumerate(self.partidas.keys(), 1):
                print(f"{i}. {partida[:-5]}")  # Eliminar la extensión ".json"
            print(f"{len(self.partidas) + 1}. Volver al menú principal")

            seleccion = input("Seleccione el número de la partida una partida: ")
            try:
                seleccion = int(seleccion)
                if seleccion == len(self.partidas) + 1:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    return
                elif seleccion <= 0 or seleccion > len(self.partidas):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Selección inválida.")
                else:
                    nombre_partida = list(self.partidas.keys())[seleccion - 1]
                    print(f"Cargando partida '{nombre_partida[:-5]}'...")  # Eliminar la extensión ".json"
                    with open(os.path.join(self.CARPETA_PARTIDAS, nombre_partida), "r") as file:
                        return json.load(file)
            except ValueError:
                # os.system('cls' if os.name == 'nt' else 'clear')
                print("Debe ingresar un número válido.")

    def listar_partidas(self):
        partidas = {}
        if not os.path.exists(self.CARPETA_PARTIDAS):
            os.makedirs(self.CARPETA_PARTIDAS)
        for archivo_json in os.listdir(self.CARPETA_PARTIDAS):
            if archivo_json.endswith(".json"):
                with open(os.path.join(self.CARPETA_PARTIDAS, archivo_json), "r") as file:
                    partidas[archivo_json] = json.load(file)
        return partidas
