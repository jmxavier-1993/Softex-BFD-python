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

class ContaBancaria:
   valor=0
   def __init__(self,titular,saldo):
      self.titular=titular
      self.saldo=saldo
   def depositar(self,valor) :
       return self.saldo + valor