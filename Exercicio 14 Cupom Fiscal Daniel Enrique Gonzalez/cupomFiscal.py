import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import simpledialog
import os.path
import pickle

class CupomFiscal:
  def __init__(self,nroCupom):
    self.__nroCupom = nroCupom
    self.__itensCupom = []

  @property
  def nroCupom(self):
    return self.__nroCupom

  @property
  def itensCupom(self):
    return self.__itensCupom

  def addProdutos(self,lst):
    self.__itensCupom = lst

class LimiteCriarCupom(tk.Toplevel):
  def __init__(self,controle,listaProdutos):

    tk.Toplevel.__init__(self)
    self.geometry("350x150")
    self.title("Cupom Fiscal")
    self.controle = controle

    self.frameNro = tk.Frame(self)
    self.frameProdutos = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameNro.pack()
    self.frameProdutos.pack()
    self.frameButton.pack()

    self.labelNro = tk.Label(self.frameNro,text = "Nro cupom: ")
    self.labelProdutos = tk.Label(self.frameProdutos, text = "Selecione um produto: ")
    self.labelNro.pack(side = "left")
    self.labelProdutos.pack(side = "left")

    self.inputNro = tk.Entry(self.frameNro,width = 20)
    self.inputNro.pack(side = "left")

    self.escolhaProduto = tk.StringVar()
    self.comboBox = ttk.Combobox(self.frameProdutos,width = 20,textvariable = self.escolhaProduto)
    self.comboBox.pack(side = "left")
    self.comboBox['values'] = listaProdutos
    

    self.buttonAgregar = tk.Button(self.frameButton, text = "Agregar")
    self.buttonAgregar.pack(side = "left")
    self.buttonAgregar.bind("<Button>",controle.enterHandler)

    self.buttonConcluido = tk.Button(self.frameButton, text = "Fechar Cupom")
    self.buttonConcluido.pack(side = "left")
    self.buttonConcluido.bind("<Button>",controle.concluidoHandler)

  def mostraJanela(self,titulo,str):
    messagebox.showinfo(titulo,str)


class LimiteConsultaCupomFiscal:
  def __init__(self,str):
    messagebox.showinfo("Produto",str)

class CtrlCupomFiscal:
  def __init__(self,controlePrincipal):
    self.ctrlPrincipal = controlePrincipal
    if not os.path.isfile("cupomFiscal.pickle"):
      self.listaCuponsFiscais = []

    else:
      with open("cupomFiscal.pickle","rb") as f:
        self.listaCuponsFiscais = pickle.load(f)

  def salvaCupomFiscal(self):
    if len(self.listaCuponsFiscais) != 0:
      with open("cupomFiscal.pickle", "wb") as f:
        pickle.dump(self.listaCuponsFiscais,f)
  
  def getListaCuponsFiscais(self):
    return self.listaCuponsFiscais

  def criaCupomFiscal(self):
    self.listaProdutosCupomAtual = []
    listaProdutos = self.ctrlPrincipal.ctrlProduto.getNomesProdutos()
    self.criaCF = LimiteCriarCupom(self,listaProdutos)

  def consultaCupomFiscal(self):
    s = 0
    codigo = simpledialog.askstring("Código","Escreva o número do cupom fiscal")
    for c in self.listaCuponsFiscais:
      if c.nroCupom == codigo:
        T = 0
        s = 1
        sb = "Código - Descricao - Valor Unitario\n"
        produtosCodigos = []
        produtoJaCadastrado = []
        for p in c.itensCupom:
          produtosCodigos.append(p.codigo)
        for p in c.itensCupom:
          if p.codigo not in produtoJaCadastrado:
            produtoJaCadastrado.append(p.codigo)
            sb += p.codigo + "-" + p.descricao + "-" + str(p.valorUnitario) + "X" + str(produtosCodigos.count(p.codigo)) + "\n"
            T += p.valorUnitario * produtosCodigos.count(p.codigo)
        sb+= "O valor total da compra é " + str(T) + "R$"  
    if s == 0:
      sb = "Não existem produtos com esse código"
    if codigo != None:
      LimiteConsultaCupomFiscal(sb)

  def enterHandler(self,event):
    s = 0
    produto = self.criaCF.escolhaProduto.get()
    for pro in self.ctrlPrincipal.ctrlProduto.getListaProdutos():
      if produto == pro.descricao:
        s = 1
        self.listaProdutosCupomAtual.append(pro)
        self.criaCF.mostraJanela("Sucesso","Produto agregado no cupom fiscal")
    if s == 0:
      self.criaCF.mostraJanela("Problema","Não esta sendo selecionado nenhum produto")


  def concluidoHandler(self,event):
    cupomFiscal = CupomFiscal(self.criaCF.inputNro.get())
    if len(self.criaCF.inputNro.get()) and len(self.listaProdutosCupomAtual):
      cupomFiscal.addProdutos(self.listaProdutosCupomAtual)
      self.listaCuponsFiscais.append(cupomFiscal)
    self.criaCF.destroy()
  