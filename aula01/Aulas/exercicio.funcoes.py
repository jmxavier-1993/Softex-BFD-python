# Crie uma função chamada saudacao que imprime na tela a mensagem 
# "Olá, bem-vindo ao Python!". Em seguida, chame a função no programa.

def saudacao():
    return "Olá, bem-vindo ao Python!"

print(saudacao())

# Crie uma função chamada dobro que recebe um número como parâmetro e
#  retorna o dobro desse número. Teste chamando a função com diferentes valores.

def dobro(a):
    return a *2

print(dobro(4))
print(dobro(10))
print(dobro(2))
print(dobro(6))

# Crie uma função chamada soma que receba dois números e retorne a soma deles. 
# Depois, use a função para somar 10 + 20.

def soma(a,b):
    return a+b

print(soma(10,20))

# Crie uma função chamada mensagem que receba um nome como parâmetro e exiba a mensagem:

# "Olá, [nome]!" , Caso o nome não seja informado, mostre "Olá, visitante!".
nome=input("Olá me diga seu nome:")
def mensagem():
    if nome != " ":
     return f"Olá, {nome}!"
    else:
       return "Olá, visitante!"

print(mensagem())

# Crie uma função chamada operacoes que receba 
# dois números e retorne a soma, a subtração e a multiplicação deles.

def operacoes(a,b):
   return f"soma:",a+b ,"subtracao:", a-b,"multiplicacao:", a*b

print(operacoes(3,4))

# Crie uma função chamada media que receba uma quantidade variável de números e retorne a média deles. 
# Teste com 3, 5 e 7 valores diferentes.

numeros=[5,6,7,5,8,9]
def calcular_media(*a):
   return sum(numeros)/len(numeros)

media=calcular_media(numeros)

print(media)

# Crie uma função chamada dados_pessoais que receba informações de uma pessoa 
# (nome, idade, cidade, etc.)
#  usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
def dados_pessoais(**a):
   return 