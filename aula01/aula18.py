# matriz
matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]
# acessar o numero 5
print(matriz[1][1])
# imprimir um abaixo do outro
# for linha in matriz:
#     print(linha)
# imprimir cada linha da matriz
for i in range(len(matriz)):
    print(matriz[i])
matriz_tridimensional = [[[1, 2, 3],[4, 5, 6],[7, 8, 9]],
                         [[1, 2, 3],[4, 5, 6],[7, 8, 9]],
                         [[1, 2, 3],[4, 5, 6],[7, 8, 9]]]

matriz_tridimensional[1][1][2]=44
print(matriz_tridimensional[1][1][2])