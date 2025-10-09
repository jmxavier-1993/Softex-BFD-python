# # 1 Crie uma classe abstrata Pessoa que tenha os métodos :falar, andar, e comer e subclasses Funcionário e aluno,
# # que herde as caracteristicas e metodos de pessoa. instacie um objeto para cada subclasse.

# # 2 Usando o mesmo exemplo da questão anterior, mas converta  a classe Pessoa em uma interface

# from abc import ABC, abstractmethod

# # class Pessoa(ABC):
# #     @abstractmethod
# #     def falar(self):
# #      print("A pessoa está falando")
# #     def comer(self):
# #      print("A pessoa está falando")
# #     def andar(self):
# #      print("A pessoa  está falando")

# class Pessoa(ABC):
#     @abstractmethod
#     def falar(self):
#      ...
#     def comer(self):
#      ... 
#     def andar(self):
#      ...

# class Funcionario(Pessoa) :
#     def falar(self):
#      print("O funcionário está falando")
#     def comer(self):
#       print("O funcionário está comendo")
#     def andar(self):
#       print("O funcionário está andando")  
        

# class Aluno(Pessoa) :
#     def falar(self):
#       print("O aluno está falando")
#     def comer(self):
#       print("O aluno está comendo")
#     def andar(self):
#       print("O aluno está andando")           
  
# funcionario01=Funcionario()
# funcionario01.falar()  

# aluno01=Aluno()
# aluno01.comer()

# Definição de classe abstrata

# 1- Crie uma classe abstrata chamada Animal que possua um método abstrato falar().
# Em seguida, crie duas classes concretas (Cachorro e Gato) que implementem esse método. 
# Mostre o uso criando objetos e chamando o método falar().

from abc import ABC, abstractmethod

class Animal(ABC):
  def __init__(self,nome):
   self.nome=nome
   
  @abstractmethod
  def falar(self):
   return f"O {self.nome} está falando"
 
  def __str__(self):
   return f"O {self.nome} está falando"
  
class Cachorro(Animal):
  def falar(self):
    return super().falar()
  
class Gato(Animal):
  def falar(self):
    return super().falar()
  
cachorrinho01=Cachorro("café")

print(cachorrinho01.falar())

gatinho01=Gato("bolinho")
print(gatinho01.falar())

# 2-  Proibição de instanciamento

# Tente instanciar diretamente a classe Animal da questão anterior 
# e explique o erro gerado pelo Python.

# cachorrinho02=Animal("bolinha")
# print(cachorrinho02.falar())

# # Traceback (most recent call last):
#   File "/workspaces/Softex-BFD-python/Exercicios/exercicioabstracao.py", line 88, in <module>
#     cachorrinho02=Animal("bolinha")
#                   ^^^^^^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Animal without an
# implementation for abstract method 'falar'

# classes abstratas não podem ser acessadas diretamente por objetos,
# só as classes concretas que herdam da classe abstrata. 

# Múltiplos métodos abstratos

# Defina uma classe abstrata FormaGeometrica com dois métodos abstratos: area() e perimetro().
# Crie uma classe concreta Retangulo que herde de FormaGeometrica e implemente os dois métodos.
# Teste criando um objeto e calculando sua área e perímetro.

class FormaGeometrica(ABC):
  @abstractmethod
  def area(self, nome, base:float, altura:float):
    self.nome=nome
    self.base=base
    self.altura=altura
    return f"A área de {self.nome} é {base * altura}"
  @abstractmethod
  def perimetro(self,nome, base:float, altura:float):
    self.nome=nome
    self.base=base
    self.altura=altura
    return f"O perimetro de {self.nome} é {2*base + 2*altura}"  
 
class Retangulo(FormaGeometrica) :
  def area(self, nome, base, altura):
    return super().area(nome, base, altura) 
  def perimetro(self, nome, base, altura):
    return super().perimetro(nome, base, altura)
  
calculaarea=Retangulo() 
calculaperimetro=Retangulo

print(calculaarea.area("shopping",2,5) )
print(calculaarea.perimetro("shopping",2,5) )

# Herança parcial

# Crie uma classe abstrata Transporte com dois métodos abstratos: mover() e parar(). 
# Depois, crie uma subclasse Carro que implemente apenas o método mover(). 
# O que acontece quando você tenta instanciar Carro? Corrija implementando o segundo método.

class Transporte(ABC):
  def __init__(self,tipoveiculo):
    self.tipoveiculo=tipoveiculo
  @abstractmethod
  def mover(self):
    return f"O {self.tipoveiculo} está se movendo"
  @abstractmethod
  def parar(self):
    return f"O {self.tipoveiculo} está parado"
  
class Carro(Transporte):
  def mover(self):
    return super().mover()
  def parar(self):
    return super().parar()
  
veiculo01=Carro("Gol")
print(veiculo01.mover())

# Traceback (most recent call last):
#   File "/workspaces/Softex-BFD-python/Exercicios/exercicioabstracao.py", line 153, in <module>
#     veiculo01=Carro("Gol")
#               ^^^^^^^^^^^^
# TypeError: Can't instantiate abstract class Carro without an implementation for abstract method 'parar'
# a classe que herda o metodos abstratos herdam tudo e precisam instaciar tudo, por isso o erro.