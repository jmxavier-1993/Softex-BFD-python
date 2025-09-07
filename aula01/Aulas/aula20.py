# # tuplas
# tupla01=("fred","joao","maria","antonia","wesley")
# # for i in tupla01:
# #     print(i+5)

# # print(type(tupla01))
# print(tupla01.index("maria"))

# # conjunto
# conjunto01={"fred","joao","maria","antonia","wesley"}
# print(type(conjunto01))
# conjunto01.add("ana")
# print(conjunto01)

frutas={"banana","maçã","laranja"}
legumes={"laranja","beterraba","banana","cenoura"}  
print(frutas.add("uva"))  # Adiciona um elemento ao conjunto
# print(frutas.intersection(legumes))  # Interseção entre conjuntos
# print(frutas.difference(legumes))  # Diferença entre conjuntos  
# print(frutas.difference_update(legumes))  # atualizar a diferença entre ao conjuntos
# print(frutas.discard("banana"))  # descarta um valor do conjunto
print(frutas)

lista_aluno={"nome":"frederico",
             "idade":20,
             "curso":"bfd softex",
             "endereco":"rua 1",
             "turma":"turma 36"}
print(lista_aluno["nome"])