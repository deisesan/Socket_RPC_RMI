# Server Side Chat Room
import socket, threading

# Defina constants 
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

# Criar um socket servidor 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Criar duas listas em branco para armazenar clientes conectados via socket e seus nomes
client_socket_list = []
client_name_list = []

def broadcast_message(message):
    '''Enviando uma mensagem para todos os clientes conectados no servidor'''
    pass

def receive_message(client_socket):
    '''Recebendo uma mensagem de um client especifico e encaminhando a mensagem a ser transmitida'''
    pass

def connect_client():
    '''Conectando um cliente no servidor'''
    pass