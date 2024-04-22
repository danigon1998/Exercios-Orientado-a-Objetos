import tkinter as tk
from tkinter import ttk
import album as alb
import artista as art
import musica as mus
from tkinter import simpledialog
from tkinter import messagebox

class Playlist:
    def __init__(self, nome):
        self.__nome = nome

        self.__musicas = []

    @property
    def nome(self):
        return self.__nome

    @property
    def musicas(self):
        return self.__musicas

    def addMusica(self, musica):
        self.__musicas.append(musica)

class LimiteInserePlaylist(tk.Toplevel):
  def __init__(self, controle,listaNomes):
    tk.Toplevel.__init__(self)
    self.geometry('300x250')
    self.title("Playlist")
    self.controle = controle

    self.frameNome = tk.Frame(self)
    self.frameArtista = tk.Frame(self)
    self.frameMusica = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNome.pack()
    self.frameArtista.pack()
    self.frameMusica.pack()
    self.frameButton.pack()

    self.labelNome = tk.Label(self.frameNome, text = "Nome da Playlist: ")
    self.labelArtista = tk.Label(self.frameArtista, text = "Selecione um Artista: ")
    self.labelMusica = tk.Label(self.frameMusica, text = "Escolha a Música: ")
    self.labelNome.pack(side = "left")
    self.labelArtista.pack(side = "left")
    self.labelMusica.pack(side = "left")

    self.inputNome = tk.Entry(self.frameNome, width = 20)
    self.inputNome.pack(side = "left")
    
    self.escolhaArtista = tk.StringVar()
    self.comboBoxArtista = ttk.Combobox(self.frameArtista,width = 15,textvariable = self.escolhaArtista)
    self.comboBoxArtista.pack(side = "left")
    self.comboBoxArtista['values'] = listaNomes
    self.comboBoxArtista.bind("<<ComboboxSelected>>",controle.colocaHandler)

    self.listBoxMusicas = tk.Listbox(self.frameMusica)
    self.listBoxMusicas.pack(side = "left")

    self.scrollbar = tk.Scrollbar(self.frameMusica)
    self.scrollbar.pack(side = "right",fill = "both")

    self.listBoxMusicas.config(yscrollcommand = self.scrollbar.set)
    self.scrollbar.config(command = self.listBoxMusicas.yview)
    
    self.buttonInsere = tk.Button(self.frameButton ,text="Insere Música")           
    self.buttonInsere.pack(side="left")
    self.buttonInsere.bind("<Button>", controle.insereHandler)

    self.buttonCria = tk.Button(self.frameButton ,text="Cria Playlist")           
    self.buttonCria.pack(side="left")
    self.buttonCria.bind("<Button>", controle.criaHandler)    

  def mostraJanela(self, titulo, msg):
    messagebox.showinfo(titulo, msg) 

class LimiteConsultaPlaylist:
  def __init__(self,str):
        messagebox.showinfo('Playlist Consultada',str)

class CtrlPlaylist:
  def __init__(self, controlePrincipal):
    self.ctrlPrincipal = controlePrincipal
    self.listaPlaylists = []


  def getMusica(self,artista,musica):
    for mu in artista.musicas:
      if musica == mu.titulo:
        return mu
        
  def inserePlaylist(self):
    self.listaMusicasPlaylist = []
    listaNomes = self.ctrlPrincipal.ctrlArtista.getNomes()
    self.limiteIns = LimiteInserePlaylist(self,listaNomes)

  def colocaHandler(self,event):
    self.limiteIns.listBoxMusicas.delete(0,tk.END)
    listaArtistas = self.ctrlPrincipal.ctrlArtista.getListaArtistas()
    for a in listaArtistas:
      if self.limiteIns.escolhaArtista.get() == a.nome:
        for m in a.musicas:
          self.limiteIns.listBoxMusicas.insert(tk.END, m.titulo)
  
  def insereHandler(self,event):
    artSel = self.limiteIns.escolhaArtista.get()
    musicaSel = self.limiteIns.listBoxMusicas.get(tk.ACTIVE)
    artSel = self.ctrlPrincipal.ctrlArtista.getArtista(artSel)
    musica = self.getMusica(artSel,musicaSel)
    if musica not in self.listaMusicasPlaylist:
      self.listaMusicasPlaylist.append(musica)
      self.limiteIns.mostraJanela('Sucesso', 'Música colocada na lista')
      self.limiteIns.listBoxMusicas.delete(tk.ACTIVE)
    else:
      self.limiteIns.mostraJanela('Problema', 'Música já na lista')

  def criaHandler(self,event):
    nome = self.limiteIns.inputNome.get().capitalize()
    
    playlist = Playlist(nome)
    for x in self.listaMusicasPlaylist:
      playlist.addMusica(x)
    if len(nome) > 0 and len(self.listaMusicasPlaylist) > 0:
      self.listaPlaylists.append(playlist)
      self.limiteIns.mostraJanela('Sucesso', 'Playlist criada com sucesso')
      self.limiteIns.destroy()
    elif len(nome) < 1:
      self.limiteIns.mostraJanela('Problema', 'Playlist sem nome')
    elif len(self.listaMusicasPlaylist) == 0:
      self.limiteIns.mostraJanela('Problema', 'Playlist sem músicas')
    
  def consultaPlaylist(self):
    nome = simpledialog.askstring("Playlist","Qual é o nome da playlist?").capitalize()
    str = ''
    s = 0
    for n in self.listaPlaylists:
      if n.nome == nome:
        s = 1
        str+= "Titulo - Artista - Album\n"
        for can in n.musicas:
          str += can.titulo + "-" + can.artista.nome + "-" + can.album.titulo + '\n'
        
    if s == 0:
        str = 'Não existem playlists com esse nome'
    if nome != None:
      LimiteConsultaPlaylist(str)
    