import socket, struct
sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_RAW)
packet = b'\x00' * 19 + b'\x04' + struct.pack("!H", 65001)
sock.sendto(packet, ("10.0.0.1", 0))
