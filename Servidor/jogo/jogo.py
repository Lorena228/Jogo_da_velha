
from threading import Thread

class JogoDaVelha:
  def rodar_jogo():
    nome1 = input("Qual o nome do jogador 1? ")
    nome2 = input("Qual o nome do jogador 2? ")

    jogar1 = j.Jogador(nome1, "X")
    jogar2 = j.Jogador(nome2, "O")

    quadro = t.Tabuleiro()

    print("----------Jogo da Velha----------")
    print("Jogador 1 - X \nJogador 2 - O")

    rodada = 1
    jogadores = {'jogar1': jogar1, 'jogar2': jogar2}
    while True:
      quadro.mostra_tabuleiro()
      jogador = None
      if rodada % 2 == 0:
        jogador = jogadores["jogar2"]
      else:
        jogador = jogadores['jogar1']
      jogada = input("digite o número correspondente a posição que deseja marcar: ")
      if quadro.verificar_posicao(jogada):
        jogador.registro(jogada)
        quadro.marcar(jogada, jogador.get_icone())


      acabou = quadro.verificar_vitoria(jogar1, jogar2)
      if not acabou:
        if quadro.verificar_empate():
          quadro.mostra_tabuleiro()
          print("Empatou!")
          break
      elif acabou == True:
        vencedor = quadro.get_vencedor()
        quadro.mostra_tabuleiro()
        print(vencedor.get_nome() + ", Parabéns você ganhou!")
        break
      rodada += 1

