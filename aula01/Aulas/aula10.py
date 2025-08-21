idade=int(input("Digite sua idade: "))  
if idade <= 12:
    print("Você é uma criança.")
elif idade <= 17:
    print("Você é um adolescente.")
elif idade <= 64:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")