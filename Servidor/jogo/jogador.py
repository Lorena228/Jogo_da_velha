class Jogador:

  def __init__(self, nome, icone):
    self.nome = nome
    self.icone = icone
    self.jogadas = []

  def registro(self, posicao):
    self.jogadas.append(posicao)

  def get_jogadas(self):
    return self.jogadas
  
  def get_nome(self):
    return self.nome
  
  def get_icone(self):
    return self.icone

