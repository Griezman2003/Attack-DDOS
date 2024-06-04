import nmap
import threading
def puertoScan (start_event,target_url ):
    if start_event.is_set():
        print("Escaneando puerto")
    try:
        nm = nmap.PortScanner() ## Aqui simplemente iniciamos a escanear el puerto, (PortScanner es de la libreria nmappara escanear puertos)
        nm.scan(target_url, arguments='-p-')
        
        for host in nm.all_hosts():  ## (all_host) metodo de la libreria nmap para iterar por todos los resultados del scaneo)
            print("Resultados del escaneo para: {host}")
            for protocolo in nm[host].all_protocols():
                print("El protocolo es: {protocolo}")
                puertos = nm[host][protocolo].keys()
                for puerto in puertos:
                    print(f"Puerto: {puerto}, Estado: {nm[host][protocolo][puerto]['estado']}")     
    except nmap.PortScannerError as e:
            print(f"Error al escanear con Nmap:", e)
    else:
        print(f"Señal de inicio no activada. Esperando instrucciones...")

if __name__ == "__main__":
    start_event = threading.Event()
    start_event.set()
    target_url = "https://utecan.edu.mx/"
    if start_event.is_set():
        puertoScan(start_event,target_url)
            
