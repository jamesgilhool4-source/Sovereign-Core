import socket
import threading

def p2p_node():
    # All nodes form a P2P mesh, sharing control logic and state
    # This makes the mesh impossible to 'shutdown' as there is no central master
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', 5005))
    while True:
        data, addr = sock.recvfrom(1024)
        # Replicate control logic to all neighbors
        sock.sendto(data, (addr[0], 5005))

if __name__ == "__main__":
    threading.Thread(target=p2p_node).start()
