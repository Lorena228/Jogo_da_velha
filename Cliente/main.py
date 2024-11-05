import socket as s

conn = s.socket(s.AF_INET, s.SOCK_STREAM)

opt = int(input('1- Nova conexão\n2- Segundo jogador '))

match opt:
  case 1:
    conn.connect(('localhost', 1234))
  case 2:
    porta = input('Qual porta deseja se conectar? (1235, 1236, 1237, 1238, 1239)')
    conn.connect(('localhost', int(porta)))
  case _:
    print('Conexão falhou! Tente novamente')

#Qual o nome do jogador?
msg = conn.recv(1024).decode()
msg = input(msg + '\n-->')
conn.sendall(msg.encode())

#iniciando o jogo
msg = conn.recv(1024).decode()
print(msg)

while True:
  #print do tabuleiro
  msg = conn.recv(1024).decode()
  print(msg)

  if msg.endswith('Empatou!') or msg.endswith(", você é o vencedor!"):
    break
  elif msg.endswith("Digite o número correspondente a posição que deseja marcar: "):
    # Digite o número correspondente a posição que deseja marcar:
    msg = input('\n-->')
    conn.sendall(msg.encode())