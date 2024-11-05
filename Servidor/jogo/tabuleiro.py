class Tabuleiro:
  def __init__(self):
    self.posicoes = {'7': ' ' , '8': ' ' , '9': ' ',
                    '4': ' ' , '5': ' ' , '6': ' ',
                    '1': ' ' , '2': ' ' , '3': ' '}
    self.vencedor = None

  def mostra_tabuleiro(self, connections:list):
    for conn in connections:
      conn.sendall(f"┌───┬───┬───┐\n│ {self.posicoes['7']} │ {self.posicoes['8']} │ {self.posicoes['9']} │\n├───┼───┼───┤\n│ {self.posicoes['4']} │ {self.posicoes['5']} │ {self.posicoes['6']} │\n├───┼───┼───┤\n│ {self.posicoes['1']} │ {self.posicoes['2']} │ {self.posicoes['3']} │\n└───┴───┴───┘".encode())

  def verificar_vitoria(self, jogador1, jogador2):
    pos1 = jogador1.get_jogadas()
    pos2 = jogador2.get_jogadas()

    vitoria = {'1':False,'2':False}
    
    # horizontais
    if ('1' in pos1 and '2' in pos1 and '3' in pos1) or ('4' in pos1 and '5' in pos1 and '6' in pos1) or ('7' in pos1 and '8' in pos1 and '9' in pos1):
      vitoria ['1'] = True
    elif ('1' in pos2 and '2' in pos2 and '3' in pos2) or ('4' in pos2 and '5' in pos2 and '6' in pos2) or ('7' in pos2 and '8' in pos2 and '9' in pos2):
      vitoria ['2'] = True
    
    #verticais
    elif ('1' in pos1 and '4' in pos1 and '7' in pos1) or ('2' in pos1 and '5' in pos1 and '8' in pos1) or ('3' in pos1 and '6' in pos1 and '9' in pos1):
      vitoria ['1'] = True
    elif ('1' in pos2 and '4' in pos2 and '7' in pos2) or ('2' in pos2 and '5' in pos2 and '8' in pos2) or ('3' in pos2 and '6' in pos2 and '9' in pos2):
      vitoria ['2'] = True

    #diagonais
    elif ('1' in pos1 and '5' in pos1 and '9' in pos1) or ('3' in pos1 and '5' in pos1 and '7' in pos1):
      vitoria ['1'] = True
    elif ('1' in pos2 and '5' in pos2 and '9' in pos2) or ('3' in pos2 and '5' in pos2 and '7' in pos2):
      vitoria ['2'] = True

    #verificador de vitórias
    if not vitoria['1'] and not vitoria['2']:
      return False
    elif vitoria['1']:
      self.vencedor = jogador1
    elif vitoria['2']:
      self.vencedor = jogador2
    return True
  
  def verificar_empate(self):
    ocupado = True
    for chave, valor in self.posicoes.items():
      if valor == ' ':
        ocupado = False
    return ocupado
  
  def get_vencedor(self):
    return self.vencedor
  
  def verificar_posicao(self, posicao):
    if self.posicoes[posicao] != ' ':
      return False
    else:
      return True
    
  def marcar(self, jogada, icone):
    self.posicoes[jogada] = icone