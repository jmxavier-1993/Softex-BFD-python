# Na classe, ContaBancaria, converta saldo para uma atributo privado. 
# Crie um método setter e um getter para acessar e modificar essa atributo,
#  seguindo uma regra lógica (Ex: saldo não pode ser negativo)

class ContaBancaria:
   # atributos
   def __init__(self,titular,conta,saldo=0):
      self.titular=titular
      self.conta=conta
      self.__saldo=saldo
   def __str__(self):
      return f"Conta n {self.conta} do titular {self.titular} tem {self.__saldo} de saldo "   
   def __repr__(self):
      return f"ContaBancaria(titular={self.titular!r}, numero_conta={self.conta!r}, saldo={self.__saldo!r})"   
   
   
    # Getters
   def get_saldo(self):
        return self.__saldo
    
    # Setters
   def set_saldo(self, valor):
        if valor < 0:
            print("Saldo não pode ser negativo")
        else:
            self.__saldo += valor
# metodos

   def depositar(self,valor) :
       self.__saldo += valor
       print(f"Foi depositado {valor} na sua conta")
       print(f"Seu saldo atual é: {self.__saldo}")
       return self.__saldo

   def sacar(self,valor) :
       if valor> self.__saldo:
          print("Saldo insuficiente")
       else:
        self.__saldo -= valor
        print(f" O valor sacado foi {valor}")
        return  f"Seu saldo atual é: {self.__saldo}"
   
conta01=ContaBancaria("Juliana",2131234,50)   
conta01.set_saldo(600)
print(conta01.get_saldo())
print(conta01.sacar(60))
print(conta01.get_saldo())


# Crie uma classe, Pessoa, que tenha os atributos: nome, data de nascimento, cpf, identidade. 
# Deixe os atributos cpf e identidade como privado e monte os métodos setters e getters para acessar
# e editar os valores

class Pessoa:
    def __init__(self,nome,data_nascimento,cpf,identidade):
       self.nome=nome
       self.data_nascimento=data_nascimento
       self.__cpf=cpf
       self.__identidade=identidade
    # def __str__(self):
    #   return f"Nome: {self.nome} data de nascimento: {self.data_nascimento} cpf: {self.__cpf} e identidade:{self.__identidade}"   
    # def __repr__(self):
    #   return f"Nome: {self.nome!r} data de nascimento: {self.data_nascimento!r} cpf: {self.__cpf!r} e identidade:{self.__identidade!r}" 

    #getters & setters
    def get_cpf(self):
      return self.__cpf  
     
    def set_cpf(self,valor):
       if len(str(valor))==11:
        self.__cpf = valor
        print("Cpf atualizado com sucesso!")
       else:
        print("Cpf invalido")  
       
    def get_identidade(self):
      return self.__identidade  
     
    def set_identidade(self,valor):
       if len(str(valor))>=6:
          self.__identidade = valor
          print("identidade atualizada com sucesso!") 
       else:
          print("identidade invalida") 
           
pessoa01=Pessoa("Juliana","11/12/1993","10876876756454","545362")
print(f"o cpf é :{pessoa01.get_cpf()}")
pessoa01.set_cpf("76734627353")
print(pessoa01.get_cpf())
print(pessoa01.get_identidade())

