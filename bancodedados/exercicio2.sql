-- comando para listar tabelas
.tables
-- mostra a extrutura de criação da tabela da tabela
.schema Aluno
.schema Turma
.schema Curso

--COUNT Mostre quantos alunos estão 
--cadastrados na tabela Aluno. (Use a função COUNT)
SELECT
  count(id) as qtd_alunos
from 
  Aluno;

--MIN Mostre a menor mensalidade
-- entre todos os cursos cadastrados. (Use a função MIN)
SELECT
  min(mensalidade) as min_mensalidade
from Curso;   

--MAX Mostre a maior nota1 registrada entre todos os alunos. (Use a função MAX)

SELECT
  max(nota1) as max_nota
FROM Aluno;  

--SUM Calcule o valor total das mensalidades 
--de todos os cursos. (Use a função SUM)

SELECT
  sum(mensalidade) as valor_total_mensalidade
from Curso;

--AVG Mostre a média geral da nota2 dos alunos. (Use a função AVG)


SELECT
  avg(nota2) as media_nota2_alunos
from Aluno;