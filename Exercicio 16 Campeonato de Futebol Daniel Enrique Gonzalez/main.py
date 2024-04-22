import tkinter as tk
import equipe as equi

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.equipeMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        self.equipeMenu.add_command(label="Cadastrar", command=self.controle.cadastraEquipe)
        self.equipeMenu.add_command(label="Consultar", command=self.controle.consultaEquipe)
        self.equipeMenu.add_command(label="Imprimir Dados", command=self.controle.imprimeEquipe)
        self.menubar.add_cascade(label="Equipes", menu=self.equipeMenu)

        self.salvaMenu.add_command(label = "Salvar", command = self.controle.salvaEquipe)
        self.menubar.add_cascade(label = "Salva", menu = self.salvaMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlEquipe = equi.CtrlEquipe(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Equipes")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraEquipe(self):
        self.ctrlEquipe.cadastraEquipe()

    def consultaEquipe(self):
        self.ctrlEquipe.consultaEquipe()
  
    def imprimeEquipe(self):
        self.ctrlEquipe.imprimeEquipe()

    def salvaEquipe(self):
        self.ctrlEquipe.salvaEquipe()
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()