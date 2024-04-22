import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import musica as mus
import artista as art

class Album:
    def __init__(self, titulo, artista, ano):
        self.__titulo = titulo
        self.__artista = artista
        self.__ano = ano

        self.__faixas = []
        artista.addAlbum(self)

    @property
    def titulo(self):
        return self.__titulo

    @property
    def artista(self):
        return self.__artista

    @property
    def ano(self):
        return self.__ano

    @property
    def faixas(self):
        return self.__faixas

    def addFaixa(self, titulo, artista=None):
        if artista is None:
          artista = self.artista
        else:
          artista.addAlbum(self)
        nroFaixa = len(self.__faixas)
        musica = mus.Musica(titulo, artista, self, nroFaixa)
        self.__faixas.append(musica)

class LimiteInsereAlbum(tk.Toplevel):
  def __init__(self,controle):

    tk.Toplevel.__init__(self)
    self.geometry('350x150')
    self.title("Album")
    self.controle = controle

    self.frameTitulo = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameAno = tk.Frame(self)
    self.frameMusica = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameTitulo.pack()
    self.frameArtista.pack()
    self.frameAno.pack()
    self.frameMusica.pack()
    self.frameButton.pack()

    self.labelTitulo = tk.Label(self.frameTitulo,text = "Titulo: ")
    self.labelArtista = tk.Label(self.frameArtista,text = "Artista: ")
    self.labelAno = tk.Label(self.frameAno, text = "Ano: ")
    self.labelMusica = tk.Label(self.frameMusica,text = "Musica: ")
    self.labelTitulo.pack(padx = 6,side = "left")
    self.labelArtista.pack(padx = 3,side = "left")
    self.labelAno.pack(padx = 11,side = "left")
    self.labelMusica.pack(padx = 2,side = "left")

    self.inputTitulo = tk.Entry(self.frameTitulo, width = 25)
    self.inputArtista = tk.Entry(self.frameArtista, width = 25)
    self.inputAno = tk.Entry(self.frameAno, width = 25)
    self.inputMusica = tk.Entry(self.frameMusica, width = 25)
    self.inputTitulo.pack(side = "left")
    self.inputArtista.pack(side = "left")
    self.inputAno.pack(side = "left")
    self.inputMusica.pack(side = "left")

    self.buttonSubmit = tk.Button(self.frameButton, text = "Enter")
    self.buttonSubmit.pack(side = "left")
    self.buttonSubmit.bind("<Button>", controle.enterHandler)

    self.buttonClear = tk.Button(self.frameButton, text = "Clear")
    self.buttonClear.pack(side = "left")
    self.buttonClear.bind("<Button>", controle.clearHandler)

    self.buttonMusica = tk.Button(self.frameButton, text = "Agregar Música")
    self.buttonMusica.pack(side = "left")
    self.buttonMusica.bind("<Button>", controle.agregarMusicaHandler)
    
    self.buttonConcluido = tk.Button(self.frameButton, text = "Concluido")
    self.buttonConcluido.pack(side = "left")
    self.buttonConcluido.bind("<Button>", controle.concluidoHandler)

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg)

class LimiteConsultaAlbuns():
    def __init__(self, str):
        messagebox.showinfo('Lista de Albuns', str)

class CtrlAlbum():
  def __init__(self,controlePrincipal):
    self.ctrlPrincipal = controlePrincipal
    self.listaAlbuns = []
    self.contador = 0
    self.tipoAlbum = 1

  def getListaAlbuns(self):
    return self.listaAlbuns

  def insereAlbuns(self):
    self.limiteInserir = LimiteInsereAlbum(self)

  def consultaAlbum(self):
    s = 0
    nome = simpledialog.askstring("Album","Escreva o nome do album").capitalize()
    
    for alb in self.listaAlbuns:
      if alb.titulo == nome:
        s = 1
        str = "Título---Artista---Ano\n"
        str += alb.titulo + "-" + alb.artista.nome + "-" + alb.ano + "\n"
        str += "Músicas\n"
        for m in alb.faixas:
          str += m.titulo + "\n"
    if s == 0:
        str = 'Não existem albuns com esse nome'
    if nome != None:   
        LimiteConsultaAlbuns(str)
  
  def enterHandler(self,event):
    s = 0
    titulo = self.limiteInserir.inputTitulo.get().capitalize()
    artista = self.limiteInserir.inputArtista.get().capitalize()
    ano = self.limiteInserir.inputAno.get()
    if len(titulo) and len(artista) and len(ano):
      for x in self.ctrlPrincipal.ctrlArtista.getListaArtistas():
        if x.nome == artista:
          artista = x
          s = 1
          break
      if s == 0 :
        artista = art.Artista(artista)
        if self.limiteInserir.inputArtista.get().capitalize() != "Varios artistas":
          self.ctrlPrincipal.ctrlArtista.getListaArtistas().append(artista)
      for alb in self.listaAlbuns:
        if alb.titulo == titulo and self.limiteInserir.inputArtista.get().capitalize() == alb.artista.nome:
          s = 2
      if s != 2:
        album = Album(titulo,artista,ano)
        self.listaAlbuns.append(album)
        self.limiteInserir.mostraJanela('Sucesso', 'Album cadastrado com sucesso')
        self.contador += 1
      elif s == 2:
        self.limiteInserir.mostraJanela('Problema', 'Album já cadastrado')
      
      if self.limiteInserir.inputArtista.get().capitalize() == "Varios artistas":
        self.limiteInserir.inputArtista.delete(0,len( self.limiteInserir.inputArtista.get()))
        self.tipoAlbum = 2
    else:
      self.limiteInserir.mostraJanela('Problema', 'Tem campos que não estão prenchidos')
   
  def clearHandler(self,event):
    self.limiteInserir.inputTitulo.delete(0,len(self.limiteInserir.inputTitulo.get()))
    self.limiteInserir.inputArtista.delete(0,len( self.limiteInserir.inputArtista.get()))
    self.limiteInserir.inputAno.delete(0,len(self.limiteInserir.inputAno.get()))


  def agregarMusicaHandler(self,event):
    if len(self.listaAlbuns) == 0:
      messagebox.showinfo('Problema','Não existe nenhum album cadastrado')

    elif len(self.limiteInserir.inputMusica.get()) > 0 and self.tipoAlbum == 1:
      self.listaAlbuns[self.contador-1].addFaixa(self.limiteInserir.inputMusica.get().capitalize())
      messagebox.showinfo('Sucesso','Música cadastrada com sucesso')
      self.limiteInserir.inputMusica.delete(0,len(self.limiteInserir.inputMusica.get()))

    elif len(self.limiteInserir.inputMusica.get()) and self.tipoAlbum == 2 and len(self.limiteInserir.inputArtista.get()):
      artista = self.limiteInserir.inputArtista.get().capitalize()
      artista = art.Artista(artista)
      self.ctrlPrincipal.ctrlArtista.getListaArtistas().append(artista)
      self.listaAlbuns[self.contador-1].addFaixa(self.limiteInserir.inputMusica.get().capitalize(),artista)
      messagebox.showinfo('Sucesso','Música cadastrada com sucesso')
      self.limiteInserir.inputMusica.delete(0,len(self.limiteInserir.inputMusica.get()))
      self.limiteInserir.inputArtista.delete(0,len(self.limiteInserir.inputArtista.get()))

    else:
      messagebox.showinfo('Problema','Tem campos que não estão prenchidos')
    
  def concluidoHandler(self, event):
        self.limiteInserir.destroy()