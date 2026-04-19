import socket, ssl
# The Hub: Receives connections from the implants
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 443))
server.listen(5)
print("LISTENING_FOR_IRL_IMPLANTS")
