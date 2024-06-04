import nmap
import socket

def puertoScan(host, start_port, end_port):
    # Eliminar el esquema y cualquier barra final si están presentes
    if host.startswith("http://"):
        host = host[7:]
    elif host.startswith("https://"):
        host = host[8:]
    if host.endswith("/"):
        host = host[:-1]
    
    try:
        # Resolver el nombre de host a una dirección IP
        host_ip = socket.gethostbyname(host)
    except socket.error as err:
        print(f"Error al resolver el host: {err}")
        return
    
    nm = nmap.PortScanner()
    print(f"Iniciando escaneo de {host} ({host_ip}) desde el puerto {start_port} hasta {end_port}...")
    
    try:
        nm.scan(hosts=host_ip, ports=f'{start_port}-{end_port}', arguments='--host-timeout 60s')  # Establecer un timeout de 60 segundos
    except nmap.PortScannerTimeout:
        print("El escaneo se ha agotado el tiempo.")
        return
    except nmap.PortScannerError as e:
        print(f"Error en el escaneo: {e}")
        return
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return
    
    open_ports = []
    try:
        for proto in nm[host_ip].all_protocols():
            lport = nm[host_ip][proto].keys()
            for port in lport:
                if nm[host_ip][proto][port]['state'] == 'open':
                    open_ports.append(port)
    except KeyError:
        print(f"No se pudo escanear el host {host}. Verifique la dirección y los puertos.")
        return
    
    if open_ports:
        print(f"Puertos abiertos: {open_ports}")
    else:
        print("No se encontraron puertos abiertos.")

