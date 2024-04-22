import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from jogo import Jogo, JogoController






class ViewMain():
    def __init__(self, root, controle):
        self.root = root
        self.controle = controle
        self.root.title("Sistema de Jogos")
        self.root.geometry('700x700')
        self.root.config(bg="#3F0071")
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)  # Adicionando o menubar à janela principal
        self.cadastrarMenu = tk.Menu(self.menubar)
        self.avaliarMenu = tk.Menu(self.menubar)
        self.consultarMenu = tk.Menu(self.menubar)
        self.sairMenu=tk.Menu(self.menubar)

        self.menubar.add_cascade(label="Cadastrar", menu=self.cadastrarMenu)
        self.cadastrarMenu.add_command(label="Cadastrar Jogo", command=self.abrir_submenu_cadastrar)

        self.menubar.add_cascade(label="Avaliar", menu=self.avaliarMenu)
        self.avaliarMenu.add_command(label="Avaliar Jogo", command=self.abrir_submenu_avaliar)

        self.menubar.add_cascade(label="Consultar", menu=self.consultarMenu)
        self.consultarMenu.add_command(label="Consultar Jogo", command=self.abrir_submenu_consultar)
        
        self.menubar.add_cascade(label="Sair", menu=self.sairMenu)
        self.sairMenu.add_command(label="Salvar")

        
        
    def abrir_submenu_cadastrar(self):
        SubmenuCadastrar(self.root,self.controle)

    def abrir_submenu_avaliar(self):
        SubmenuAvaliar(self.root)

    def abrir_submenu_consultar(self):
        SubmenuConsultar(self.root)



class SubmenuCadastrar:
    def __init__(self, root,controle):
        self.root=root
        self.controle=controle
        self.janelaCadastro = tk.Toplevel(root)
        self.janelaCadastro.title("Cadastro de Jogo")
        self.janelaCadastro.geometry('400x400')
        self.janelaCadastro.config(bg="#ffff00")
       
        #cadastro do codigo 
        self.labelTitulo=tk.Label(self.janelaCadastro, text="Codigo", bg="#ffff00")
        self.labelTitulo.pack()

        self.entryCodigo=tk.Entry(self.janelaCadastro)
        self.entryCodigo.pack()
        
        #cadastro do titulo
        self.labelTitulo=tk.Label(self.janelaCadastro, text="Titulo", bg="#ffff00")
        self.labelTitulo.pack()        
        
        self.entryTitulo=tk.Entry(self.janelaCadastro)
        self.entryTitulo.pack()        
        
        #cadastro do console
        self.labelConsole=tk.Label(self.janelaCadastro, text="Console", bg="#ffff00")
        self.labelConsole.pack()
        
        self.entryConsole=tk.Entry(self.janelaCadastro)
        self.entryConsole.pack()

        #cadastro do genero
        self.labelGenero=tk.Label(self.janelaCadastro, text="Genero", bg="#ffff00")
        self.labelGenero.pack()
        
        self.entryGenero=tk.Entry(self.janelaCadastro)
        self.entryGenero.pack()
        
        #cadastro do preco
        self.labelPreco = tk.Label(self.janelaCadastro, text="Preço", bg="#ffff00")
        self.labelPreco.pack()

        self.entryPreco = tk.Entry(self.janelaCadastro)
        self.entryPreco.pack()       
         
        # Botão de cadastro
        self.botaoCadastrar = tk.Button(self.janelaCadastro, text="Cadastrar", bg="#3f0071", fg="white", command=self.cadastrarJogo)
        self.botaoCadastrar.pack()
        
        #botao clear
        self.buttonClear = tk.Button(self.janelaCadastro, text="Clear", command=self.clearHandler, bg="#3f0071", fg="white")
        self.buttonClear.pack()
        
    def cadastrarJogo(self):
        codigo = self.entryCodigo.get()
        titulo = self.entryTitulo.get()
        console = self.entryConsole.get()
        genero = self.entryGenero.get()
        preco = self.entryPreco.get()
        
        # Criando instancia de jogo, ou seja, criando um jogo
        jogo = Jogo(codigo,titulo,console,genero,preco)

        # Adicionando o jogo ao controle
        self.controle.cadastrarJogo(codigo, titulo,console, genero,preco)

        # Limpar os campos após o cadastro
        self.clearHandler()       

        
        
    def clearHandler(self):
        self.entryCodigo.delete(0, len(self.entryCodigo.get()))
        self.entryTitulo.delete(0, len(self.entryTitulo.get()))
        self.entryGenero.delete(0, len(self.entryGenero.get()))
        self.entryConsole.delete(0, len(self.entryConsole.get()))
        self.entryPreco.delete(0, len(self.entryPreco.get()))


        

class SubmenuAvaliar:
    def __init__(self, root):
        self.janelaAvaliar = tk.Toplevel(root)
        self.janelaAvaliar.title("Avaliação")
        self.janelaAvaliar.geometry('300x200')
        self.janelaAvaliar.config(bg="#ffff00")


class SubmenuConsultar:
    def __init__(self, root):
        self.janelaConsultar = tk.Toplevel(root)
        self.janelaConsultar.title("Consultar Jogo")
        self.janelaConsultar.geometry('300x200')
        self.janelaConsultar.config(bg="#ffff00")

class ControleView():
    def __init__(self):
        self.root = tk.Tk()
        self.controle = JogoController()  # Criando uma instância de JogoController
        self.view_main = ViewMain(self.root, self.controle)
        self.root.mainloop()

c = ControleView()
