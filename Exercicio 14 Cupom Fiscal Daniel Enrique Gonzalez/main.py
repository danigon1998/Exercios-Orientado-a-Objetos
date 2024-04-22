import tkinter as tk
import produto as pro
import cupomFiscal as cf


class LimitePrincipal:
  def __init__(self,root,controle):
    self.root = root
    self.root.geometry("300x250")
    self.controle = controle
    self.menubar = tk.Menu(self.root)
    self.produtoMenu = tk.Menu(self.menubar)
    self.cupomFiscalMenu = tk.Menu(self.menubar)
    self.sairMenu = tk.Menu(self.menubar)

    self.produtoMenu.add_command(label = "Cadastrar", command = self.controle.cadastraProduto)
    self.produtoMenu.add_command(label = "Consultar", command = self.controle.consultaProduto)
    self.menubar.add_cascade(label = "Produto", menu = self.produtoMenu)

    self.cupomFiscalMenu.add_command(label = "Cadastrar", command = self.controle.criaCupomFiscal)
    self.cupomFiscalMenu.add_command(label = "Consultar", command = self.controle.consultaCupomFiscal)
    self.menubar.add_cascade(label = "Cupom Fiscal", menu = self.cupomFiscalMenu)

    self.sairMenu.add_command(label="Salva",command=self.controle.salvaDados)
    self.menubar.add_cascade(label="Sair", menu=self.sairMenu)

    self.root.config(menu = self.menubar)

class ControlePrincipal:
  def __init__(self):
    self.root = tk.Tk()

    self.ctrlProduto = pro.CtrlProduto()
    self.ctrlCupomFiscal = cf.CtrlCupomFiscal(self)

    LimitePrincipal(self.root,self)

    self.root.title("Consulta Fiscal")

    self.root.mainloop()

  def cadastraProduto(self):
    self.ctrlProduto.cadastraProduto()

  def consultaProduto(self):
    self.ctrlProduto.consultaProduto()

  def criaCupomFiscal(self):
    self.ctrlCupomFiscal.criaCupomFiscal()

  def consultaCupomFiscal(self):
    self.ctrlCupomFiscal.consultaCupomFiscal()

  def salvaDados(self):
    self.ctrlProduto.salvaProduto()
    self.ctrlCupomFiscal.salvaCupomFiscal()
    self.root.destroy()


if __name__ == '__main__':
    ControlePrincipal()