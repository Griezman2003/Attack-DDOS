import threading
from bot1 import launch_attack1 as bot1_attack
from bot2 import launch_attack2 as bot2_attack
from bot3 import launch_attack3 as bot3_attack
from bot4 import launch_attack4 as bot4_attack
from bot5 import launch_attack5 as bot5_attack
from bot6 import launch_attack6 as bot6_attack
from bot7 import launch_attack7 as bot7_attack
from bot8 import launch_attack8 as bot8_attack
from bot9 import launch_attack9 as bot9_attack
from bot10 import launch_attack10 as bot10_attack
from escaner import puertoScan


# Definir la variable global para bloquear/desbloquear el inicio del ataque
start_event = threading.Event()

def print_menu():
    print("Seleccione qué bots iniciar:")
    print("1. Escanear")
    print("2. Bot2")
    print("3. Bot3")
    print("4. Iniciar todos")

def main():
    print("INICIE EL ATAQUE DDOS")
    while True:
        print_menu()
        choice = input("Ingrese el número de la opción (q para salir): ")

        if choice == 'q':
            break
        elif choice == '4':
            start_event.set()  # Desbloquear la señal de inicio para todos los bots
            bot_functions = [bot1_attack, bot2_attack,bot3_attack,bot4_attack,bot5_attack,
                             bot6_attack,bot7_attack,bot8_attack,bot9_attack,bot10_attack]
            for i, bot_func in enumerate(bot_functions, start=1):
                threading.Thread(target=bot_func, args=(f"Bot{i}", start_event)).start()
                print(f"Iniciando Bot{i}...")
            break
        elif choice == '1':
            scan_name = "escaneo"
            start_event.set()
            threading.Thread(target=puertoScan, args=(start_event, scan_name)).start()
            print(f"Iniciando {scan_name}...")
        elif choice == '2':
            bot_name = "Bot2"
            start_event.set()
            threading.Thread(target=bot2_attack, args=(bot_name, start_event)).start()
            print(f"Iniciando {bot_name}...")
            break
        elif choice == '3':
            bot_name = "Bot3"
            start_event.set()
            threading.Thread(target=bot3_attack, args=(bot_name, start_event)).start()
            print(f"Iniciando {bot_name}...")
            break
        else:
            print("Opción no válida. Por favor, ingrese un número del 1 al 3.")
            

if __name__ == "__main__":
    main()
