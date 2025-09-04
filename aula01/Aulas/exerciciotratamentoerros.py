# # # Escreva um programa que peça ao usuário para digitar um número. 
# # # Trate o erro caso ele digite algo que não seja um número inteiro.

# # # while True:
# # #     try :
# # #      num =int(input("Digite um número:"))
# # #      break
# # #     except ValueError :
# # #        print("Opção invalida, digite novamente um número")   

# # #Peça ao usuário dois números e tente multiplicá-los. 
# # # Se o usuário digitar algo inválido, exiba uma mensagem de erro.    
# # while True:
# #     try :
# #      num =int(input("Digite um número:"))
# #      num2 =int(input("Digite outro número:"))
# #      print(num*num2)
# #      break
# #     except ValueError :
# #        print("Opção invalida, digite novamente um número")   

# # # Crie um programa que peça ao usuário um número inteiro. 
# # # Se a conversão for bem-sucedida, mostre uma mensagem usando o bloco else.    
   

# # try:
# #     num =int(input("Digite um número:"))
# # except ValueError:
# #     print("Opção invalida, digite novamente um número")  
# # else:
# #    print(f"Você digitou corretamente {num}")        

# #  Implemente um programa que abra um arquivo chamado dados.txt (não precisa existir). 
# # Use try e finally para garantir que uma mensagem de "Encerrando programa" seja sempre exibida.  

# try:
#  with open (r'aula01\Aulas\dados.txt','r') as arquivo:
#     conteudo = arquivo.read()
#     print(conteudo)
# except FileNotFoundError:
#     print("Erro: O arquivo 'dados.txt' não foi encontrado no caminho especificado.")   

#Crie uma função dividir(a, b) que lance (raise) uma exceção ZeroDivisionError se b for igual a zero. 
# Caso contrário, retorne o resultado da divisão. 

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

class IdadeInvalidaError :
   

 def cadastrar_idade(idade) :
  idade=input("Digite sua idade")
  
