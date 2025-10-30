# Importe o módulo sqlite3 e faça a conexão com o banco de dados escola_v2.db

# Faça a query para pegar toda a tabela alunos e imprima na tela.

import sqlite3

conn = sqlite3.connect("escola_v2.db")
cursor = conn.cursor()

cursor.execute("SELECT* FROM Aluno")

query_result =cursor.fetchall()

print(query_result)

conn.close()

# Obtenha a media entre nota1 e nota2 dos alunos,
# ordene em ordem decrescente e retorne apenas os 10 maiores notas.
# No fim imprima na tela a lista desses alunos e suas médias.

cursor.execute(
    "SELECT nome,(nota1+nota2)/2 as media_alunos  from Aluno order by media_alunos desc limit 10;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()

# Use Left Join com as tabelas Aluno e Turma e imprima todos os dados da tabela.

cursor.execute(
    "SELECT * from Aluno left join Turma on Aluno.id_Turma = Turma.id;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()

# Usando a query da questão 4, adicione um filtro para pegar apenas os alunos da turma 2 e imprima na tela.


cursor.execute(
    "SELECT * from Aluno left join Turma on Aluno.id_Turma = Turma.id where Turma.id = 2;"
)
query_result = cursor.fetchall()

print(query_result)

conn.close()