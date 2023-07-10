import socket

HOST = 'localhost'
PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(5)

while True:
    print('Servidor rodando!')
    novo_sock, _ = sock.accept()

    # recebendo o nome do arquivo para salvar na pasta
    nome_arquivo = novo_sock.recv(1024).decode()
    # recebendo a imagem
    novo_arquivo = novo_sock.recv(1000000000)

    with open(f'arquivos/{nome_arquivo}.png', 'wb') as arq:
        arq.write(novo_arquivo)

    novo_sock.send(b'ok')