import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import os.path
import pickle

class Produto:
  def __init__(self,codigo,descricao,valorUnitario):
    self.__codigo = codigo
    self.__descricao = descricao
    self.__valorUnitario = valorUnitario

  @property
  def codigo(self):
    return self.__codigo

  @property
  def descricao(self):
    return self.__descricao

  @property
  def valorUnitario(self):
    return self.__valorUnitario


class LimiteCadastraProduto(tk.Toplevel):
  def __init__(self,controle):

    tk.Toplevel.__init__(self)
    self.geometry("350x150")
    self.title("Produto")
    self.controle = controle

    self.frameCodigo = tk.Frame(self)
    self.frameDescricao = tk.Frame(self)
    self.frameValorUnitario = tk.Frame(self)
    self.frameButton = tk.Frame(self)
    self.frameCodigo.pack()
    self.frameDescricao.pack()
    self.frameValorUnitario.pack()
    self.frameButton.pack()

    self.labelCodigo = tk.Label(self.frameCodigo,text = "Codigo:")
    self.labelDescricao = tk.Label(self.frameDescricao, text = "Descricão: ")
    self.labelValorUnitario = tk.Label(self.frameValorUnitario, text = "Valor Unitario: ")
    self.labelCodigo.pack(side = "left", padx=21)
    self.labelDescricao.pack(side = "left", padx=10)
    self.labelValorUnitario.pack(side = "left")

    self.inputCodigo = tk.Entry(self.frameCodigo,width = 20)
    self.inputDescricao = tk.Entry(self.frameDescricao,width = 20)
    self.inputValorUnitario = tk.Entry(self.frameValorUnitario,width = 20)
    self.inputCodigo.pack(side = "left")
    self.inputDescricao.pack(side = "left")
    self.inputValorUnitario.pack(side = "left")

    self.buttonSubmit = tk.Button(self.frameButton, text = "Enter")
    self.buttonSubmit.pack(side = "left")
    self.buttonSubmit.bind("<Button>",controle.enterHandler)

    self.buttonClear = tk.Button(self.frameButton, text = "Clear")
    self.buttonClear.pack(side = "left")
    self.buttonClear.bind("<Button>",controle.clearHandler)

    self.buttonConcluido = tk.Button(self.frameButton, text = "Concluido")
    self.buttonConcluido.pack(side = "left")
    self.buttonConcluido.bind("<Button>",controle.concluidoHandler)

  def mostraJanela(self,titulo,str):
    messagebox.showinfo(titulo,str)


class LimiteConsultaProduto:
  def __init__(self,str):
    messagebox.showinfo("Produto",str)

class CtrlProduto:
  def __init__(self):
    if not os.path.isfile("produto.pickle"):
      self.listaProdutos = []
    else:
      with open("produto.pickle","rb") as f:
        self.listaProdutos = pickle.load(f)

  def salvaProduto(self):
    if len(self.listaProdutos) != 0:
      with open("produto.pickle","wb") as f:
          pickle.dump(self.listaProdutos, f)

  def getListaProdutos(self):
    return self.listaProdutos

  def getNomesProdutos(self):
    self.listaNomes = []
    for x in self.listaProdutos:
      self.listaNomes.append(x.descricao)
    return self.listaNomes

  def cadastraProduto(self):
    self.cadProduto = LimiteCadastraProduto(self)

  def consultaProduto(self):
    s = 0
    codigo = simpledialog.askstring("Código","Escreva o código do produto")
    for prd in self.listaProdutos:
      if prd.codigo == codigo:
        s = 1
        sb = "Descricao - Valor Unitario\n"
        sb += prd.descricao + "-" + str(prd.valorUnitario)
    if s == 0:
      sb = "Não existem produtos com esse código"
    if codigo != None:
      LimiteConsultaProduto(sb)

  def enterHandler(self,event):
    s = 0
    codigo = self.cadProduto.inputCodigo.get()
    descricao = self.cadProduto.inputDescricao.get()
    valorUnitario = self.cadProduto.inputValorUnitario.get()
    if len(codigo) and len(descricao) and len(valorUnitario) and codigo.isnumeric():
      try:
        produto = Produto(codigo,descricao,float(valorUnitario))
      except:
        self.cadProduto.mostraJanela("Erro","O valor unitario esta errado")
        s = 2
      for x in self.listaProdutos:
        if x.codigo == codigo:
          s = 1
      if s == 0:
        self.listaProdutos.append(produto)
        self.cadProduto.mostraJanela("Sucesso","Produto cadastrado com sucesso")
        self.clearHandler(event)
      elif s == 1:
        self.cadProduto.mostraJanela("Problema","Este produto já foi cadastrado")
    else:
      self.cadProduto.mostraJanela("Problema","Tem campo que não foi prenchido ou o código não é um valor inteiro")

  def clearHandler(self,event):
    self.cadProduto.inputCodigo.delete(0,len(self.cadProduto.inputCodigo.get()))
    self.cadProduto.inputDescricao.delete(0,len(self.cadProduto.inputDescricao.get()))
    self.cadProduto.inputValorUnitario.delete(0,len(self.cadProduto.inputValorUnitario.get()))

  def concluidoHandler(self,event):
    self.cadProduto.destroy()