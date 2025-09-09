# poo
class Cachorro:
    especie="Cannis lupus familiaris"
    nome="toto"
    raca="caramelo"
    idade=2

# instaciar o objeto
auau = Cachorro()
print(auau)    
# acessar os atributos do objeto
print(auau.especie,auau.nome,auau.idade,auau.raca , sep="\n")    

# atributos do objeto com init(metodo construtor)
class Cachorro:  #segue a covenção CamelCase
    especie= "Cannis lupus familiaris" 
    def __init__(self,nome,raca,idade): #metodo construtor
        self.nome=nome
        self.raca= raca
        self.idade=idade
    def __str__(self):
        return f"Especie:{self.especie} \n nome:{self.nome}\n raça:{self.raca}\n idade: {self.idade}"
    def latir(self):
     print("Auuuuuuu")
    def correr(self, metros):
     print(f"{self.nome} correu {metros}")  
  


doguinho1 = Cachorro("café","labrador",5)
print(doguinho1)
print(doguinho1.especie,doguinho1.nome,doguinho1.raca,doguinho1.idade,sep="\n")

print(doguinho1.latir())
print(doguinho1.correr(40))








