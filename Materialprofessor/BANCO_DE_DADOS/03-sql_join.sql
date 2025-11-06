SELECT Aluno.nome, Turma.nome
FROM Aluno
--WHERE (Aluno.nota1 + Aluno.nota2)/2  >= 7
FULL JOIN Turma
ON id_turma = Turma.id

