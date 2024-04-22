from abc import ABC, abstractmethod

class transacoes:
  def __init__(self,data,valor,descricao):
    self.__data = data
    self.__valor = valor
    self.__descricao = descricao

  @property
  def data(self):
    return self.__data

  @property
  def valor(self):
    return self.__valor

  @valor.setter
  def valor(self,valor):
    self.__valor = valor

  @property
  def descricao(self):
    return self.__descricao

  @descricao.setter
  def descricao(self,des):
    self.__descricao = des

class Conta(ABC):
  def __init__(self,nConta,nomeCorrentista,saldo,lstTransacoes):
    self.__nConta = nConta
    self.__nomeCorrentista = nomeCorrentista
    self.__saldo = saldo
    self.__lstTransacoes = lstTransacoes
    
  @property
  def nConta(self):
    return self.__nConta

  @property
  def nomeCorrentista(self):
    return self.__nomeCorrentista

  @property
  def saldo(self):
    return self.__saldo

  @saldo.setter
  def novoSaldo(self,valor):
    self.__saldo = valor

  @property
  def lstTransacoes(self):
    return self.__lstTransacoes  
  
  def deposito(self,valor,transacao):
    transacao.valor = valor
    transacao.descricao = "deposito"
    self.__saldo = self.__saldo + valor
    self.__lstTransacoes.append(transacao)

  def retirar(self,valor,transacao):
    transacao.descricao = "retirada"
    if valor > self.__saldo:
      #O valor que quer ser retirado supera o saldo da conta, pelo qual vai ser retirado todo o saldo da conta
      transacao.valor = self.__saldo
      self.__saldo = 0
    else:
      transacao.valor = valor
      self.__saldo = self.__saldo - valor
    self.__lstTransacoes.append(transacao)  

  @abstractmethod
  def extrato(self):
    pass

class ContaComum(Conta):
  def __init__(self,nConta,nomeCorrentista,saldo,lstTransacoes):
    super().__init__(nConta,nomeCorrentista,saldo,lstTransacoes)
  def extrato(self):
    print("Nome: {}".format(self.nomeCorrentista))
    print("Numero de conta: {}".format(self.nConta))
    print("Saldo: {}".format(self.saldo))
    print("Transacoes realizadas")
    for tran in self.lstTransacoes:
      print("Valor:{} - Data:{} - Descricao:{} ".format(tran.valor,tran.data,tran.descricao))
    print()    

class ContaPoupanca(Conta):
  def __init__(self,nConta,nomeCorrentista,saldo,lstTransacoes,diaAniversario):
    super().__init__(nConta,nomeCorrentista,saldo,lstTransacoes)
    self.__diaAniversario = diaAniversario

  @property
  def diaAniversaio(self):
    return self.__diaAniversario
  
  def extrato(self):
    print("Nome: {}".format(self.nomeCorrentista))
    print("Numero de conta: {}".format(self.nConta))
    print("Saldo: {}".format(self.saldo))
    print("Dia Aniversario: {}".format(self.__diaAniversario))
    print("Transacoes realizadas")
    for tran in self.lstTransacoes:
      print("Valor:{} - Data:{} - Descricao:{} ".format(tran.valor,tran.data,tran.descricao))
    print()    

class ContaLimite(Conta):
  def __init__(self,nConta,nomeCorrentista,saldo,lstTransacoes,limite):
    super().__init__(nConta,nomeCorrentista,saldo,lstTransacoes)
    self.__limite = limite

  @property
  def limite(self):
    return self.__limite

  def retirar(self,valor,transacao):
    transacao.descricao = "retirada"
    if valor > (self.saldo + self.limite):
      # O valor que quer ser retirado supera o saldo da conta e o limite, pelo qual vai ser retirado todo o saldo da conta + o limite
      transacao.valor = self.saldo + self.limite
      self.novoSaldo = -self.limite
    else:
      transacao.valor = valor
      self.novoSaldo = self.saldo - valor
    self.lstTransacoes.append(transacao)  
  
  def extrato(self):
    print("Nome: {}".format(self.nomeCorrentista))
    print("Numero de conta: {}".format(self.nConta))
    print("Saldo: {}".format(self.saldo))
    print("Limite: {}".format(self.limite))
    print("Transacoes realizadas")
    for tran in self.lstTransacoes:
      print("Valor:{} - Data:{} - Descricao:{} ".format(tran.valor,tran.data,tran.descricao))
    print()  
      
if __name__ == "__main__":
  conta1 = ContaComum(100,"Pedro Diaz",2000,[])
  conta2 = ContaLimite(101,"Isabel Lara",3200,[],1000)
  conta3 = ContaPoupanca(102,"Felipe Souza",2000,[],10)
  transacao1 = transacoes("10/10/2022",0,"")
  transacao2 = transacoes("11/10/2022",0,"")
  transacao3 = transacoes("12/10/2022",0,"")
  conta1.deposito(500,transacao1)
  conta1.retirar(400,transacao2)
  conta1.deposito(200,transacao3)
  conta1.extrato()
  conta2.deposito(5000,transacao1)
  conta2.retirar(10000,transacao2)
  conta2.deposito(500,transacao3)
  conta2.extrato()
  conta3.deposito(1000,transacao1)
  conta3.retirar(3100,transacao2)
  conta3.deposito(200,transacao3)
  conta3.extrato()