import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

class Estudante:

    def __init__(self, nroMatric, nome):
        self.__nroMatric = nroMatric
        self.__nome = nome

    @property
    def nroMatric(self):
        return self.__nroMatric
    
    @property
    def nome(self):
        return self.__nome

class LimiteInsereEstudantes(tk.Toplevel):
    def __init__(self, controle):

        tk.Toplevel.__init__(self)
        self.geometry('250x100')
        self.title("Estudante")
        self.controle = controle

        self.frameNro = tk.Frame(self)
        self.frameNome = tk.Frame(self)
        self.frameButton = tk.Frame(self)
        self.frameNro.pack()
        self.frameNome.pack()
        self.frameButton.pack()
      
        self.labelNro = tk.Label(self.frameNro,text="Nro Matrícula: ")
        self.labelNome = tk.Label(self.frameNome,text="Nome: ")
        self.labelNro.pack(side="left")
        self.labelNome.pack(side="left")  

        self.inputNro = tk.Entry(self.frameNro, width=20)
        self.inputNro.pack(side="left")
        self.inputNome = tk.Entry(self.frameNome, width=20)
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

class LimiteMostraEstudantes():
    def __init__(self, str):
        messagebox.showinfo('Lista de alunos', str)
class LimiteConsultaEstudantes():
    def __init__(self,str):
        messagebox.showinfo('Aluno consultado',str)
      
class CtrlEstudante():       
    def __init__(self):
        self.listaEstudantes = [
            Estudante('1001', 'Joao Santos'),
            Estudante('1002', 'Marina Cintra'),
            Estudante('1003', 'Felipe Reis'),
            Estudante('1004', 'Ana Souza')
        ]

    def getEstudante(self, nroMatric):
        estRet = None
        for est in self.listaEstudantes:
            if est.nroMatric == nroMatric:
                estRet = est
        return estRet

    def getListaNroMatric(self):
        listaNro = []
        for est in self.listaEstudantes:
            listaNro.append(est.nroMatric)
        return listaNro

    def insereEstudantes(self):
        self.limiteIns = LimiteInsereEstudantes(self) 

    def mostraEstudantes(self):
        str = 'Nro Matric. -- Nome\n'
        for est in self.listaEstudantes:
            str += est.nroMatric + ' -- ' + est.nome + '\n'       
        self.limiteLista = LimiteMostraEstudantes(str)

    def consultaEstudantes(self):
        numM = simpledialog.askstring("Número de matricula","Qual é o número de matrícula")
        str = 0
        for n in self.listaEstudantes:
          if n.nroMatric == numM:
            str = 'Nome -- Nro Matric.\n'
            str += n.nome + ' - ' + n.nroMatric
        if str == 0:
          str = 'O número de matricula não existe'
        if numM != None:
          LimiteConsultaEstudantes(str)
  
    def enterHandler(self, event):
        nroMatric = self.limiteIns.inputNro.get()
        nome = self.limiteIns.inputNome.get()
        estudante = Estudante(nroMatric, nome)
        self.listaEstudantes.append(estudante)
        self.limiteIns.mostraJanela('Sucesso', 'Estudante cadastrado com sucesso')
        self.clearHandler(event)

    def clearHandler(self, event):
        self.limiteIns.inputNro.delete(0, len(self.limiteIns.inputNro.get()))
        self.limiteIns.inputNome.delete(0, len(self.limiteIns.inputNome.get()))

    def fechaHandler(self, event):
        self.limiteIns.destroy()