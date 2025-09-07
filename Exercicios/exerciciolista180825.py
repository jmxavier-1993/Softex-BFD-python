# 1

a1 = "123"
a2 = int(a1)
a3 = float(a1)
print(a2)
print(a3)
# 2
nome = "Python é incrível!"
print(len(nome))
nome = nome.upper()
print(nome)
nome = "Python é poderoso!"
print(nome)
# 3
numeros = [10, 20, 30, 40, 50]
print(numeros[3])
numeros.append(60)
print(numeros)
numeros.remove(20)
print(numeros)

# 4
aluno = {"nome": "Maria", "idade": 22, "curso": "Engenharia"}
aluno["notas"] = [8.5, 7.0, 9.2]
print(aluno["curso"])
# 5
cores = ("vermelho", "verde", "azul", "verde")
conjunto_cores = set(cores)
conjunto_cores.add("amarelo")
print(conjunto_cores)

# 6
a = 15
b = 4
divisaointeira = a // b
print(divisaointeira)
restodivisao = a % b
print(restodivisao)

# 7
dados = [42, 3.14, "Python", True, [1, 2]]
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))
print(type(dados[4]))

# 8
valorstring = "programação"
invertido = valorstring[::-1]
print(invertido)

if valorstring == invertido:
    print(True)
else:
    print(False)

# 9
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[1][1])
matriz[2][1] = 10
print(matriz)

# 10
estoque = {"banana": 5, "maca": 10, "laranja": 8}
estoque["pera"] = [12]
print(estoque)

del estoque["banana"]
print(estoque)
print(estoque.keys())