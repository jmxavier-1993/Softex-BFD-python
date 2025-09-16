# Crie uma classe chamada Pessoa que tenha os atributos nome e idade. 
# Em seguida, crie dois objetos dessa classe e imprima os valores de seus atributos.

class Pessoa:
    def __init__(self,nome,idade):
     self.nome = nome
     self.idade= idade
    def apresentar(self):
      return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    

pessoa01=Pessoa("Juliana",31)
print(f" A pessoa01 eh:{pessoa01.nome} e sua idade eh:{pessoa01.idade}")

pessoa02=Pessoa("Claudia",34)
print(f" A pessoa02 eh:{pessoa02.nome} e sua idade eh:{pessoa02.idade}")

# Expanda a classe Pessoa para incluir um método apresentar() que imprima uma frase 
# como:"Olá, meu nome é João e tenho 25 anos.". Teste o método chamando-o a partir de um objeto.

pessoa03=Pessoa("Ana",35)
print(f" A pessoa03 eh:{pessoa03.nome} sua idade eh:{pessoa03.idade}")
print(pessoa03.apresentar())

# Crie uma classe Carro com os atributos marca, modelo e ano.
#  Use o método __init__ para inicializar esses valores. 
# Crie três objetos e mostre suas informações.

class Carro:
   def __init__(self,marca,modelo,ano):
      self.marca=marca
      self.modelo=modelo
      self.ano=ano
carro01= Carro("fiat","uno",2010)   
print(f"Este carro eh da marca:{carro01.marca} o modelo eh:{carro01.modelo} e o ano eh:{carro01.ano}")   

carro02= Carro("Ford","Ford Fiesta",2015)   
print(f"Este carro eh da marca:{carro02.marca} o modelo eh:{carro02.modelo} e o ano eh:{carro02.ano}")   

carro03= Carro("Chevrolet","Onix",2020)   
print(f"Este carro eh da marca:{carro03.marca} o modelo eh:{carro03.modelo} e o ano eh:{carro03.ano}")   

# Usando a classe Carro, crie um objeto e depois altere o valor de um de seus
#  atributos (por exemplo, mudar o ano).
#  Imprima antes e depois da alteração.

carro04=Carro("Toyota","Corolla",2019)
print(f"Este carro eh da marca:{carro04.marca} o modelo eh:{carro04.modelo} e o ano eh:{carro04.ano}")
carro04.ano=2021
print(f"Este carro eh da marca:{carro04.marca} o modelo eh:{carro04.modelo} e o ano eh:{carro04.ano}")

# Crie uma classe ContaBancaria com os atributos titular e saldo. 
# Adicione um método depositar(valor) que aumenta o saldo e um método sacar(valor)
# que diminui o saldo (se houver saldo suficiente). Teste com depósitos e saques.
# parte2
# Modifique a classe ContaBancaria para que o método sacar retorne 
# True se a operação for bem-sucedida e False caso contrário. 
# Teste o retorno e imprima mensagens adequadas.

class ContaBancaria:
   # atributos
   def __init__(self,titular,conta,saldo=0):
      self.titular=titular
      self.conta=conta
      self.saldo=saldo
   def __str__(self):
      return f"Conta n {self.conta} do titular {self.titular} tem {self.saldo} de saldo "   
   def __repr__(self):
      return f"ContaBancaria(titular={self.titular!r}, numero_conta={self.conta!r}, saldo={self.saldo!r})"   
   
   # metodo
   
   def depositar(self,valor) :
       self.saldo += valor
       print(f"Foi depositado {valor} na sua conta")
       print(f"Seu saldo atual é: {self.saldo}")
       return self.saldo

   def sacar(self,valor) :
       if valor> self.saldo:
          print("Saldo insuficiente")
       else:
        self.saldo -= valor
        print(f" O valor sacado foi {valor}")
        print(f"Seu saldo atual é: {self.saldo}")
        return  self.saldo 
   
conta01=ContaBancaria("Juliana",2131234,50)   
conta01.depositar(600)
conta01.sacar(700)

# Crie uma classe Aluno com atributos nome e nota. 
# Depois crie uma classe Turma que tenha uma lista de alunos e um método adicionar_aluno(aluno).
# Crie alguns objetos Aluno e adicione-os à turma.
# parte 8 quesito
# Na classe Aluno, implemente o método __str__ para que, ao imprimir um objeto da classe, 
# apareça algo como:"Aluno: Maria - Nota: 9.5". Teste imprimindo os objetos.

class Aluno:
   def __init__(self,nome,nota):
      self.nome=nome
      self.nota=nota
   def __str__(self):
      return f"Aluno:{self.nome} -Nota :{self.nota}"  
   def __repr__(self):
      return f"(aluno={self.nome!r}, nota={self.nota!r})"

aluno01=Aluno("Ana",9)   
aluno02=Aluno("Juliana",8)

class Turma:
   def __init__(self):
      self.alunos=[]

   def cadastrar_aluno(self,aluno):
      self.alunos.append(aluno)

turma01=Turma()
turma01.cadastrar_aluno(aluno01)
turma01.cadastrar_aluno(aluno02)
print(turma01.alunos)
print(aluno01)
print(aluno02)

# Crie uma classe Cachorro com um atributo de classe especie = "Canis familiaris" e 
# atributos de instância nome e idade. 
# Mostre a diferença entre acessar especie pelo objeto e pela classe.
class Cachorro():
   especie = "Canis familiaris"
   def __init__(self,nome,idade):
      self.nome=nome
      self.idade=idade
   def __str__(self):
      return f"O cachorro:{self.nome} tem {self.idade} de idade"  
      
cachorro01=Cachorro("café",5)  
print(cachorro01.especie) 
cachorro01.especie="Cannis gato"
print(cachorro01.especie) 
print(cachorro01)


            
