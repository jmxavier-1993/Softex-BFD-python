# Crie um dicionário simples
# Crie um dicionário chamado aluno com as chaves: "nome",
# "idade" e "nota", e preencha com valores fictícios.

aluno = {"nome": "Fred", "idade": 35, "nota": 8.5}

# Acessando valores

# Dado o dicionário:

# produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
# Imprima o nome do produto e a quantidade em estoque.

produto = {"nome": "Caneta", "preço": 2.5, "estoque": 100}
print((produto["nome"]), (produto["estoque"]))

# Adicionando novos pares chave-valor

# Dado o dicionário:

# pessoa = {"nome": "Carlos", "idade": 30}
# Adicione uma nova chave "cidade" com valor "São Paulo".
pessoa = {"nome": "Carlos", "idade": 30}
pessoa.update({"cidade": "São Paulo"})
print(pessoa)

# Removendo elementos

# Dado o dicionário:

# carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
# Remova a chave "ano" do dicionário.
carro = {"marca": "Ford", "modelo": "Fiesta", "ano": 2010}
del carro["ano"]
print(carro)

# Verificando existência de uma chave

# Verifique se a chave "telefone" existe no dicionário:

# contato = {"nome": "Ana", "email": "ana@email.com"}
contato = {"nome": "Ana", "email": "ana@email.com"}
if contato.items == "telefone":
    print(contato("telefone"))
else:
    print("Este usuário não possui telefone cadastrado")

# Contando frequência de palavras

# Escreva uma função que receba uma lista de palavras e retorne um dicionário com a contagem de cada palavra.

# palavras = ["maçã", "banana", "maçã", "laranja", "banana", "maçã"]
# Invertendo um dicionário

# Dado o dicionário:

# d = {"a": 1, "b": 2, "c": 3}
# Crie um novo dicionário invertendo as chaves e os valores: {1: "a", 2: "b", 3: "c"}.

# Dicionário com listas

# Crie um dicionário onde cada chave é o nome de um aluno e o valor é uma lista com 3 notas. Depois, imprima a média de cada aluno.
# Mesclando dois dicionários

# Escreva uma função que recebe dois dicionários e retorna um novo dicionário contendo todos os pares chave-valor. Se houver chaves repetidas, o valor do segundo dicionário deve prevalecer.
# Ordenando dicionário por valor

# Dado o dicionário:

# pontuacoes = {"João": 50, "Maria": 80, "Pedro": 70}
# Imprima os itens do dicionário ordenados pela pontuação (valor), do maior para o menor.