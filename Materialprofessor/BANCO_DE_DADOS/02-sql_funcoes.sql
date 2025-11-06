-- Agrupa os dados com base no id_turma e retorna a contagem de alunos por turma
SELECT id_turma, COUNT() AS n_alunos
FROM Aluno
GROUP BY id_turma;

-- Agrupa os dados com base no id_turma e retorna as turmas com mais de 20 alunos
SELECT id_turma, COUNT() AS n_alunos
FROM Aluno
WHERE (nota1+nota2)/2 > 7
GROUP BY id_turma
HAVING n_alunos > 5;

-- Retorna a maior nota entre os alunos
SELECT nome, MAX(nota1) AS maior_nota
FROM Aluno;

-- Retorna a menor nota entre os alunos
SELECT nome, MIN(nota1) AS menor_nota
FROM Aluno;

-- Retorna a media da coluna nota1 entre os alunos
SELECT AVG(nota1)
FROM Aluno;

-- Retorna a tabela alunos com os valores da coluna nome em maiúsculo 
SELECT nome, upper(nome)
FROM Aluno