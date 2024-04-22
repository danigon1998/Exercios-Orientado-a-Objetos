
class Aluno:
  def __init__(self,nome,nMatricula):
    self.__nome = nome
    self.__nMatricula = nMatricula

    self.__curso = ""
    self.__historico = []

  @property
  def nome(self):
    return self.__nome

  @property
  def nMatricula(self):
    return self.__nMatricula

  @property
  def curso(self):
    return self.__curso 

  @property
  def historico(self):
    return self.__historico

  def addCurso(self,curso):
    self.__curso = curso

  def addHistorico(self,historico):
    self.__historico = historico.historico

  def mostrarHistorico(self):
    if len(self.__historico) > 0:
      obri = 0
      elet = 0
      lstTipoDisciplina =[]
      tipo = 0
      for dis in self.__historico:
        O = False
        for dis1 in self.__curso.grade.disciplinas:
          if dis.codigo == dis1.codigo:
            O = True
        if O == True:
          obri = obri + dis.cargaHoraria
          lstTipoDisciplina.append("Obrigatoria")
        else:
          elet = elet + dis.cargaHoraria
          lstTipoDisciplina.append("Eletiva")
      
      print("O aluno {}, matricula {} tem realizado um total de {} horas obrigatorias e um total de {} eletivas".format(self.__nome,self.__nMatricula,obri,elet))
      print("O aluno fez as seguintes disciplinas:")
      for dis in self.__historico:
        print("{0:23} - {1:11} - horas: {2}".format(dis.nome,lstTipoDisciplina[tipo],dis.cargaHoraria))
        tipo+=1
    else:
      print("O aluno {}, matricula {} ainda não cursou nenhuma disciplina".format(self.__nome,self.__nMatricula))

class Curso:
  def __init__(self,nome,grade):
    self.__nome = nome
    self.__grade = grade

  @property
  def nome(self):
    return self.__nome

  @property
  def grade(self):
    return self.__grade

class Grade:
  def __init__(self,ano):
    self.__ano = ano
    
    self.__disciplinas = []

  @property
  def ano(self):
    return self.__ano

  @property
  def disciplinas(self):
    return self.__disciplinas

  def addDisciplina(self,disciplina):
    self.__disciplinas.append(disciplina)

class Disciplina:
  def __init__(self,codigo,nome,cargaHoraria):
    self.__codigo = codigo
    self.__nome = nome
    self.__cargaHoraria = cargaHoraria

  @property
  def codigo(self):
    return self.__codigo

  @property
  def nome(self):
    return self.__nome

  @property
  def cargaHoraria(self):
    return self.__cargaHoraria

class Historico:
  def __init__(self):
    self.__historico = []

  @property
  def historico(self):
    return self.__historico

  def addDisciplina(self,disciplina):
    self.__historico.append(disciplina)


if __name__ == "__main__": 

  Daniel = Aluno("Daniel Gonzalez","2022004588")
  disciplina1 = Disciplina("C011","Algoritmos",96)
  disciplina2 = Disciplina("F011","Fisica",96)
  disciplina3 = Disciplina("M011","Calculo 1",96)
  disciplina4 = Disciplina("M012","Algebra 1",64)
  disciplina5 = Disciplina("AD11","Administracao 1",32)
  disciplina6 = Disciplina("E011","Introducao a engenharia",64)
  disciplina7 = Disciplina("C012","Programacao 1",96)
  disciplina8 = Disciplina("S011","Fundamentos de sistemas",96)
  disciplina9 = Disciplina("Q011","Quimica",64)
  grade1 = Grade(2023)
  grade2 = Grade(2022)
  grade1.addDisciplina(disciplina1)
  grade1.addDisciplina(disciplina3)
  grade1.addDisciplina(disciplina5)
  grade1.addDisciplina(disciplina7)
  grade1.addDisciplina(disciplina8)
  grade2.addDisciplina(disciplina2)
  grade2.addDisciplina(disciplina3)
  grade2.addDisciplina(disciplina4)
  grade2.addDisciplina(disciplina6)
  grade2.addDisciplina(disciplina9)
  historicoD = Historico()
  historicoD.addDisciplina(disciplina1)
  historicoD.addDisciplina(disciplina3)
  historicoD.addDisciplina(disciplina5)
  historicoD.addDisciplina(disciplina6)
  historicoD.addDisciplina(disciplina9)
  Sistemas = Curso("Sistemas de Informacao",grade1)
  Mecanica = Curso("Mecanica",grade2)
  Daniel.addCurso(Sistemas)
  Daniel.addHistorico(historicoD)
  Daniel.mostrarHistorico()

  