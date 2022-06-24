
def get_ip(texto):
    for linha in texto.readlines():
        if "IPv4" in linha:
            inicio = linha.find(":")
            ip = linha[inicio+2:-1]
            break
    return ip


# Esssa funcao retorna o endereco de ip do computador
if __name__ == '__main__':
    print(get_ip())
