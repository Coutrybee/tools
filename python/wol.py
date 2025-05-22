import socket
import struct

def wake_on_lan(mac_address, broadcast_ip="192.168.1.255"):
    # Convierte la dirección MAC en bytes
    mac_bytes = bytes.fromhex(mac_address.replace(":", ""))
    
    # Crea el paquete mágico: 6 bytes de 0xFF seguidos de la MAC repetida 16 veces
    magic_packet = b'\xff' * 6 + mac_bytes * 16

    # Crea un socket UDP y envía el paquete al broadcast
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        sock.sendto(magic_packet, (broadcast_ip, 9))  # Puerto 9 es el estándar para WOL

