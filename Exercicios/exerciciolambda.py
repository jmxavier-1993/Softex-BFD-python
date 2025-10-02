# Dobro dos números (map + lambda)

# Dada a lista [1, 2, 3, 4, 5], use map com 
# lambda para gerar uma nova lista com o dobro de cada número.
num=[1, 2, 3, 4, 5]
dobro=lambda num:num*2
print(list(map(dobro,num)))

# Filtrar pares (filter + lambda)

# Dada a lista [10, 15, 20, 25, 30],
# use filter com lambda para obter apenas os números pares.

num2= [10, 15, 20, 25, 30]
print(list(filter(lambda num2: num2 % 2 == 0,num2)))

# Soma dos números (reduce + lambda)

# Usando reduce, some todos os números da lista [1, 2, 3, 4, 5].
from functools import reduce
num3= [1, 2, 3, 4, 5]
print(reduce(lambda x, y : x + y , num3))

# Ordenação por comprimento da palavra (sorted + lambda)

# Dada a lista ["uva", "banana", "maçã", "laranja"], 
# ordene as palavras pelo tamanho usando sorted e lambda.

lista = ["uva", "banana", "maçã", "laranja"]

ordenamento=sorted(lista,key= lambda lista : len(lista))
print(ordenamento)

# Primeira letra maiúscula (map + lambda)

# Dada a lista ["ana", "pedro", "maria"], 
# use map e lambda para transformar em ["Ana", "Pedro", "Maria"].

lista2= ["ana", "pedro", "maria"]
primaiscula=list(map(lambda lista2: lista2.capitalize(),lista2))
print(primaiscula)

# Produto dos números (reduce + lambda)

# Usando reduce, calcule o produto (multiplicação)
# de todos os elementos da lista [2, 3, 4, 5].

lista3= [2, 3, 4, 5]
multiplicacao=reduce(lambda x , y: x * y,lista3)
print(multiplicacao)

# Ordenar por último caractere (sorted + lambda)

# Dada a lista ["banana", "uva", "maçã", "laranja"], ordene as palavras pelo último caractere.

