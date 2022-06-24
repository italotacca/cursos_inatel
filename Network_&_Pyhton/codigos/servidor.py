# Bate-papo com socket - Servidor
from socket import *
from funcoes import get_ip
import threading
import os

ipconfig = os.popen('ipconfig')
ip = get_ip(ipconfig)
print("O IP do servidor é: " + ip)

servidor = socket(AF_INET, SOCK_STREAM)
servidor.bind((ip, 1234))
servidor.listen(1)

cliente, endereco = servidor.accept()
print(f"{endereco} esta online.")

while True:
    dados = cliente.recv(2048).decode()
    print(f"O cliente diz: {dados}")
    if dados == "sair":
        cliente.close()
        break
    mensagem = input("Digite uma mensagem: ")
    cliente.sendall(mensagem.encode())

servidor.close()