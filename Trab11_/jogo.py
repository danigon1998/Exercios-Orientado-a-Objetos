import pickle,os,math
from tkinter import messagebox
class Jogo:
    def __init__(self,codigo,titulo,console,genero,preco):
        self.resenha=[]
        self.codigo=codigo
        self.titulo=titulo
        self.console=console
        self.genero=genero
        self.preco=preco
        
    @property
    def resenha(self):
        return self.__resenha
    
    @property
    def codigo(self):
        return self.__codigo
    
    @property
    def titulo(self):
        return self.__titulo
       
    @property
    def console(self):
        return self.__console
    
    @property
    def genero(self):
        return self.__genero
    
    @property
    def preco(self):
        return self.__preco
    
    @resenha.setter
    def resenha(self, value):
        self.__resenha = value

    @codigo.setter
    def codigo(self, value):
        self.__codigo = value
        
    @titulo.setter
    def titulo(self, value):
        self.__titulo = value
    #validação console
    @console.setter
    def console(self,console):
        consoles=["Xbox","PlayStation","Switch","PC"]
        if console not in consoles:
            raise ValueError("Erro: Console inválido. Escolha entre: {}".format(consoles))
        
        else:
            self.__console=console         
             
    #validação genero
    @genero.setter
    def genero(self,genero):
        generos=["Ação","Aventura","Estratégia","RPG","Esporte","Simulação"]
        if genero not in generos:
            raise ValueError("Erro: Gênero inválido. Escolha entre: {}".format(generos))
        
        else:
            self.__genero=genero
    
    #validação preço
    @preco.setter
    def preco(self,preco):
        preco=int(preco)
        if (preco < 0 or preco>500):
            raise ValueError("Valor Invalido")
        
        else:
            self.__preco=preco


    def listarJogos(self):
        for jogo in self.lista_jogos:
            print(jogo)


class JogoController:
    def __init__(self):
        self.lista_jogos = []  #inicializar a lista de jogos

    def cadastrarJogo(self, codigo, titulo, console, genero, preco):
        try:
            jogo = Jogo(codigo, titulo, console, genero, preco)
            self.lista_jogos.append(jogo)
            
            messagebox.showinfo("Cadastro bem-sucedido", "Jogo cadastrado com sucesso!")

        except ValueError as e:
            messagebox.showerror("Erro no cadastro", str(e))
            
    def listarJogos(self):
        if not self.lista_jogos:
            messagebox.showinfo("Lista de Jogos", "Nenhum jogo cadastrado.")
            return

        for jogo in self.lista_jogos:
            print(jogo.codigo, jogo.titulo, jogo.console, jogo.genero, jogo.preco)