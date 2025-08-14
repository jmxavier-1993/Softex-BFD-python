# lista
# Criando uma lista de frutas
# e inserindo valores dentro da lista com o append
frutas=["banana","maçã","laranja"]


# frutas.append("uva")
# print(frutas) 
# Inserindo um valor no início da lista, ou pelo indice que desejar
frutas.insert(0,"uva")
frutas.insert(0,"jaca")
frutas.insert(0,"limao")
# salada_frutas=frutas
# print(frutas)
# print(frutas[2])  # Imprime o terceiro elemento da lista
# print(frutas[0:4])  # Imprime os quatro primeiros elementos da lista
# print(frutas[0:len(frutas)])  # Imprime todos os elementos da lista
# print(frutas[0:-1])  # Imprime o penúltimo elemento da lista
# print(frutas[0:])  # Imprime o último elemento da lista

# aluno="fred"
# print(aluno[0])  # Imprime o primeiro caractere da string aluno ou a posicao que desejar

# temperos=["sal","pimenta","cominho"]
# frutas += temperos

# print(temperos)

# frutas.remove("jaca")
# frutas.pop(1)
# del frutas[1]  # elemento do python para remover o segundo elemento da lista
# print(frutas)
# print(frutas.clear()) # limpar a lista
# print(sorted(frutas))  # Imprime a lista ordenada sem modificar a lista original
# frutas.sort() # Ordena a lista em ordem crescente
# # frutas.sort(reverse=True) # Ordena a lista em ordem decrescente
# print(frutas)  # Imprime a lista ordenada original


# fruta="morango"
# morango_do_amor=fruta
# print(id(morango_do_amor))
# print(id(fruta))
# salada_frutas=frutas[:] copiando os itens da lista de frutas para a salada de frutas
# salada_frutas=frutas
# salada_frutas.append("morango")  #caso modifique a copia da lista ela modifica as duas.
# print(salada_frutas)
salada_frutas=frutas.copy()  # Copia os itens da lista de frutas para a salada de frutas
# salada_frutas=[]

# for i in frutas:
#     salada_frutas.append(i)
#     print(i)
#     print(salada_frutas)

# print(salada_frutas)  # Imprime a lista de salada de frutas

print(salada_frutas.count("banana"))
# salada_frutas.extend(frutas)  # Adiciona os elementos da lista frutas à lista salada_frutas
print(salada_frutas.index("banana"))
# print(salada_frutas)
idx_banana=salada_frutas.index("banana")

salada_frutas.pop(idx_banana)
print(salada_frutas)