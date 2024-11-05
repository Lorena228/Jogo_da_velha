import socket as s
from threading import Thread
from time import sleep
import jogo.jogador as j
import jogo.tabuleiro as t

class JogoDaVelha:

  entradas_jogador_2 = [1235, 1236, 1237, 1238, 1239]

  def conectar_jogador_dois(self, conn_socket:s.socket):
    for porta in self.entradas_jogador_2:
      try:
        conn_socket.bind(('', porta))
        break
      except: None
    conn_socket.listen(1)
    conn, addr = conn_socket.accept()
    print(f"Conexão 2 estabelecida com {addr}")
    return conn

  def handle(self, conn1:s.socket, conn2: s.socket):
    tabuleiro = t.Tabuleiro()
    rodada = 1

    conn1.sendall('Qual o nome do jogador-1? '.encode())
    data = conn1.recv(1024)
    nome_jogador = data.decode()
    jogadores = {'jog1':j.Jogador(nome_jogador, 'X'), 'jog2':None}

    conn2 = self.conectar_jogador_dois(conn2)

    conn2.sendall('Qual o nome do jogador-2? '.encode())
    data = conn2.recv(1024)
    nome_jogador = data.decode()
    jogadores['jog2'] = j.Jogador(nome_jogador, 'O')

    msg = f"----------Jogo da Velha----------\n{jogadores['jog1'].get_nome()} - X \n{jogadores['jog2'].get_nome()} - O"
    conn1.sendall(msg.encode())
    conn2.sendall(msg.encode())

    while True:
      while True:
        tabuleiro.mostra_tabuleiro([conn1, conn2])
        jogador = None
        jogada = ''
        if rodada % 2 == 0:
          jogador = jogadores["jog2"]
        else:
          jogador = jogadores['jog1']
        while True:
          if jogada != '':
            try: 
              num = int(jogada)
              if num in range(1,10):
                break
              else:
                jogada = ''
                continue
            except:
              jogada = ''
              continue
          else:
            if jogador.get_icone() == 'X':
              conn1.sendall("\nDigite o número correspondente a posição que deseja marcar: ".encode())
              jogada = conn1.recv(1024).decode()
            else:
              conn2.sendall("Digite o número correspondente a posição que deseja marcar: ".encode())
              jogada = conn2.recv(1024).decode()
        if tabuleiro.verificar_posicao(jogada):
          jogador.registro(jogada)
          tabuleiro.marcar(jogada, jogador.get_icone())
          break
        else: 
          continue

      acabou = tabuleiro.verificar_vitoria(jogadores['jog1'], jogadores['jog2'])
      conex = [conn1,conn2]
      if not acabou:
        if tabuleiro.verificar_empate():
          tabuleiro.mostra_tabuleiro(conex)
          for conn in conex:
            conn.sendall("Empatou!".encode())
          break
      elif acabou == True:
        vencedor = tabuleiro.get_vencedor()
        tabuleiro.mostra_tabuleiro(conex)
        for conn in conex:
          conn.sendall((vencedor.get_nome() + ", você é o vencedor!").encode())
        break
      rodada += 1
    for conn in conex:
      conn.close()

  def start(self):
    server_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    server_socket.bind(('', 1234))
    server_socket.listen(5)
    print('servidor iniciado!')
    conn_socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    while True:
      conn, addr = server_socket.accept()
      print(f"Conexão 1 estabelecida com {addr}")
      novo_jogo = Thread(target=self.handle, args=(conn, conn_socket), daemon=True)
      novo_jogo.start()


if __name__ == '__main__':
  jogo = JogoDaVelha()
  jogo.start()