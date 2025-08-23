# 1. Torneio de Futebol
vitorias = empates = derrotas = 0

for i in range(1, 6):
    gols_selecao = int(input(f"Gols da Seleção no jogo {i}: "))
    gols_adversario = int(input(f"Gols do adversário no jogo {i}: "))

    if gols_selecao > gols_adversario:
        vitorias += 1
    elif gols_selecao == gols_adversario:
        empates += 1
    else:
        derrotas += 1

print("\n=== Torneio de Futebol ===")
print(f"Vitórias: {vitorias}")
print(f"Empates: {empates}")
print(f"Derrotas: {derrotas}")

# 2. Jogo de Adivinhação
import random

numero_secreto = random.randint(1, 20)
tentativas = 5

for tentativa in range(1, tentativas + 1):
    palpite = int(input("Adivinhe o número (1 a 20): "))

    if palpite < numero_secreto:
        print("Muito baixo!")
    elif palpite > numero_secreto:
        print("Muito alto!")
    else:
        print("Você acertou!")
        break
else:
    print(f"Game over! O número era {numero_secreto}")

# 3. Venda de Ingressos
total = 0
pessoas = int(input("Quantas pessoas vão ao show? "))

for i in range(1, pessoas + 1):
    idade = int(input(f"Idade da pessoa {i}: "))

    if idade <= 12:
        print("Entrada grátis")
    elif 13 <= idade <= 17:
        print("Meia entrada (R$ 10)")
        total += 10
    else:
        print("Ingresso inteiro (R$ 20)")
        total += 20

print(f"Total arrecadado: R$ {total}")

# 4. Quiz de Conhecimentos Gerais

perguntas = [
    {
        "pergunta": "Capital do Brasil?",
        "opcoes": ["1- São Paulo", "2- Brasília", "3- Rio de Janeiro"],
        "correta": 2,
    },
    {
        "pergunta": "Planeta conhecido como planeta vermelho?",
        "opcoes": ["1- Marte", "2- Júpiter", "3- Vênus"],
        "correta": 1,
    },
    {
        "pergunta": "Quem escreveu Dom Quixote?",
        "opcoes": ["1- Machado de Assis", "2- Cervantes", "3- Shakespeare"],
        "correta": 2,
    },
    {
        "pergunta": "Qual o maior oceano?",
        "opcoes": ["1- Atlântico", "2- Pacífico", "3- Índico"],
        "correta": 2,
    },
    {
        "pergunta": "Qual a cor da clorofila?",
        "opcoes": ["1- Verde", "2- Azul", "3- Amarela"],
        "correta": 1,
    },
]

pontos = 0

print("== Quiz de Conhecimentos Gerais ==")

for i, pergunta in enumerate(perguntas, start=1):
    print(f"{i}) {pergunta['pergunta']}")
    for opcao in pergunta["opcoes"]:
        print(opcao)
    resposta = int(input("Sua resposta: "))
    if resposta == pergunta["correta"]:
        pontos += 1

print(f"\nPontuação final: {pontos}/5")

if pontos == 5:
    print("Gênio!")
elif pontos >= 3:
    print("Mandou bem!")
elif pontos >= 1:
    print("Precisa estudar mais")
else:
    print("Zerou o quiz")

# 5. Competição entre Candidatos
candidatos = [0, 0, 0]

for avaliador in range(1, 4):
    print(f"\nAvaliador {avaliador}:")
    for candidato in range(1, 4):
        nota = float(
            input(f"Nota do avaliador {avaliador} para o candidato {candidato}: ")
        )
        candidatos[candidato - 1] += nota

print("\nPontuação final:")
for i, total in enumerate(candidatos, start=1):
    print(f"Candidato {i}: {total}")

max_pontos = max(candidatos)
vencedores = [i + 1 for i, pontos in enumerate(candidatos) if pontos == max_pontos]

if len(vencedores) > 1:
    print("\nEmpate! Disputa acirrada")
else:
    print(f"\nCandidato {vencedores[0]} é o campeão!")

# 6. Verificação de Situação do Aluno
nome = input("Digite o nome do aluno: ")
nota = float(input("Digite a nota do aluno: "))

if nota >= 7:
    situacao = "APROVADO"
elif nota >= 5:
    situacao = "em REPOSIÇÃO"
else:
    situacao = "REPROVADO"

print(f"{nome} está {situacao}!")
