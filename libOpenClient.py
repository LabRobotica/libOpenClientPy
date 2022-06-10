import socket

socketClient = 0

def iniciar_conexao(ipServidor,portaServidor):
    # Criando um socket TCP/IP
    global socketClient
    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#, socket.SOCK_NONBLOCK)
    # Conectando ao servidor
    print('Tentando conectar a ' + ipServidor + 'através da porta' + str(portaServidor))
    socketClient.connect((ipServidor,portaServidor))
    socketClient.setblocking(0)
    return 0 #Bem sucedido

def finaliza_conexao():
    global socketClient
    print('Fechando socket')
    socketClient.close()
    return 0

def envia_mensagem(msg):
    global socketClient
    socketClient.sendall(str.encode(msg))
    return 0

def recebe_mensagem(tamanho):
    global socketClient
    mensagemRecebida = socketClient.recv(tamanho)
    return mensagemRecebida.decode('UTF-8')

#####EXEMPLO
#iniciar_conexao('localhost',54000)
#envia_mensagem('lc')
#recebe_mensagem(60)
#finaliza_conexao()