import datetime

class Produto(object):
  def __init__(self,idProduto,nome,descricao,preco):
    self.idProduto = idProduto
    self.nome = nome
    self.descricao = descricao
    self.preco = preco

#Herança Superclasse
class Pessoa(object):
  def __init__(self,nome):
    self.nome = nome
  def calcularIdade(self): 
    hoje = datetime.date.today()
    idade = hoje.year - self.dataNascimento.year - ((hoje.month, hoje.day)<
          (self.dataNascimento.month, self.dataNascimento.day))
    return idade


class Cliente(Pessoa):
  #Polimorfismo
  def __init__(self,nome,email,telefone, dataNascimento,idCliente):
    super().__init__(nome)
    self.idCliente = idCliente
    self.telefone = telefone
    self.email = email
    self.dataNascimento = dataNascimento
#Herança
class Atendente(Pessoa):
  #Polimorfismo
  def __init__(self,nome,idAtendente):
    super().__init__(nome)
    self.idAtendente = idAtendente

class Venda(object):
  def __init__(self, idVenda,produto,quantidade, atendente, cliente,dataVenda):
    self.produto = produto
    self.quantidade = quantidade
    self.idVenda = idVenda
    self.cliente = cliente
    self.atendente = atendente
    self.dataVenda = dataVenda
  def calcularVenda(self):
    return self.quantidade * self.produto.preco