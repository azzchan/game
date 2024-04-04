import os
from app.game.partidas import GestorPartidas

class Menu:
    @staticmethod
    def mostrar_menu():
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Crear nueva partida")
        print("2. Seleccionar partida")
        print("3. Salir")
        opcion = input("Ingrese una opción: ")
        return opcion

    @staticmethod
    def limpiar_pantalla():
        os.system('cls' if os.name == 'nt' else 'clear')

    @staticmethod
    def mostrar_menu():
        return ["Crear nueva partida", "Seleccionar partida", "Salir"]