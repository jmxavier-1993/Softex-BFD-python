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
  