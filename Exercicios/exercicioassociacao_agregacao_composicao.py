# Crie as classes Pessoa e Livro e demonstre uma relação de associação entre eles.
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade  
        
class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor      
    def consultalivro(self,pessoa:Pessoa):
        print(f"Oª {pessoa.nome} está consultando o livro {self.titulo} que foi escrito pelo autor {self.autor}")
             
pessoa=Pessoa("Juliana",31)
livro=Livro("O Senhor dos Aneis","JRR Tolkien")
livro.consultalivro(pessoa)        

# Crie as classes Aluno e Onibus. Crie um método em Aluno que use a classe Onibus.

class Onibus: 
    def __init__(self,numero):
        self.numero=numero
class Aluno():
    def __init__(self,nome,matricula):
        self.nome=nome
        self.matricula=matricula
    def embarcar(self,onibus:Onibus):
        print(f"Oª aluno {self.nome} de matricula {self.matricula} embarcou no onibus{onibus.numero}")      
   
onibus=Onibus(1)
aluno=Aluno("Juliana",3105)
aluno.embarcar(onibus)

# Crie uma classe Funcionario e Departamento que contém uma lista de Funcionarios.
# Departamento deve agregar funcionários já criados.

class Funcionario():
    def __init__(self,nome,matricula,salario):
        self.nome=nome
        self.matricula=matricula
        self.salario=salario
    def __str__(self):
        return f"O funcionario:{self.nome} tem matricula:{self.matricula} e salario:{self.salario}"    
class Departamento():
    def __init__(self,nome):
        self.nome=nome
        self.funcionarios=[]
      
    def adicionar_funcionario(self,funcionario:Funcionario):
        self.funcionarios.append(funcionario)
    def __str__(self):
        nomes_funcionarios = ", ".join([f.nome for f in self.funcionarios])
        return f"O departamento:{self.nome} tem {len(self.funcionarios)} funcionarios." 
       
funcionario01=Funcionario("Juliana",3105,5000)
funcionario02=Funcionario("Antonio",3206,5000)
departamento=Departamento("TI")
departamento.adicionar_funcionario(funcionario01)  
departamento.adicionar_funcionario(funcionario02)  
for funcionario in departamento.funcionarios:
    print(funcionario)
print(departamento)
            
# Crie as classes Time e Jogador. 
# Um Jogador tem nome e posição como atributos, enquanto Time agrega jogadores em uma lista.
class Jogador():
    def __init__(self,nome,posicao):
        self.nome=nome
        self.posicao=posicao
    def __str__(self):
        return f"O jogador:{self.nome} tem a posicao:{self.posicao}"    
class Time():
    def __init__(self, nome):
        self.nome=nome
        self.jogadores=[]
    def adicionar_jogador(self,jogador):
        self.jogadores.append(jogador)
    def __str__(self):
        nomes_jogadores = ", ".join([f.nome for f in self.jogadores])
        return f"O time:{self.nome} tem {len(self.jogadores)} jogadores."
    
jogador01= Jogador("Juliana","Atacante")
jogador02= Jogador("Antonio","Atacante")
time=Time("Flamengo")
time.adicionar_jogador(jogador01)
time.adicionar_jogador(jogador02)
for jogador in time.jogadores:
    print(jogador)
print(time)    
        
        
#Crie a classe Carro que possui um Motor. O Motor deve ser criado dentro do Carro. 
#Se o Carro deixar de existir, o Motor também deixa. Mostre isso criando e depois apagando o objeto. 
class Motor():
    def __init__(self,potencia):
        self.potencia=potencia  
class Carro():
    def __init__(self,marca,modelo,ano,potencia_motor):
        self.marca=marca
        self.modelo=modelo
        self.ano=ano
        self.motor=Motor(potencia_motor)
    def __str__(self):   
        return f"O carro:{self.marca} do modelo:{self.modelo} de ano:{self.ano} tem potencia:{self.motor.potencia}"    
        
carro01 =Carro("Chevrolet","Onix",2010,1000)
carro02 = Carro("Fiat","Fusca",1995, 50)
print(carro01)
print(carro02)

# Crie a classe Casa que é composta por vários Comodos (sala, cozinha, quarto, etc.).
# Cada Comodo deve ser criado dentro da Casa.
class Comodo():
    def __init__(self,nome):
        self.nome=nome
class Casa():
    def __init__(self,endereco):
        self.endereco = endereco
        self.comodos=[]  
    def adicionar_comodo(self,comodo:Comodo):
        self.comodos.append(comodo)
    def __str__(self):
        nomes_comodos = ", ".join([f.nome for f in self.comodos])
        return f"A casa de endereço :{self.endereco} tem {len(self.comodos)} comodos {nomes_comodos}"
    
casa01=Casa("Rua 1")
casa01.adicionar_comodo(Comodo("Sala"))
casa01.adicionar_comodo(Comodo("Cozinha"))
casa01.adicionar_comodo(Comodo("Quarto"))
print(casa01)        
        