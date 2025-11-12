# Client Side Chat Room
import socket, threading

# Define a constants 
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345 
ENCODER = "utf-8"
BYTESIZE = 1024

# Cria um socket client 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

def send_message():
    "Enviando a mensagem para o servidor para ser encaminhada"
    pass

def receive_message():
    '''Recebe uma mensagem enviada do servidor'''
    pass