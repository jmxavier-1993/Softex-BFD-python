# lista com for
lista01=[]
for i in range(1,11):
    lista01.append(i*2)
print(lista01)

# o primeiro for roda a qtd de  indices e o segundo for roda a qtd de elementos
lista02=[[linha for linha in range(3)] for coluna in range(3)]
print(lista02)