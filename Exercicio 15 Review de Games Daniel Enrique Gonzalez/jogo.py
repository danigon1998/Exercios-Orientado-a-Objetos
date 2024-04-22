import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os.path
import pickle

class Jogo:
    def __init__(self, codigo, titulo, console, genero, preco):
        self.__codigo = codigo
        self.__titulo = titulo
        self.console = console
        self.genero = genero
        self.preco = preco

        self.__avaliacoes = []
    
    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def console(self):
        return self.__console

    @console.setter
    def console(self, valor):
        self.consoles = ["Xbox", "PlayStation", "Switch", "PC"]
        if not valor in self.consoles:
            raise ValueError("Console inválido: {}".format(valor))
        else:
            self.__console = valor

    @property
    def genero(self):
        return self.__genero

    @genero.setter
    def genero(self, valor):
        self.generos = ["Ação", "Aventura", "Estratégia", "RPG", "Esporte", "Simulação"]
        if not valor in self.generos:
            raise ValueError("Gênero inválido: {}".format(valor))
        else:
            self.__genero = valor         

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, valor):
        if int(valor) < 1 or int(valor) > 500 or valor.isnumeric() == False:
            raise ValueError("Valor inválido: {}".format(valor))
        else:
            self.__preco = int(valor)

    @property
    def avaliacoes(self):
      return self.__avaliacoes
  
    def addAvaliacao(self,valor):
      self.avaliacoes.append(valor)

    def getMedia(self):
      media = 0
      for i in self.avaliacoes:
        media += i

      media = media/len(self.avaliacoes)
      return round(media)

    def getJogo(self):
        return "Título: " + str(self.titulo)\
        + "\nCodigo: " + str(self.codigo)\
        + "\nConsole: " + str(self.console)\
        + "\nGênero: " + str(self.genero)\
        + "\nPreço: " + str(self.preco)
    

class LimiteInsereJogo(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x200')
        self.title("Vinho")
        self.controle = controle

        self.frameCodigo = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameConsole = tk.Frame(self)
        self.frameGenero = tk.Frame(self)
        self.framePreco = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        
        self.frameCodigo.pack()
        self.frameNome.pack()
        self.frameConsole.pack()
        self.frameGenero.pack()
        self.framePreco.pack()
        self.frameButton.pack()
      
        self.labelCodigo = tk.Label(self.frameCodigo, text="Codigo: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelConsole = tk.Label(self.frameConsole, text="Console: ")
        self.labelGenero = tk.Label(self.frameGenero, text="Gênero: ")
        self.labelPreco = tk.Label(self.framePreco, text="Preco: ")
        self.labelCodigo.pack(side="left")
        self.labelNome.pack(side="left")
        self.labelConsole.pack(side="left")
        self.labelGenero.pack(side="left")
        self.labelPreco.pack(side="left")

        self.inputCodigo = tk.Entry(self.frameCodigo, width=10)
        self.inputNome = tk.Entry(self.frameNome, width=20)
        self.inputConsole = tk.Entry(self.frameConsole, width=15)
        self.inputGenero = tk.Entry(self.frameGenero, width=20)
        self.inputPreco = tk.Entry(self.framePreco, width=10)
        self.inputCodigo.pack(side="left")
        self.inputNome.pack(side="left")
        self.inputConsole.pack(side="left")
        self.inputGenero.pack(side="left")
        self.inputPreco.pack(side="left")
      
        self.buttonSubmit = tk.Button(self.frameButton ,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controle.enterHandler)
      
        self.buttonClear = tk.Button(self.frameButton ,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controle.clearHandler)  

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)

class LimiteAvaliaJogo(tk.Toplevel):
    def __init__(self,controle,avaliacoes):
        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Avaliar Jogos")
        self.ctrl = controle

        self.frameCodigo = tk.Frame(self)
        self.frameCombo = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameCodigo.pack()
        self.frameCombo.pack()
        self.frameButton.pack()

        self.labelCodigo = tk.Label(self.frameCodigo, text= "Codigo:")
        self.labelCombo = tk.Label(self.frameCombo , text = "Estrelas:")
        self.labelCodigo.pack(side = "left")
        self.labelCombo.pack(side = "left")

        self.inputCodigo = tk.Entry(self.frameCodigo,width = 20)
        self.inputCodigo.pack(side = "left")

        self.escolhaAvaliar  = tk.StringVar()
        self.comboboxAvaliar = ttk.Combobox(self.frameCombo, width = 15, values = avaliacoes, text = self.escolhaAvaliar)
        self.comboboxAvaliar.pack(side = "left")
        self.comboboxAvaliar.bind("<<ComboboxSelected>>",self.ctrl.exibeAvaliacoes)

        self.buttonFecha = tk.Button(self.frameButton ,text="Concluído")      
        self.buttonFecha.pack(side="left")
        self.buttonFecha.bind("<Button>", controle.fechaHandler2)

    def mostraJanela(self, titulo, msg):
        messagebox.showinfo(titulo, msg)
        

class LimiteConsultaJogo(tk.Toplevel):
    def __init__(self, estrelas, controle):

        tk.Toplevel.__init__(self)
        self.geometry('400x250')
        self.title("Consultar Jogos")
        self.ctrl = controle

        self.frameCombo = tk.Frame(self)
        self.frameCombo.pack()

        self.labelCombo = tk.Label(self.frameCombo,text="Estrelas: ")
        self.labelCombo.pack(side="left")
        self.escolhaEstrelas = tk.StringVar()
        self.comboboxEstrelas = ttk.Combobox(self.frameCombo, width = 15 ,values=estrelas, textvariable = self.escolhaEstrelas)
        self.comboboxEstrelas.pack(side="left")
        self.comboboxEstrelas.bind("<<ComboboxSelected>>", self.ctrl.exibeJogos)

        self.frameJogos = tk.Frame(self)
        self.frameJogos.pack()
        self.textJogos = tk.Text(self.frameJogos, height=20,width=40)
        self.textJogos.pack()
        self.textJogos.config(state=tk.DISABLED)

class CtrlJogo():
    def __init__(self, controlador):
      if not os.path.isfile("jogo.pickle"):
        self.listaJogos =  []
      else:
        with open("jogo.pickle","rb") as f:
          self.listaJogos = pickle.load(f)
          
      self.controlador = controlador

    def salvaJogo(self):
      if len(self.listaJogos) != 0:
        with open("jogo.pickle","wb") as f:
          pickle.dump(self.listaJogos,f)
    
    def cadastraJogo(self):
        self.limiteIns = LimiteInsereJogo(self)

    def avaliaJogo(self):
        self.avaliacoes = []
        for i in range(1,6):
          self.avaliacoes.append(str(i))
        self.limiteAva = LimiteAvaliaJogo(self,self.avaliacoes)

    def consultaJogo(self):
        self.estrelas = []
        for i in range(1,6):
          self.estrelas.append(str(i))
        self.limiteCons = LimiteConsultaJogo(self.estrelas, self)
    
    def enterHandler(self, event):
        codigo = self.limiteIns.inputCodigo.get()
        nome = self.limiteIns.inputNome.get().capitalize()
        console = self.limiteIns.inputConsole.get().capitalize()
        genero = self.limiteIns.inputGenero.get().capitalize()
        preco = self.limiteIns.inputPreco.get()

        try:
            jogo = Jogo(codigo, nome, console, genero, preco)
            self.listaJogos.append(jogo)            
            self.limiteIns.mostraJanela('Sucesso', 'Jogo cadastrado com sucesso')
            self.clearHandler(event)
        except ValueError as error:
            self.limiteIns.mostraJanela('Erro', error)            
    

    def clearHandler(self, event):
        self.limiteIns.inputCodigo.delete(0, len(self.limiteIns.inputCodigo.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))
        self.limiteIns.inputConsole.delete(0, len(self.limiteIns.inputConsole.get()))
        self.limiteIns.inputGenero.delete(0, len(self.limiteIns.inputGenero.get()))
        self.limiteIns.inputPreco.delete(0, len(self.limiteIns.inputPreco.get()))
    
    def fechaHandler(self, event):
        self.limiteIns.destroy()

    def fechaHandler2(self, event):
        self.limiteAva.destroy()

    def exibeAvaliacoes(self,event):
        s = 0
        avalSel = self.limiteAva.comboboxAvaliar.get()
        codigoSel = self.limiteAva.inputCodigo.get()
        for j in self.listaJogos:
          if j.codigo == codigoSel:
            s = 1
            j.addAvaliacao(int(avalSel))
            self.limiteAva.mostraJanela("Sucesso","Jogo Avaliado com sucesso")
            pass
        if s == 0:
          self.limiteAva.mostraJanela("Problema","Jogo não encontrado")
            

    def exibeJogos(self, event):
        estSel = self.limiteCons.comboboxEstrelas.get()
        self.limiteCons.textJogos.config(state = "normal")
        self.limiteCons.textJogos.delete("1.0",tk.END)
        for jogo in self.listaJogos:
          if jogo.getMedia() == int(estSel):
            jogoSel = jogo.getJogo() + "\n\n"
            self.limiteCons.textJogos.insert(1.0,jogoSel)
        self.limiteCons.textJogos.config(state = "disable")