# Criando uma interface

# Crie uma interface chamada Pagamento com um método abstrato processar(valor). 
# Depois, crie duas classes (CartaoCredito e Boleto) que implementem a interface.
# Mostre como chamar processar() para cada uma.

from abc import ABC, abstractmethod

class Pagamento(ABC):
    @abstractmethod
    def processar(self,valor):
        ...
        
class CartaoCredito(Pagamento):
    def processar(self, valor,senha):
        self.valor = valor
        self.senha = senha
        return (f"Pagamento no valor R${self.valor} realizado com sucesso!")
            
class Boleto(Pagamento):
    def processar(self, valor,vezes):
        self.valor = valor
        self.vezes = vezes
        return (f"Boleto no valor R${self.valor} em {self.vezes} vezes no total de {self.valor/self.vezes} gerado com sucesso!")    
        
cartao = CartaoCredito()
boleto = Boleto()       
print(cartao.processar(5000,1234))
print(boleto.processar(5000,2))

# Interface múltipla

# Crie duas interfaces: Ligavel (com o método ligar()) e Desligavel (com o método desligar()). 
# Crie uma classe Computador que implemente ambas. Mostre seu uso.

from abc import ABC, abstractmethod
class ligavel(ABC):
    @abstractmethod
    def ligar(self):
        ...,        
class desligavel(ABC):
    @abstractmethod
    def desligar(self):
        ...
class Computador(ligavel,desligavel):
    def ligar(self):
        return "O computador foi ligado"
    def desligar(self):
        return "O computador foi desligado"
caso=Computador()
print(caso.ligar())
print(caso.desligar())    
    
# Interface em herança múltipla

# Crie uma interface Imprimivel com o método imprimir(). 
# Crie outra interface Exportavel com o método exportar(). 
# Implemente uma classe Relatorio que herde de ambas e implemente os métodos.    

class Imprimivel(ABC):
    @abstractmethod
    def imprimir(self):
        ...
class Exportavel(ABC):
    @abstractmethod
    def exportar(self):
        ...
        
class Relatorio(Imprimivel,Exportavel):
    def imprimir(self):
        return "Relatório impresso"
    def exportar(self):
        return "Relatório exportado"    
    
caso01=Relatorio()
print(caso01.imprimir())
print(caso01.exportar())     

#Forçando contrato

# Crie uma interface Repositorio com os métodos salvar(objeto) e buscar(id). 
# Depois, crie uma classe RepositorioMemoria que não implemente um dos métodos. 
# O que acontece quando você tenta instanciá-la? Corrija o código.    

class Repositorio(ABC):
    @abstractmethod
    def salvar(self,objeto):
        ...
    @abstractmethod
    def buscar(self,id):
        ...
        
class RepositorioMemoria(Repositorio):
    def salvar(self,objeto):
        super().salvar(objeto)
        return "Objeto salvo na memória"
    def buscar(self,id):
        super().buscar(id)
        return "Objeto buscado na memória"  
    
caso02=RepositorioMemoria()
print(caso02.buscar(1))  
print(caso02.salvar(1))  

#File "c:\Área de Trabalho\Softex-BFD-python\Exercicios\exerciciointerface.py", line 101, in <module>        
#caso02=RepositorioMemoria()
#TypeError: Can't instantiate abstract class RepositorioMemoria without an implementation for abstract method ' 
# não posso instanciar uma classe abstrata,sem instaciar todos os metodos pois ela tem metodos abstratos