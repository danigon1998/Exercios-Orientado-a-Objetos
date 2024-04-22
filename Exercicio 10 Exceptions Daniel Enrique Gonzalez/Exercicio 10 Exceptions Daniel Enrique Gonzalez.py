from abc import ABC, abstractmethod

class Pessoa(ABC):
  def __init__(self,nome,endereco,idade,cpf):
    self.__nome = nome
    self.__endereco = endereco
    self.__idade = idade
    self.__cpf = cpf

  @property
  def nome(self):
    return self.__nome

  @property
  def endereco(self):
    return self.__endereco

  @property
  def idade(self):
    return self.__idade

  @property
  def cpf(self):
    return self.__cpf

  @abstractmethod
  def printDescricao(self):
    pass

class Professor(Pessoa):
  def __init__(self,nome,endereco,idade,cpf,titulacao):
    super().__init__(nome,endereco,idade,cpf)
    self.__titulacao = titulacao

  @property
  def titulacao(self):
    return self.__titulacao

  def printDescricao(self):
    print("Nome: {}\nEndereco: {}\nIdade: {}\nCPF: {}\nTitulacao: {}\n".format(self.nome,self.endereco,self.idade,self.cpf,self.__titulacao))

class Aluno(Pessoa):
  def __init__(self,nome,endereco,idade,cpf,curso):
    super().__init__(nome,endereco,idade,cpf)
    self.__curso = curso

  @property
  def curso(self):
    return self.__curso

  def printDescricao(self):
    print("Nome: {}\nEndereco: {}\nIdade: {}\nCPF: {}\nCurso: {}\n".format(self.nome,self.endereco,self.idade,self.cpf,self.__curso))
    
class TitulacaoNaoAtingeNivelRequerido(Exception):
  pass

class ProfessorNaoTemIdadeNecessaria(Exception):
  pass

class CursoIncorreto(Exception):
  pass

class AlunoNaoTemIdadeNecessaria(Exception):
  pass 

class CPFRepetido(Exception):
  pass

if __name__ == "__main__":
  listaExemplo = [Professor("Pedro","Av 25",35,"1234-567","Doutor"),Aluno("Maria","Av 26",19,"1334-777","SIN"),Professor("Thiago","Av 27",29,"1234-777","Doutor"),Aluno("Carlos","Av 28",17,"1222-567","CCO"),Aluno("Isabella","Av 29",20,"1111-567","CCO"),Professor("João","Av 30",35,"1234-777","Licenciado"),Aluno("Luis","Av 31",21,"1234-666","ADM"),Professor("Bruno","Av 32",33,"4321-567","Doutor"),Professor("Gabriel","Av 33",33,"4321-567","Doutor"),Aluno("Jason","Av 36",20,"1234-567","CCO")]
  cadastro = []

  for pessoa in listaExemplo:

    try:
      if type(pessoa) == Professor:
        if pessoa.titulacao != "Doutor":
          raise TitulacaoNaoAtingeNivelRequerido
        elif pessoa.idade < 30:
          raise ProfessorNaoTemIdadeNecessaria
      elif type(pessoa) == Aluno:
        if pessoa.curso != "CCO" and pessoa.curso != "SIN":
          raise CursoIncorreto
        elif pessoa.idade < 18:
          raise AlunoNaoTemIdadeNecessaria
      for x in cadastro:
        if x.cpf == pessoa.cpf:
          raise CPFRepetido

    except TitulacaoNaoAtingeNivelRequerido:
        print("O professor {} ({}) não tem o titulo requerido".format(pessoa.nome,pessoa.titulacao))

    except ProfessorNaoTemIdadeNecessaria:
        print("O professor {} ({}) não tem a idade requerida".format(pessoa.nome,pessoa.idade))

    except CursoIncorreto:
        print("O Aluno {} ({}) não é nem de CCO nem de SIN".format(pessoa.nome,pessoa.curso))

    except AlunoNaoTemIdadeNecessaria:
        print("O Aluno {} ({}) não tem a idade requerida".format(pessoa.nome,pessoa.idade))
    
    except CPFRepetido:
      print("O CPF de {} ({}) já se encontra no cadastro".format(pessoa.nome, pessoa.cpf))

    else:
      cadastro.append(pessoa)

print()
for pessoa in cadastro:
  pessoa.printDescricao()
      