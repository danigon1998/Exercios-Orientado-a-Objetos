import tkinter as tk
import jogo as jog

class LimitePrincipal():
    def __init__(self, root, controle):
        self.controle = controle
        self.root = root
        self.root.geometry('300x250')
        self.menubar = tk.Menu(self.root)        
        self.jogoMenu = tk.Menu(self.menubar)
        self.salvaMenu = tk.Menu(self.menubar)

        self.jogoMenu.add_command(label="Cadastrar", command=self.controle.cadastraJogo)
        self.jogoMenu.add_command(label="Avaliar", command=self.controle.avaliaJogo)
        self.jogoMenu.add_command(label="Consultar", command=self.controle.consultaJogo)
        self.menubar.add_cascade(label="Jogo", menu=self.jogoMenu)

        self.salvaMenu.add_command(label = "Salvar", command = self.controle.salvaJogo)
        self.menubar.add_cascade(label = "Salva", menu = self.salvaMenu)
               
        self.root.config(menu=self.menubar)

      
class ControlePrincipal():       
    def __init__(self):
        self.root = tk.Tk()

        self.ctrlJogo = jog.CtrlJogo(self)

        self.limite = LimitePrincipal(self.root, self) 

        self.root.title("Jogos")
        # Inicia o mainloop
        self.root.mainloop()
    
    def cadastraJogo(self):
        self.ctrlJogo.cadastraJogo()

    def avaliaJogo(self):
        self.ctrlJogo.avaliaJogo()
  
    def consultaJogo(self):
        self.ctrlJogo.consultaJogo()

    def salvaJogo(self):
        self.ctrlJogo.salvaJogo()
        self.root.destroy()


if __name__ == '__main__':
    c = ControlePrincipal()