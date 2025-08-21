# criar uma lista com varios tipos de dados
dados=[1,"banana",3.14,True]

# criar uma lista e adicionar 2 itens e remova 1
dados.append("maça")
dados.append(42)
dados.remove("banana")
# faça uma copia real de uma lista
dados2=dados.copy()
print(dados2)

# criar uma lista com numeros e multiplicar cada numero por 5
num=[1,2,3,4,5,6,7,8,9]
# multiplica= [(num[0])*5,(num[1])*5,(num[2])*5,(num[3])*5,(num[4])*5,(num[5])*5,(num[6])*5,(num[7])*5,(num[8])*5] 
# print(multiplica)
vazio = []
for i in num:
    vazio.append(i * 5)  # Multiplica cada número por 5 e adiciona à lista
print(vazio)

# pegue a lista a1 =[1, 2, 3, 4, 5,6] e gere uma nova lista apenas com os valores 4 e 5

a1 = [1, 2, 3, 4, 5, 6]
a2 = [a1[3:5]]
print(a2)