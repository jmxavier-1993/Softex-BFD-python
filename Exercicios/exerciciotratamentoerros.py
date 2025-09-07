# # # Escreva um programa que peça ao usuário para digitar um número. 
# # # Trate o erro caso ele digite algo que não seja um número inteiro.

while True:
    try :
     num =int(input("Digite um número:"))
     break
    except ValueError :
       print("Opção invalida, digite novamente um número")   

# # #Peça ao usuário dois números e tente multiplicá-los. 
# # # Se o usuário digitar algo inválido, exiba uma mensagem de erro.    
while True:
    try :
     num =int(input("Digite um número:"))
     num2 =int(input("Digite outro número:"))
     print(num*num2)
     break
    except ValueError :
       print("Opção invalida, digite novamente um número")   

# # # Crie um programa que peça ao usuário um número inteiro. 
# # # Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.    
   

try:
    num =int(input("Digite um número:"))
except ValueError:
    print("Opção invalida, digite novamente um número")  
else:
   print(f"Você digitou corretamente {num}")        

# #  Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# # Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.  

try:
 with open (r'aula01\Aulas\dados.txt','r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)
except FileNotFoundError:
    print("Erro: O arquivo 'dados.txt' não foi encontrado no caminho especificado.")   

# # Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
# # Caso contrário, retorne o resultado da divisão. 

def divisao(a,b):
   a/b
   if b == 0:
        raise ZeroDivisionError("O denominador não pode ser zero.")
   return a / b
try:
   resultado=divisao(2,0)
   print(f"O resultado da divisão eh:{resultado}")
except ZeroDivisionError as e:
 print(f"Erro: {e}")

#  Crie uma exceção personalizada chamada IdadeInvalidaError. 
# Depois, crie uma função cadastrar_idade(idade) que lance essa exceção caso a idade seja negativa.

# Criando a exceção personalizada
class IdadeInvalidaError(Exception):
       def __init__(self, mensagem="A idade não pode ser um número negativo."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)

# # Criando a função para cadastrar a idade
def cadastrar_idade(idade):
    
    if idade <= 0:
        raise IdadeInvalidaError()
    return f"Idade {idade} cadastrada com sucesso!"

# Exemplo de uso da função com e sem a exceção
try:
     print(cadastrar_idade(25))
     print(cadastrar_idade(0))
except IdadeInvalidaError as e:
     print(f"Erro: {e.mensagem}")  
     
# Peça ao usuário dois números e divida o primeiro pelo segundo. Trate dois tipos de erro :

# ValueErrorse o usuário digitar algo inválido
# ZeroDivisionErrorse tentar dividir por zero 
try:
    num3=int(input("Digite um número:"))
    num4=int(input("Digite outro número:"))
    print(num3/num4)
except ValueError:
    print("Opção invalida, digite novamente um número")  
except ZeroDivisionError:
    print("Opção invalida, digite novamente um número")

# Crie um programa que peça ao usuário um número inteiro e verifique se ele é par. Usar:
# trypara a conversão,
# elsepara verificar se é par ou ímpar,
# finallypara exibir "Fim do programa".  

try:
    num =int(input("Digite um número:"))
    if num % 2 == 0:
        print("O número é par.")
    else:
        print("O número é ímpar.")
except ValueError:
    print("Opção invalida, digite novamente um número")
finally:
    print("Fim do programa")
    
# Crie uma função sacar(saldo, valor)que:
# Lance ( raise) uma exceção personalizada SaldoInsuficienteErrorse o valor for maior que o saldo.
# Caso contrário, retorne o novo saldo. 
# Teste a função dentro de um try-excepte exiba uma mensagem enviada ao usuário.   

class SaldoInsuficienteErrorse(Exception):
       def __init__(self, mensagem="Saldo insuficiente."):
        self.mensagem = mensagem
        super().__init__(self.mensagem)
        
def sacar(saldo,valor):
    if valor > saldo:
        raise SaldoInsuficienteErrorse()
    else:
     print(f"Saldo atualizado: {saldo - valor}" ) 
try:
    print(sacar(1000,2000))
except SaldoInsuficienteErrorse as e:
    print(f"Erro: {e.mensagem}") 