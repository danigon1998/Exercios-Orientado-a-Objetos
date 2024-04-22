import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class ModelCliente():
    def __init__(self, nome, email,codigo):
        self.__nome = nome
        self.__email = email
        self.__codigo = codigo

    @property
    def nome(self):
        return self.__nome
    @property
    def email(self):
        return self.__email

    @property
    def codigo(self):
      return self.__codigo

class View():
    def __init__(self, master, controller):
        self.controller = controller
        self.janela = tk.Frame(master)
        self.janela.pack()
        self.frame1 = tk.Frame(self.janela)
        self.frame2 = tk.Frame(self.janela)
        self.frame3 = tk.Frame(self.janela)
        self.frame1.pack()
        self.frame2.pack()
        self.frame3.pack()
      
        self.labelInfo1 = tk.Label(self.frame1,text="Nome: ")
        self.labelInfo2 = tk.Label(self.frame2,text="Email: ")
        self.labelInfo3 = tk.Label(self.frame3,text="Código: ")
        self.labelInfo1.pack(padx = 3,side="left")
        self.labelInfo2.pack(padx = 4,side="left")
        self.labelInfo3.pack(padx = 0,side="left")

        self.inputText1 = tk.Entry(self.frame1, width=25)
        self.inputText1.pack(side="left")
        self.inputText2 = tk.Entry(self.frame2, width=25)
        self.inputText2.pack(side="left")        
        self.inputText3 = tk.Entry(self.frame3, width=25)
        self.inputText3.pack(side="left")     
      
        self.buttonSubmit = tk.Button(self.janela,text="Enter")      
        self.buttonSubmit.pack(side="left")
        self.buttonSubmit.bind("<Button>", controller.enterHandler)
      
        self.buttonClear = tk.Button(self.janela,text="Clear")      
        self.buttonClear.pack(side="left")
        self.buttonClear.bind("<Button>", controller.clearHandler)  

        # Ex2: Acrescentar o botão para listar os clientes cadastrados  

        self.buttonMostrarLista = tk.Button(self.janela, text = "Cliente cadastrado")
        self.buttonMostrarLista.pack(side = "left")
        self.buttonMostrarLista.bind("<Button>", controller.clientesHandler)

    def mostraJanela(self, titulo, mensagem):
        messagebox.showinfo(titulo, mensagem)
      
class Controller():       
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('300x100')
        self.listaClientes = []

        # Cria a view passando referência da janela principal e
        # de si próprio (controlador)
        self.view = View(self.root, self) 

        self.root.title("Exemplo MVC")
        # Inicia o mainloop
        self.root.mainloop()

    def enterHandler(self, event):
        nomeCli = self.view.inputText1.get().capitalize()
        emailCli = self.view.inputText2.get()
        codigoCli = self.view.inputText3.get()
        if(len(codigoCli) < 5):
          self.view.mostraJanela('Problema', 'Seu código tem que ter um mínimo de 5 caracteres')
        else:
          n = False
          for cli in self.listaClientes:
            if cli.codigo == codigoCli:
              n = True
              self.view.mostraJanela('Problema', 'Seu código não pode ser este, pois já foi usado por outra pessoa')
          if(n == False):    
            cliente = ModelCliente(nomeCli, emailCli,codigoCli)
            self.listaClientes.append(cliente)
            self.view.mostraJanela('Sucesso', 'Cliente cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.view.inputText1.delete(0, len(self.view.inputText1.get()))
        self.view.inputText2.delete(0, len(self.view.inputText2.get()))
        self.view.inputText3.delete(0, len(self.view.inputText3.get()))

    def clientesHandler(self,event):
        self.msg = "1"
        cod = simpledialog.askstring("Entrada","Qual é seu código?",parent = self.root)
        for x in self.listaClientes:
          if x.codigo == cod:
            self.msg = x.nome + ' - ' + x.email + '\n'
        if(self.msg != '1'):    
          self.view.mostraJanela('Dados do cliente',self.msg)  
        elif (self.msg == '1' and cod != None):
          self.view.mostraJanela('Dados do cliente',"Código não cadastrado")
if __name__ == '__main__':
    c = Controller()