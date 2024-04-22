import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Artista:
    def __init__(self, nome):
        self.__nome = nome

        self.__albuns = []
        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def albuns(self):
        return self.__albuns

    @property
    def musicas(self):
        return self.__musicas

    def addAlbum(self, album):
        self.__albuns.append(album)

    def addMusica(self, musica):
        self.__musicas.append(musica)

class LimiteInsereArtista(tk.Toplevel):
  def __init__(self,controle):

    tk.Toplevel.__init__(self)
    self.geometry('350x100')
    self.title("Artista")
    self.controle = controle

    self.frameNome = tk.Frame(self)
    self.frameNome.pack()
    self.frameButton = tk.Frame(self)
    self.frameButton.pack()

    self.labelNome = tk.Label(self.frameNome,text="Nome: ")
    self.labelNome.pack(side="left")

    self.inputNome = tk.Entry(self.frameNome, width=25)
    self.inputNome.pack(side="left")    

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

class LimiteConsultaArtistas():
  def __init__(self,str):
    messagebox.showinfo('Artista consultada',str)

class CtrlArtista():
  def __init__(self,controlePrincipal):
    self.ctrlPrincipal = controlePrincipal
    self.listaArtistas = []

  def getListaArtistas(self):
    return self.listaArtistas

  def getArtista(self,nome):
    for art in self.listaArtistas:
      if nome == art.nome:
        return art

  def getNomes(self):
    nomes = []
    for n in self.listaArtistas:
      nomes.append(n.nome)
    return nomes

  def artistaCadastrado(self,nome,E):
    for x in self.listaArtistas:
      if nome == x.nome:
        E = True
        self.limiteInsereArt.mostraJanela("Problema","O artista já foi cadastrado")
    return E
    
  def insereArtista(self):
    self.limiteInsereArt = LimiteInsereArtista(self)

  def consultaArtista(self):
    nome = simpledialog.askstring("Artista","Escreva o nome do artista").capitalize()
    str = ''
    s = 0
    for art in self.listaArtistas:
      if nome == art.nome:
        s = 1
        str += art.nome + "\n"
        for a in art.albuns:
          str += "Album\n"
          str += a.titulo + "\n"
          str += "Músicas\n"
          for m in a.faixas:
            if m.artista.nome == nome:
              str += m.titulo + "\n"
          str += "---------\n"
    if s == 0:
        str = 'Não existem artistas com esse nome'
    if nome != None:
      LimiteConsultaArtistas(str)

  def enterHandler(self,event):
    E = False
    nome = self.limiteInsereArt.inputNome.get().capitalize()
    
    if self.artistaCadastrado(nome,E) == False:
      artista = Artista(nome)
      for a in self.ctrlPrincipal.ctrlAlbum.getListaAlbuns():
        if a.artista == nome:
          artista.addAlbum(a)
          for m in a.faixas:
            artista.addMusica(m)
      self.listaArtistas.append(artista)
      self.limiteInsereArt.mostraJanela("Sucesso","O artista foi cadastrado com sucesso")
    self.clearHandler(event)

  def clearHandler(self,event):
    self.limiteInsereArt.inputNome.delete(0,len(self.limiteInsereArt.inputNome.get()))

  def fechaHandler(self, event):
        self.limiteInsereArt.destroy()