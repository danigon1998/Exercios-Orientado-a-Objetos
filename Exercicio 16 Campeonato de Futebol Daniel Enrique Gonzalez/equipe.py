import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Curso:
  def __init__(self,sigla,nome):
    self.__sigla = sigla
    self.__nome = nome

  @property
  def sigla(self):
    return self.__sigla

  @property
  def nome(self):
    return self.__nome

class Estudante:
  def __init__(self,nroMatric, nome, curso):
    self.__nroMatric = nroMatric
    self.__nome = nome
    self.__curso = curso

  @property
  def nroMatric(self):
    return self.__nroMatric

  @property
  def nome(self):
    return self.__nome

  @property
  def curso(self):
    return self.__curso

  def getDados(self):
    return "Nome: " + self.__nome + "\nNro de matricula: " + str(self.__nroMatric) + "\n"

class Equipe:
  def __init__(self,curso = ""):
    self.__curso = curso
    self.__listaEstudantes = []

  @property
  def curso(self):
    return self.__curso

  @property
  def listaEstudantes(self):
    return self.__listaEstudantes

  def colocaCurso(self,curso):
    self.__curso = curso

  def addEstudante(self,estudante):
    self.__listaEstudantes.append(estudante)

class LimiteInsereEquipe(tk.Toplevel):
    def __init__(self, controle, listaCursos):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Equipe")
        self.controle = controle

        self.frameCurso = tk.Frame(self)
        self.frameEstudante = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCurso.pack()
        self.frameEstudante.pack()
        self.frameButton.pack()
      
        self.labelCurso = tk.Label(self.frameCurso, text="Curso: ")
        self.labelEstudante = tk.Label(self.frameEstudante,text="Estudante: ")
        self.labelCurso.pack(side="left")
        self.labelEstudante.pack(side="left")

        self.inputEstudante = tk.Entry(self.frameEstudante, width=20)
        self.inputEstudante.pack(side = "left")
      
        self.escolheCurso = tk.StringVar()
        self.comboboxCurso = ttk.Combobox(self.frameCurso,width = 20, values = listaCursos, text = self.escolheCurso)
        self.comboboxCurso.pack(side = "left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonCria = tk.Button(self.frameButton ,text="Criar")      
        self.buttonCria.pack(side="left")
        self.buttonCria.bind("<Button>", controle.criaHandler) 

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteDados(tk.Toplevel):
    def __init__(self,controle):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Dados do Campeonato")
        self.ctrl = controle

        self.frameDados = tk.Frame(self)
        self.frameDados.pack()
        self.textDados = tk.Text(self.frameDados, height=20,width=50)
        self.textDados.pack()
        self.textDados.config(state=tk.DISABLED)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        

class LimiteConsultaEquipe(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Consultar Equipes")
        self.ctrl = controle

        self.frameEquipe = tk.Frame(self)
        self.frameEquipe.pack()
        self.frameButton = tk.Frame(self)
        self.frameButton.pack()

        self.labelEquipe = tk.Label(self.frameEquipe,text="Sigla do curso: ")
        self.labelEquipe.pack(side="left")

        self.inputEquipe = tk.Entry(self.frameEquipe, width = 20)
        self.inputEquipe.pack(side="left")

        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler2)

        self.frameEstudantes = tk.Frame(self)
        self.frameEstudantes.pack()
        self.textEstudantes = tk.Text(self.frameEstudantes, height=20,width=70)
        self.textEstudantes.pack()
        self.textEstudantes.config(state=tk.DISABLED)
      
    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class CtrlEquipe():
    def __init__(self, controlador):
      if not os.path.isfile("equipe.pickle"):
        self.listaEquipes =  []
      else:
        with open("equipe.pickle","rb") as f:
          self.listaEquipes = pickle.load(f)
          
      self.controlador = controlador
      c1 = Curso("CCO", "Ciência da Computação")
      c2 = Curso("SIN", "Sistemas de Informação")
      c3 = Curso("EEL", "Engenharia Elétrica")
      self.listaCurso = []
      self.listaCurso.append(c1)
      self.listaCurso.append(c2)
      self.listaCurso.append(c3)
      #Inserir mais cursos, se quiser
      self.listaEstudante = []
      self.listaEstudante.append(Estudante(1001, "José da Silva", c1))
      self.listaEstudante.append(Estudante(1002, "João de Souza", c1))
      self.listaEstudante.append(Estudante(1003, "Rui Santos", c2))
      self.listaEstudante.append(Estudante(1004, "Pedro Teixeira", c1))
      self.listaEstudante.append(Estudante(1005, "João Castro", c3))
      self.listaEstudante.append(Estudante(1006, "Francisco Almeida", c2))
      self.listaEstudante.append(Estudante(1007, "Carlos Rocha", c1))
      self.listaEstudante.append(Estudante(1008, "Paulo Valle", c2))
      self.listaEstudante.append(Estudante(1009, "Lucas Pedreira", c2))
      self.listaEstudante.append(Estudante(1010, "Vinicius Campos", c3))
      self.listaEstudante.append(Estudante(1011, "Marcos Correira", c3))
      self.listaEstudante.append(Estudante(1012, "Luis Braga", c3))
      #Inserir mais 7 alunos, totalizando pelo menos 10 na lista

    def salvaEquipe(self):
      if len(self.listaEquipes) != 0:
        with open("equipe.pickle","wb") as f:
          pickle.dump(self.listaEquipes,f)
    
    def cadastraEquipe(self):
        #self.E = Equipe()
        self.listaAtual = []
        listaNomesCursos = []
        for n in self.listaCurso:
          listaNomesCursos.append(n.nome)
        self.limiteIns = LimiteInsereEquipe(self, listaNomesCursos)

    def imprimeEquipe(self):
        self.limiteImp = LimiteDados(self)
        numEqui = len(self.listaEquipes)
        numEst = 0
        for e in self.listaEquipes:
          for est in e.listaEstudantes:
            numEst += 1

        med = numEst/numEqui
        s = "Total de número de equipes: " + str(numEqui) + "\n"
        s += "Total de número de estudantes no campeonato: " + str(numEst) + "\n"
        s += "Média de estudantes por equipe: " + str(med) + "\n"
        self.limiteImp.textDados.config(state = "normal")
        self.limiteImp.textDados.delete("1.0",tk.END)
        self.limiteImp.textDados.insert(1.0,s)
        self.limiteImp.textDados.config(state = "disable")

    def consultaEquipe(self):
        self.limiteCons = LimiteConsultaEquipe(self)
        
    
    def enterHandler(self, event):
        curso = self.limiteIns.comboboxCurso.get()
        numero = int(self.limiteIns.inputEstudante.get())
        s = 0
        for est in self.listaEstudante:
          if est.nroMatric == numero  and est.curso.nome == curso:
            s = 1
            for nr in self.listaAtual:
              if est.nroMatric == nr.nroMatric:
                s = 2
                break
            if s == 2:
              self.limiteIns.mostraJanela("Problema", "Este estudante já está neste grupo")
            else:
              self.listaAtual.append(est)
              self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
            self.clearHandler(event)
            break

        if s == 0:
          self.limiteIns.mostraJanela("Problema", "Este número de matrícula não existe neste curso")

    def clearHandler(self, event):
        self.limiteIns.inputEstudante.delete(0, len(self.limiteIns.inputEstudante.get()))

    def criaHandler(self,event):
        if len(self.listaAtual) > 0:
          E = Equipe(self.listaAtual[0].curso)
          p = 0
          for est in self.listaAtual:
            if est.curso.nome != E.curso.nome:
              self.listaAtual.pop(p)
            p += 1
          p = 0
          for e in self.listaEquipes:
            if e.curso.sigla == E.curso.sigla:
              self.listaEquipes.pop(p)
              break
            p += 1
          for i in self.listaAtual:
            E.addEstudante(i)
          self.listaEquipes.append(E)
          self.listaAtual.clear()
          
          self.limiteIns.mostraJanela("Sucesso", "Equipe criada com sucesso")
        else:
          self.limiteIns.mostraJanela("Problema", "Não existe estudantes nesta equipe")
  
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def enterHandler2(self,event):
        sigla = self.limiteCons.inputEquipe.get()
        s1 = 0
        s2 = 0
        for c in self.listaCurso:
          if sigla == c.sigla:
            s1 = 1
            for e in self.listaEquipes:
              if sigla == e.curso.sigla:
                s2 = 1
                self.limiteCons.textEstudantes.config(state = "normal")
                self.limiteCons.textEstudantes.delete("1.0",tk.END)
                for es in e.listaEstudantes:
                  est = es.getDados()
                  self.limiteCons.textEstudantes.insert(1.0,est)
            self.limiteCons.textEstudantes.config(state = "disable")
            if s2 == 0:
              self.limiteCons.mostraJanela("Problema","Não existe nenhuma equipe deste curso")
        if s1 ==0:
           self.limiteCons.mostraJanela("Problema","Não existe esta sigla")
            
    def fechaHandler2(self, event):
        self.limiteAva.destroy()
