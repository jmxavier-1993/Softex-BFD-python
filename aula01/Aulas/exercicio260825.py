# Crie um dicionário vazio chamado cadastro e adicione os seguintes pares chave-valor:
cadastro={
"nome": "Lucas",
"idade": 25,
"email": "lucas@email.com"
}

# Usando o dicionário abaixo, use o método .get() para obter o valor da chave "telefone", retornando "Não informado" se a chave não existir.
cliente = {"nome": "Amanda", "idade": 31,}
if cliente.get("telefone"):
  print("o telefone do cliente eh:",(cliente["telefone"]))
else:
  print(f"Não informado")  

# Utilize um laço for para imprimir todas as chaves do dicionário abaixo.
livro = {"título": "1984", "autor": "George Orwell", "ano": 1949}
for i in livro:
    print(i)

# Adicione uma nova chave chamada "disponível" ao dicionário acima com o valor True.
livro.update({"disponível":True})
print(livro)

# Use o método .pop() para remover a chave "ano" do dicionário livro. Imprima o valor removido.
removido=livro.pop("ano")
print("\n" "valor removido", removido)

# Crie um dicionário compras com pelo menos 3 itens (nome do produto como chave e preço como valor). 
# Em seguida, use .values() para calcular o total da compra.
listacompras={"Agua sanitária":2.00, "feijão":6.00,"Arroz":5.00}
print(sum(listacompras.values()))

# Dado o dicionário:
# Imprima as frutas que têm mais de 2 unidades usando um laço for.
frutas = {"maçã": 3, "banana": 5, "laranja": 2}
for j, i in frutas.items():
   if i >2:
    print(j,i)

# Verifique se a chave "senha" está presente no dicionário abaixo. Se não estiver, adicione-a com o valor "123456".
usuario = {"login": "joaosilva"}
if usuario.items== "senha":
  print(usuario("senha"))
else:
  usuario.update({"senha":"123456"})
  print(usuario)

# Use o método .items() para iterar sobre o dicionário abaixo e imprima frases como "A capital de SP é São Paulo".
capitais = {"SP": "São Paulo", "RJ": "Rio de Janeiro", "MG": "Belo Horizonte"}
for estado, capital in capitais.items():
        print(f"A capital de {estado} é {capital}")

# Dado o dicionário abaixo, atualize o valor da chave "estoque" somando 10 unidades ao valor atual. 

produto = {"nome": "Teclado", "estoque": 15}
produto.update({"estoque":15+10})
print(produto)


