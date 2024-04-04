from personaje import Personaje
from partidas import GestorPartidas
from menu import Menu

def main():
    personaje = Personaje()
    gestor_partidas = GestorPartidas()

    while True:
        
        opcion = Menu.mostrar_menu()
        Menu.limpiar_pantalla()

        if opcion == "1":
            gestor_partidas.crear_partida()
        elif opcion == "2":
            gestor_partidas.seleccionar_partida()
        elif opcion == "3":
            print("")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

if __name__ == "__main__":
    main()
