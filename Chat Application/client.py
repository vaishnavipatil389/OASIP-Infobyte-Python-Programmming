import socket
import threading
# import server

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except:
            print("Connection closed.")
            break

def send_message(client_socket):
    while True:
        message = input()
        client_socket.send(message.encode('utf-8'))

server_address = ('localhost', 12345)

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(server_address)

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

send_thread = threading.Thread(target=send_message, args=(client_socket,))
send_thread.start()
