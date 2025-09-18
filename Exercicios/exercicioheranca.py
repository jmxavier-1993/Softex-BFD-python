# 1-Crie uma classe Usuario com atributos nome e email. 
# Depois, crie uma classe Cliente que herde de Usuario. 
# Crie uma instancia de um cliente e acesse todos os atributos.

# 2-Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente.
#  Mostre como chamar o método herdado a partir de um objeto Cliente.

class Usuario:
   def __init__(self,nome,email):
      self.nome=nome
      self.email=email
   def __str__(self):
    return f"O cliente {self.nome}, possui email {self.email}"
   
   def exibir_informacoes(self):
    return f"O cliente {self.nome}, possui email {self.email}"
   def saudacao(self):
     return f"Olá, {self.nome}"

class Cliente(Usuario):
  def __init__(self, nome, email,saudacao="Olá, cliente"):
    super().__init__(nome, email)
    self.saudacao=saudacao
  ...

cliente01=Cliente("Juliana","ju@hotmail.com") 
# print(cliente01)
print(cliente01.exibir_informacoes())
print(cliente01.saudacao)

# Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".
# Mostre como funciona a chamada.



# criar classe Pessoa com suas caracteristicas e uma classe funcionario que herde Pessoa

# class Pessoa:
#     def __init__(self,nome,idade,genero,estado_civil):
#      self.nome=nome
#      self.idade=idade
#      self.genero=genero
#      self.estado_civil=estado_civil
    

# class funcionario(Pessoa):
#    def __init__(self, nome, idade, genero, estado_civil,telefone,email):
#       super().__init__(nome, idade, genero, estado_civil)
#       self.telefone=telefone
#       self.email=email
#    def __str__(self):
#       return f"Nome: {self.nome}, idade: {self.idade}, genero: {self.genero}, e estado civil:{self.estado_civil}, telefone: {self.telefone} ,email:{self.email}"

# pessoa1=funcionario("Juliana",31,"Feminino","Solteira",81978409237,"ju@hotmail.com")    

# print(pessoa1)
  