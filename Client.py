import socket

# Creates a TCP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects the socket to the server IP address and port 5000/ port of your choice
server_address = ("YOUR IP ADDRESS HERE", 5000)
print('Connecting to %s port %s' % server_address)
sock.connect(server_address)

try:
    while True:
        try:
            # Receives the message from the server
            received_message = sock.recv(2048)
            print(f"Message received: {received_message}")
        except ConnectionResetError:
            print("Server closed the connection")
            break

except KeyboardInterrupt:
    print("Closing socket.")
    sock.close()
