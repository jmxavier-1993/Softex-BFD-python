idade=int(input("Digite sua idade: ")) 
cnh=input("Você possui CNH? (S/N): ").upper()
cachaca=input("Você bebeu cachaça? (S/N): ").upper()

if idade>=18 and cnh=="S" and cachaca=="N":
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.")