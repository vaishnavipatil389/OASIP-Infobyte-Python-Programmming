import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                break
            print(f"Received from {address}: {message}")
           
            for client in clients:
                if client != client_socket:
                    client.send(message.encode('utf-8'))
        except:
            break
    
    client_socket.close()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 12345))
server.listen(5)

print("Server is listening...")

clients = []

while True:
    client_socket, address = server.accept()
    print(f"Accepted connection from {address}")
    
    clients.append(client_socket)
    
   
    client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
    client_thread.start()
