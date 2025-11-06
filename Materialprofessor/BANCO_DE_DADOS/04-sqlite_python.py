import sqlite3

# cria uma conexao com o banco de dados.
db_connection = sqlite3.connect("aulas/banco_dados/db/escola_v2.db")

# cria o cursor
cursor = db_connection.cursor()

# executa qualquer comando SQL suportado pelo sqlite
cursor.execute("""
SELECT * 
FROM Aluno
""")

# retorna o cabecalho de cada coluna
print([description[0] for description in cursor.description])

# imprime cada linha da tabela
for row in cursor:
    print(row)

# Encerra a conexao com o banco de dados
db_connection.close()
