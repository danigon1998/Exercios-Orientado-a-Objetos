from abc import ABC, abstractmethod

class Venda:
  def __init__(self,codImovel,mesVenda,anoVenda,valorVenda):
    self.__codImovel = codImovel
    self.__mesVenda = mesVenda
    self.__anoVenda = anoVenda
    self.__valorVenda = valorVenda
  
  @property
  def codImovel(self):
    return self.__codImovel

  @property
  def mesVenda(self):
    return self.__mesVenda

  @property
  def anoVenda(self):
    return self.__anoVenda

  @property
  def valorVenda(self):
    return self.__valorVenda

class Vendedor(ABC):
  def __init__(self,codigo,nome):
    self.__codigo = codigo
    self.__nome = nome
    self.__venda = []

  @property
  def codigo(self):
    return self.__codigo

  @property
  def nome(self):
    return self.__nome

  @property
  def venda(self):
    return self.__venda

  def adicionaVenda(self,codImovel,mesVenda,anoVenda,valorVenda):
    venda = Venda(codImovel,mesVenda,anoVenda,valorVenda)
    self.__venda.append(venda)

  @abstractmethod
  def getDados(self):
    pass

  @abstractmethod
  def calculaRenda(self,mes,ano):
    pass

class Contratado(Vendedor):
  def __init__(self,codigo,nome,salario,nroCartTrabalho):
    super().__init__(codigo,nome)
    self.__salario = salario
    self.__nroCartTrabalho = nroCartTrabalho

  @property
  def nroCartTrabalho(self):
    return self.__nroCartTrabalho

  @property
  def salario(self):
    return self.__salario

  def getDados(self):
    return "Nome: {} - Nro Carteira: {}".format(self.nome,self.__nroCartTrabalho)

  def calculaRenda(self,mes,ano):
    total = self.__salario
    for x in self.venda:
      if x.mesVenda == mes and x.anoVenda == ano:
        total += x.valorVenda*0.01
    return total    

class Comissionado(Vendedor):
  def __init__(self,codigo,nome,nroCPF,comissao):
    super().__init__(codigo,nome)
    self.__nroCPF = nroCPF
    self.__comissao = comissao

  @property
  def nroCartTrabalho(self):
    return self.__nroCartTrabalho

  @property
  def comissao(self):
    return self.__comissao

  def getDados(self):
    return "Nome: {} - Nro CPF: {}".format(self.nome,self.__nroCPF)

  def calculaRenda(self,mes,ano):
    total = 0
    for x in self.venda:
      if x.mesVenda == mes and x.anoVenda == ano:
        total = total + x.valorVenda*self.__comissao/100
    return total    

if __name__ == "__main__":
  funcContratado = Contratado(1001, 'João da Silva', 2000, 1234)
  funcContratado.adicionaVenda(100, 3, 2022, 200000)
  funcContratado.adicionaVenda(101, 3, 2022, 300000)
  funcContratado.adicionaVenda(102, 4, 2022, 600000)
  funcComissionado = Comissionado(1002, 'José Santos', 4321, 5)
  funcComissionado.adicionaVenda(200, 3, 2022, 200000)
  funcComissionado.adicionaVenda(201, 3, 2022, 400000)
  funcComissionado.adicionaVenda(202, 4, 2022, 500000)
  listaFunc = [funcContratado, funcComissionado]
  for func in listaFunc:
    print(func.getDados())
    print("Renda no mês 3 de 2022: ")
    print(func.calculaRenda(3, 2022))