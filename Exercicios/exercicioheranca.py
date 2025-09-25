# 1-Crie uma classe Usuario com atributos nome e email. 
# Depois, crie uma classe Cliente que herde de Usuario. 
# Crie uma instancia de um cliente e acesse todos os atributos.

# 2-Implemente um método exibir_informacoes() na classe Usuario e herde esse método em Cliente.
#  Mostre como chamar o método herdado a partir de um objeto Cliente.

# 3- Na classe Usuario, crie um método saudacao() que retorna "Olá, usuário".
# Na classe Cliente, sobrescreva esse método para retornar "Olá, cliente".
# Mostre como funciona a chamada.

# 4-Na classe Cliente, adicione o atributo saldo.
# Adicione um método construtor em Cliente que inicialize também os atributos de Usuario 
# usando super().

class Usuario:
   def __init__(self,nome,email,senha):
      self.nome=nome
      self.email=email
      self.senha=senha
   def __str__(self):
    return f"O cliente {self.nome}, possui email {self.email}"
   
   def exibir_informacoes(self):
    return f"O cliente {self.nome}, possui email {self.email}"
   def saudacao(self):
     return f"Olá, {self.nome}"

class Cliente(Usuario):
  def __init__(self, nome, email,senha,saldo):
    super().__init__(nome, email,senha)
    self.saldo=saldo
  def saudacao(self):
    return f"Olá, {self.nome}! Seu saldo é de R${self.saldo}."
    
  

cliente01=Cliente("Juliana","ju@hotmail.com",123456,500) 
# print(cliente01)
print(cliente01.exibir_informacoes())
print(cliente01.saudacao())

#5- Crie uma classe Funcionario que herda de Usuario e, em seguida, 
# crie uma classe Gerente que herda de Funcionario. 
# Mostre como instanciar um gerente e acessar seus atributos.

class Funcionario(Usuario):
 def __init__(self, nome, email,senha):
   super().__init__(nome, email,senha)

class Gerente(Funcionario) :
  ...

gerente01=Gerente("Juliana","ju@hotmail.com",12345)
print(gerente01.nome)
print(gerente01.email)

# -6 Crie uma classe Autenticacao com um método login(). 
# Crie outra classe Permissao com um método verificar_permissao(). 
# Em seguida, crie uma classe Administrador que herda de ambas. Como usar os métodos herdados?

# -7 Usando o exemplo anterior, adicione um método status() em Autenticacao e também em Permissao. 
# Se a classe Administrador herda das duas, qual versão de status() será chamada?
# Use Administrador.__mro__ para mostrar a ordem.

class Autenticacao:
      
   def login(self, senha_digitada):
        if self.senha == senha_digitada:
         return f"Login permitido!!!"
        else:
         return f"Login Não autorizado!!!"
         
   def status(self) :
     return f"Login permitido!!!"   
  

class Permissao:
    def verificar_permissao(self, nome, senha):
        if nome == self.nome and senha == self.senha:
         return f"Login permitido!!!"
        else:
         return f"Login Não autorizado!!!"
          
    def status(self) :
     return f"Status permitido!!!"

class Administrador(Usuario, Autenticacao, Permissao):
    def __init__(self, nome, email, senha, nivel_acesso):
        super().__init__(nome, email, senha)
        self.nivel_acesso = nivel_acesso # Adicionando um atributo exclusivo

    def __str__(self):
        return f"Administrador {self.nome} com nível {self.nivel_acesso}"
      
admin = Administrador("Juliana", "juliana@adm.com", "12345", 10)
admin.status()
print(admin.status())
print(Administrador.__mro__)

# Métodos herdados de Autenticacao
print(f"Login com a senha correta: {admin.login('12345')}")
print(f"Login com a senha errada: {admin.login('senha_errada')}")

# Métodos herdados de Permissao
print(f"Verificar permissão com dados corretos: {admin.verificar_permissao('Juliana', '12345')}")
print(f"Verificar permissão com dados incorretos: {admin.verificar_permissao('Joao', 'outra_senha')}")  
   
# plus exercicio anterior

# criar classe Pessoa com suas caracteristicas e uma classe funcionario que herde Pessoa

class Pessoa:
    def __init__(self,nome,idade,genero,estado_civil):
     self.nome=nome
     self.idade=idade
     self.genero=genero
     self.estado_civil=estado_civil
    

class funcionario(Pessoa):
   def __init__(self, nome, idade, genero, estado_civil,telefone,email):
      super().__init__(nome, idade, genero, estado_civil)
      self.telefone=telefone
      self.email=email
   def __str__(self):
      return f"Nome: {self.nome}, idade: {self.idade}, genero: {self.genero}, e estado civil:{self.estado_civil}, telefone: {self.telefone} ,email:{self.email}"

pessoa1=funcionario("Juliana",31,"Feminino","Solteira",81978409237,"ju@hotmail.com")    

print(pessoa1)
  