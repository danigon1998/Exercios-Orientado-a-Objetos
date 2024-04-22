from abc import ABC, abstractmethod

class EmpDomestica(ABC):
  def __init__(self):
    self.__nome = ""
    self.__telefone = ""
  def setNome(self,nome):
    self.__nome = nome
  def setTelefone(self,telefone):
    self.__telefone = telefone  
  def getNome(self):
    return self.__nome
  def getTelefone(self):
    return self.__telefone  
  @abstractmethod
  def getSalario(self):
    pass

class Horista(EmpDomestica):
  def __init__(self,horasTrabalhadas,valorPorHora):
    super().__init__()
    self.__horasTrabalhadas = horasTrabalhadas
    self.__valorPorHora = valorPorHora

  def getSalario(self):
    return self.__horasTrabalhadas * self.__valorPorHora

class Diarista(EmpDomestica):
  def __init__(self,diasTrabalhados,valorPorDia):
    super().__init__()
    self.__diasTrabalhados = diasTrabalhados
    self.__valorPorDia = valorPorDia

  def getSalario(self):
    return self.__diasTrabalhados * self.__valorPorDia

class Mensalista(EmpDomestica):
  def __init__(self,valorMensal):
    super().__init__()
    self.__valorMensal = valorMensal

  def getSalario(self):
    return self.__valorMensal

if __name__ == "__main__":
  empre1 = Horista(160,12)
  empre2 = Diarista(20,60)
  empre3 = Mensalista(1200)
  empre1.setNome("Maria Luiza")
  empre2.setNome("Clara da Silva")
  empre3.setNome("Isabela Martins")
  empre1.setTelefone("000-001")
  empre2.setTelefone("000-002")
  empre3.setTelefone("000-003")
  listaEmpregadas = [empre1, empre2, empre3]
  listaSalarios = []
  for empre in listaEmpregadas:
    print("Salario: {}".format(empre.getSalario()))
    listaSalarios.append(empre.getSalario())
  for empre in listaEmpregadas:
    if empre.getSalario() == min(listaSalarios):
      print("Nome: {0:15} - Telefone: {1} - Salario: {2}".format(empre.getNome(), empre.getTelefone(),empre.getSalario()))
  
    