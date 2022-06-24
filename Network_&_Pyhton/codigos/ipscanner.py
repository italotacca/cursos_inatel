# Scanner de Rede /24

#importando os módulos necessários
from funcoes import get_ip
import threading
import os

# Declarando as listas dos hosts e de threads
hosts = []
threads = []

# Obtendo o endereco de IP do computador
configuracao = os.popen("ipconfig")
end_ip = get_ip(configuracao)

print("Escaneando a Rede /24:\n")

# Função que envia um ping para um IP e verifica se há um computador respondendo
def scanner(i,l):
    resposta = os.popen("ping " + end_ip[0:11] + f"{i} " + "-n 1").read()

    if "TTL" in resposta:
        with l:
            hosts.append(end_ip[0:11] + f"{i}") # Adiciona o IP dos PCs online em uma lista
            print(end_ip[0:11] + f"{i}" + " online") # Exibe na tela o endereço de IP dos PCs online

# Recurso lock de sincronização
lock = threading.Lock()

# Criando os threads e variando os IPs da rede /24
for i in range(1, 255):
    t = threading.Thread(target=scanner, args=(i,lock,))
    t.start()

# Loop para que o código espere os threads finalizarem antes de ir para as próximas instruções
for thread in threads:
    thread.join()

print("\nFim da execução, pressione qualquer tecla para sair.\n")
os.system("pause")


