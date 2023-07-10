import socket

HOST = 'localhost'
PORT = 8001

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # fazendo a conexão com o server
sock.connect((HOST, PORT))
sock.send(input('digite o nome do arquivo: ').encode(encoding="utf-8"))

    # caminho arquivo 
arquivo = open('teste.jpg', 'rb')
sock.send(arquivo.read())

confirmacao = sock.recv(1024)
if confirmacao == b'ok':
    print('imagem enviada')
