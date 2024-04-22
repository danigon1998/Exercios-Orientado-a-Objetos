import tkinter as tk
import album as alb
import artista as art
import playlist as play

class LimitePrincipal():
  def __init__(self,root,controle):
    self.root = root
    self.root.geometry("300x250")
    self.controle = controle
    self.menubar = tk.Menu(self.root) 
    self.albumMenu = tk.Menu(self.menubar)
    self.artistaMenu = tk.Menu(self.menubar)
    self.playlistMenu = tk.Menu(self.menubar) 

    self.albumMenu.add_command(label = "Cadastrar", command = self.controle.insereAlbum)
    self.albumMenu.add_command(label = "Consultar", command = self.controle.consultaAlbum)
    self.menubar.add_cascade(label = "Album", menu = self.albumMenu)

    self.artistaMenu.add_command(label = "Cadastrar", command = self.controle.insereArtista)
    self.artistaMenu.add_command(label = "Consultar", command = self.controle.consultaArtista)
    self.menubar.add_cascade(label = "Artista", menu = self.artistaMenu)

    self.playlistMenu.add_command(label = "Cadastrar", command = self.controle.inserePlaylist)
    self.playlistMenu.add_command(label = "Consultar", command = self.controle.consultaPlaylist)
    self.menubar.add_cascade(label = "Playlist", menu = self.playlistMenu)

    self.root.config(menu = self.menubar)

class ControlePrincipal():
  def __init__(self):
    self.root = tk.Tk()

    self.ctrlAlbum = alb.CtrlAlbum(self)
    self.ctrlArtista = art.CtrlArtista(self)
    self.ctrlPlaylist = play.CtrlPlaylist(self)

    LimitePrincipal(self.root,self)

    self.root.title("Consulta Musical")

    self.root.mainloop()

  def insereAlbum(self):
      self.ctrlAlbum.insereAlbuns()

  def consultaAlbum(self):
      self.ctrlAlbum.consultaAlbum()

  def insereArtista(self):
      self.ctrlArtista.insereArtista()

  def consultaArtista(self):
      self.ctrlArtista.consultaArtista()

  def inserePlaylist(self):
      self.ctrlPlaylist.inserePlaylist()

  def consultaPlaylist(self):
      self.ctrlPlaylist.consultaPlaylist()

if __name__ == '__main__':
    ControlePrincipal()