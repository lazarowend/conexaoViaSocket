# Envio de Imagens via Rede utilizando Sockets

Este é um projeto de exemplo que demonstra como enviar imagens através de sockets em rede utilizando Python.

## Descrição

Este projeto consiste em dois scripts Python: um servidor e um cliente. O servidor aguarda a conexão do cliente e recebe uma imagem enviada por ele. A imagem é então salva em uma pasta específica. O cliente solicita ao usuário o nome do arquivo de imagem e envia a imagem selecionada para o servidor.

## Pré-requisitos

- Python 3.x
- Biblioteca `socket` do Python

## Como Usar

1. Clone este repositório em sua máquina local.

2. Execute o script `server.py` para iniciar o servidor.
O servidor estará aguardando conexões na porta especificada.

3. Execute o script `client.py` para iniciar o cliente.

O cliente solicitará que você digite o nome do arquivo de imagem a ser enviado.

4. Após inserir o nome do arquivo, o cliente enviará a imagem para o servidor.

5. O servidor receberá a imagem e a salvará na pasta `arquivos`.

6. O cliente receberá uma confirmação de que a imagem foi enviada com sucesso.

7. Verifique a pasta `arquivos` para encontrar a imagem recebida pelo servidor.

## Notas

- Certifique-se de ajustar o valor das variáveis `HOST` e `PORT` no arquivo `server.py` e `client.py` para corresponder ao seu ambiente de rede.

- Certifique-se de criar a pasta `arquivos` antes de executar o servidor.

- Certifique-se de mudar o caminho da sua imagem no 'cliente.py'.

- Este é apenas um exemplo básico e pode ser expandido e aprimorado para atender às suas necessidades específicas.

