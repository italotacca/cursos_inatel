# Bate-papo com socket - Cliente
from socket import *

ip_servidor = input("Digite o IP do servidor: ")

cliente = socket(AF_INET, SOCK_STREAM)
cliente.connect((ip_servidor, 1234))

while True:
    dados_enviar = input("Enviar ao servidor: ")
    cliente.sendall(dados_enviar.encode())

    if dados_enviar == "sair":
        cliente.close()
        break

    dados_recebidos = cliente.recv(2048).decode()
    print(f"O servidor diz: {dados_recebidos}")
    if dados_recebidos == "sair":
        cliente.sendall(dados_recebidos.encode())
        cliente.close()
        break