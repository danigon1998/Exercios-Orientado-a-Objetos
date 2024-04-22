from abc import ABC, abstractmethod

class PontoFunc:
  def __init__(self,mes,ano,nroFaltas,nroAtrasos):
    self.__mes = mes
    self.__ano = ano
    self.__nroFaltas = nroFaltas
    self.__nroAtrasos = nroAtrasos

  @property
  def mes(self):
    return self.__mes

  @property
  def ano(self):
    return self.__ano

  @property
  def nroFaltas(self):
    return self.__nroFaltas

  @property
  def nroAtrasos(self):
    return self.__nroAtrasos

  @nroFaltas.setter
  def lancaFaltas(self,nroFaltas):
    self.__nroFaltas = nroFaltas

  @nroAtrasos.setter
  def lancaAtrasos(self,nroAtrasos):
    self.__nroAtrasos = nroAtrasos

class Funcionario(ABC):
  def __init__(self,codigo,nome):
    self.__codigo = codigo
    self.__nome = nome
    self.__pontoMensalFunc = []

  @property
  def codigo(self):
    return self.__codigo

  @property
  def nome(self):
    return self.__nome

  @property
  def pontoMensalFunc(self):
    return self.__pontoMensalFunc

  def adicionaPonto(self,mes,ano,faltas,atrasos):
    x = PontoFunc(mes,ano,faltas,atrasos)
    self.__pontoMensalFunc.append(x)

  def lancaFaltas(self,mes,ano,faltas):
    for x in self.__pontoMensalFunc:
      if mes == x.mes and ano == x.ano:
        x.lancaFaltas = faltas

  def lancaAtrasos(self,mes,ano,atrasos):
    for x in self.__pontoMensalFunc:
      if mes == x.mes and ano == x.ano:
        x.lancaAtrasos = atrasos

  def imprimeFolha(self,mes,ano):
    print("Codigo: {}\nNome: {}\nSalario Liquido: {:.2f}\nBonus: {:.2f}".format(self.__codigo,self.__nome,self.calculaSalario(mes,ano),self.calculaBonus(mes,ano)))

  @abstractmethod
  def calculaSalario(self,mes,ano):
    pass

  @abstractmethod
  def calculaBonus(self,mes,ano):
    pass

class Professor(Funcionario):
  def __init__(self,codigo,nome,titulacao,salarioHora,nroHoras):
    super().__init__(codigo,nome)
    self.__titulacao = titulacao
    self.__salarioHora = salarioHora
    self.__nroHoras = nroHoras

  @property
  def titulacao(self):
    return self.__titulacao

  @property
  def salarioHora(self):
    return self.__salarioHora

  @property
  def nroHoras(self):
    return self.__nroHoras

  def calculaSalario(self,mes,ano):
    for x in self.pontoMensalFunc:
      if x.mes == mes and x.ano == ano:
        salario = self.__salarioHora * self.__nroHoras - self.__salarioHora * x.nroFaltas
    return salario

  def calculaBonus(self,mes,ano):
    for x in self.pontoMensalFunc:
      if x.mes == mes and x.ano == ano:
        bonus = self.calculaSalario(mes,ano) * (0.1-(x.nroAtrasos)/100)
    return bonus

class TecAdmin(Funcionario):
  def __init__(self,codigo,nome,funcao,salarioMensal):
    super().__init__(codigo,nome)
    self.__funcao = funcao
    self.__salarioMensal = salarioMensal

  @property
  def funcao(self):
    return self.__funcao

  @property
  def salarioMensal(self):
    return self.__salarioMensal

  def calculaSalario(self,mes,ano):
    for x in self.pontoMensalFunc:
      if x.mes == mes and x.ano == ano:
        salario = self.__salarioMensal - (self.__salarioMensal/30) * x.nroFaltas
    return salario

  def calculaBonus(self,mes,ano):
    for x in self.pontoMensalFunc:
      if x.mes == mes and x.ano == ano:
        bonus = self.calculaSalario(mes,ano) * (0.08-(x.nroAtrasos)/100)
    return bonus

if __name__ == "__main__":
  funcionarios = []
  prof = Professor(1, "Joao", "Doutor", 45.35, 32)
  prof.adicionaPonto(4, 2021, 0, 0)
  prof.lancaFaltas(4, 2021, 2)
  prof.lancaAtrasos(4, 2021, 3)
  funcionarios.append(prof)
  tec = TecAdmin(2, "Pedro", "Analista Contábil", 3600)
  tec.adicionaPonto(4, 2021, 0, 0)
  tec.lancaFaltas(4, 2021, 3)
  tec.lancaAtrasos(4, 2021, 4)
  funcionarios.append(tec)
  for func in funcionarios:
    func.imprimeFolha(4, 2021)
    print()