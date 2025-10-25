-- comando para listar tabelas
.tables
-- mostra a extrutura de criação da tabela da tabela
.schema Aluno
.schema Turma
.schema Curso

--query para acessar colunas da tabela aluno
-- SELECT
-- *
-- from 
-- Aluno;

-- 

-- SELECT
-- nome as nome_aluno,
-- nota1,
-- nota2,
-- (nota1+nota2)/3 as media
-- from Aluno
-- ORDER by media DESC
-- LIMIT 10;

--Mostre todos os registros da tabela Aluno.

-- (Use SELECT e FROM)
SELECT
*
from 
  Aluno;


--Exiba apenas o nome e a nota1 de todos os alunos.

--(Use SELECT com colunas específicas)
SELECT
  nome as nome_aluno,
  nota1
from 
  Aluno;


-- Liste todos os alunos cuja nota2 seja maior que 8.

-- (Use WHERE)
SELECT
  nome as nome_aluno,
  nota2
from 
  Aluno
WHERE 
  nota2 > 8;

-- Mostre os alunos que nasceram após o ano de 2000.

-- (Use WHERE com data)
SELECT
  nome as nome_aluno,
  data_nascimento
from 
  Aluno
WHERE 
  data_nascimento >= date(2000-01-01);


-- Exiba o nome e a mensalidade de todos os cursos que custam mais de 600 reais.

-- (Use WHERE com condição numérica)

SELECT
  nome as nome_curso,
  mensalidade
from 
  Curso
WHERE 
  mensalidade > 600;

-- Mostre o nome das turmas e o ano correspondente, 
--ordenados pelo ano em ordem crescente.

-- (Use ORDER BY)
SELECT
  nome as nome_turma,
  ano
from 
  Turma
ORDER by 
  ano ASC;


-- Liste o ano das turmas e a quantidade de turmas por ano.

-- (Use GROUP BY)
SELECT
  ano,
  COUNT(*) AS qtd_turmas
FROM
  Turma
GROUP BY
  ano;




-- Calcule a média da nota1 dos alunos por turma_id.

-- (Use GROUP BY com função de agregação)
SELECT
  sum(nota1)/count(nota1) as media_alunos,
  id_turma
FROM
  Aluno
GROUP by id_turma 
ORDER by media_alunos DESC;   



-- Mostre o ano e a quantidade de turmas apenas 
--para os anos que têm mais de 2 turmas.

-- (Use GROUP BY e HAVING)

SELECT
  count(nome) as qtd_turmas,
  ano
from 
  Turma
GROUP by ano
having qtd_turmas >2;

-- Exiba o nome dos cursos e suas mensalidades,
-- ordenando primeiro pela mensalidade (decrescente).

-- (Use ORDER BY)

SELECT
  nome as nomes_cursos,
  mensalidade
from 
  Curso
ORDER by mensalidade DESC;


