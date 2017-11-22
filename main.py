with open("inst1.dat") as arquivo: # abertura do arquivo
    primeira_linha = next(arquivo).split(' ')
    quant_nodos, quant_arestas = int(primeira_linha[0]), int(primeira_linha[1]) #extração da primeira linha

    matriz = [[0 for x in range(quant_nodos)] for x in range(quant_nodos)] #criação da matriz de acordo com os
                                        #dados da primeira linha
    for linha in arquivo: #Valores sendo atribuidos a matriz
        linha = linha.split(' ')
        matriz[int(linha[0])][int(linha[1])] = int(linha[2])

print(matriz)

