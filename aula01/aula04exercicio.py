# mostre tres frases diferentes usando tres comandos prints separados
print ("hello word", "Juliana Marinho")
print ("hello word", "Juliana Marinho")
print ("hello word", "Juliana Marinho")

# mostre o seguinte  texto formatado:
# Nome:Joao
# idade: 20 anos
#Curso :Python basico

nome="Joao"
idade= 20
Curso="Python basico"
print(nome ,"\n", idade ,"\n", Curso ,"\n")

# combinar textos e numeros
print(f"Meu nome eh:{nome} Minha idade eh:{idade} Eu faco curso de:{Curso}")

# use print para desenhar um quadrado com ## como:
# ####
# #  #
# #  #
# ####

print("#####")
print("#   #")
print("#   #")
print("#####")

print("#####" "\n" "#   #""\n" "#   #""\n" "#####" "\n")

# operacoes basicas

var01=6
var02=4
soma= var01+ var02
print(soma)
subtracao= var01-var02
print(subtracao)
multiplicacao= var01* var02
print(multiplicacao)
divisao=var01/var02
print(divisao)
restodivisao= var01%var02
print(restodivisao)
divisao1=var01//var02
print(divisao1)
exponencial=var01**var02
print(exponencial)

# calculadora simples
var04=int(input("digite um numero"))
var05=int(input("digite outro numero"))
operacao=input("qual operacao deseja fazer [S] ou[D]")
if (operacao == "S"):
    print(var04+var05)
elif(operacao == "D"):
    print(var04*var05)
else:
    print("opção invalida")      