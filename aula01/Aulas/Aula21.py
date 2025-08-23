# atividade listas
# 1- Crie uma lista chamada livros contendo 3 livros diferentes e exiba a lista na tela.
# 2- Usando a lista livros, exiba apenas o primeiro e o último elemento.
livros=["o programador pragmático","Estatistica - o que é, para que serve, como funciona","Amazon AWS - Descomplicando a computação na nuvem"]
print(livros[0])
print(livros[-1])
# 3- Adicione mais dois livros à lista livros usando o método append() e exiba a lista atualizada.
livros.append(["HTML5 e CSS3 - domine a web do futuro","A Web Mobile - Programe para um Mundo de Muitos Dispositivos"])
print(livros)
# 4- Insira o livro "Duna" na segunda posição da lista livros usando insert().
livros.insert(1,"Duna")
print(livros)
# 5- Remova o livro "Silêncio dos inocentes" da lista usando remove(). Se ele não existir, exiba a mensagem "Livro não encontrado".
if livros=="Silêncio dos inocentes":
 livros.remove("Silêncio dos inocentes")
else:
 print("Livro não encontrado")
# 6- Crie uma lista chamada numeros com os valores [1, 2, 3, 2, 4, 2, 5].
# Mostre quantas vezes o número 2 aparece na lista. 
numeros = [1, 2, 3, 2, 4, 2, 5]
print(numeros.count(2))

# 7- Percorra a lista livros e exiba cada livro com a frase: "O livro <nome do livro> é interessante"

for i in  livros:
 print(f"O livro {i} é interessante")

#  8- Dada a lista idades = [12, 18, 25, 14, 30], use um laço para exibir somente as idades maiores ou iguais a 18.
idades = [12, 18, 25, 14, 30]
maior18=[]
for i in idades:
 if i >=18:
  maior18.append(i)
print(f"{maior18}")
#  9- Crie uma lista valores = [10, 20, 30, 40]. Use um laço for para calcular manualmente a soma de todos os valores.
valores = [10, 20, 30, 40]
soma=0
for i in valores:
    soma+=i
print(soma)
# 10- Use input para receber 3 notas de dois alunos. As notas de cada aluno precisam ser armazenadas em uma lista separada que deve ser armazenada dentro de outra lista chamada notas, exemplo:
# notas = [[7, 8, 9], [6, 5, 7]]
notasaluno01=[]
notasaluno02=[]
for i in range(3):
    notasaluno01.append(int(input(f"Digite a {i+1} nota do aluno01: ")))
    notasaluno02.append(int(input(f"Digite a {i+1}  nota do aluno02: ")))
    notas=[notasaluno01,notasaluno02]
print(f"a media do aluno01 eh: {sum(notasaluno01)/len(notasaluno01)} \n a media do aluno02 eh: {sum(notasaluno02)/len(notasaluno02)} ")