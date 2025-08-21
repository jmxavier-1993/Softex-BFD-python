notas=[]

nota01=int(input("Digite a primeira nota: "))
notas.append(nota01)
nota02=int(input("Digite a segunda nota: "))
notas.append(nota02)

media=sum(notas)
qtdnotas=len(notas)
resultadofinal=media/qtdnotas
if resultadofinal >=7 :
    print("Aprovado")
elif resultadofinal >=5 and resultadofinal<7:    
    print("Recuperação")
else:
    print("Reprovado")