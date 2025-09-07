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

def calcular_media(*numeros):
    
   return sum(numeros)/len(numeros)
media=calcular_media(1,2,4,5,6,7,8,)

print(media)

# Crie uma função chamada dados_pessoais que receba informações de uma pessoa 
# (nome, idade, cidade, etc.)
#  usando **kwargs e imprima cada dado em uma linha. Exemplo de chamada:
# dados_pessoais(nome="Ana", idade=25, cidade="Recife")
def dados_pessoais(**kwargs):
   return {k:v for k,v in kwargs.items()}
print(dados_pessoais(nome="Ana", idade=25, cidade="Recife"))

# Crie uma função chamada calculadora que tenha dentro dela outras funções 
# (somar, subtrair, multiplicar, dividir). 
# A função principal deve permitir escolher a operação e retornar o resultado.

def calculadora(a,b):
    def somar():
        return a+b
    def subtrair():
        return a-b
    def multiplicar():
        return a*b
    def dividir():
        return a/b
    return somar(),subtrair(),multiplicar(),dividir()
print(calculadora(4,5))

# Crie uma função chamada aplicar_operacao que receba dois números e uma função como parâmetros.
# A função deve aplicar a operação recebida (ex: soma, multiplicação). Exemplo:
def soma(a, b):
    return a + b

def multiplicacao(a, b):
    return a * b

def aplicar_operacao(a, b, operacao):
    return operacao(a, b)

resultado_soma = aplicar_operacao(3, 4, soma)
print(f"O resultado da soma é: {resultado_soma}")

resultado_multiplicacao = aplicar_operacao(5, 6, multiplicacao)
print(f"O resultado da multiplicação é: {resultado_multiplicacao}")