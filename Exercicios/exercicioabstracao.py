# 1 Crie uma classe abstrata Pessoa que tenha os métodos :falar, andar, e comer e subclasses Funcionário e aluno,
# que herde as caracteristicas e metodos de pessoa. instacie um objeto para cada subclasse.

# 2 Usando o mesmo exemplo da questão anterior, mas converta  a classe Pessoa em uma interface

from abc import ABC, abstractmethod

# class Pessoa(ABC):
#     @abstractmethod
#     def falar(self):
#      print("A pessoa está falando")
#     def comer(self):
#      print("A pessoa está falando")
#     def andar(self):
#      print("A pessoa  está falando")

class Pessoa(ABC):
    @abstractmethod
    def falar(self):
     ...
    def comer(self):
     ... 
    def andar(self):
     ...

class Funcionario(Pessoa) :
    def falar(self):
     print("O funcionário está falando")
    def comer(self):
      print("O funcionário está comendo")
    def andar(self):
      print("O funcionário está andando")  
        

class Aluno(Pessoa) :
    def falar(self):
      print("O aluno está falando")
    def comer(self):
      print("O aluno está comendo")
    def andar(self):
      print("O aluno está andando")           
  
funcionario01=Funcionario()
funcionario01.falar()  

aluno01=Aluno()
aluno01.comer()