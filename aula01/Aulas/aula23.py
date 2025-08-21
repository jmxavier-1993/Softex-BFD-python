# FAZER UM CRUD (Create, Read, Update, Delete)

# DICIONÁRIOS

dicionario = {"id": 0,
               "nome": "fred",
              "idade": 30,
              "nacionalidade":"brasileiro",
              }
#print(dicionario.get("nome")) # OU
#print(dicionario["nome"])
# print(dicionario.keys()) # Imprimir as chaves
# print(dicionario.values()) # Imprimir os valores
# dicionario["profissão"] = "desenvolvedor" # Adicionando itens e categorias à lista
# dicionario.update({"idade":25}) # Atualizando dados dentro do dicionário
# dicionario.pop("idade") # Deletando a categoria
# dicionario.popitem() # Removendo o útlimo item do dicionário
# dicionario.clear() # Apaga os dados mas não apaga o dicionário
# del dicionario["idade"] # Apaga a chave correspondente
# del dicionario # Deletando o dicionário inteiro
# dicionario_2 = dicionario.copy() # Copiando o dicionário

# for itens in dicionario.items(): #Para gerar o dicionário em tuplas
# for itens in dicionario.values(): # Procurando um valor específico dentro do dicionário
#     if itens == "fred":
#         print("Achamos o meliante")

nomes_funcionarios = ["Fred", "João", "Maria"]
dicionario_aleatorio = {
    "nome": nomes_funcionarios,
    "função":["Desenvolvedor", "Tech Lead", "PO"],
}
print(dicionario_aleatorio["função"][2]) 