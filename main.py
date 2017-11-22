def main():
    with open("inst1.dat") as arquivo: # abertura do arquivo
        primeira_linha = next(arquivo).split(' ')
        quant_nodos, quant_arestas = int(primeira_linha[0]), int(primeira_linha[1]) #extração da primeira linha

        matriz = [[0 for x in range(quant_nodos)] for x in range(quant_nodos)] #criação da matriz de acordo com os
                                                                                #dados da primeira linha
        for linha in arquivo: #Valores sendo atribuidos a matriz
            linha = linha.split(' ')
            matriz[int(linha[0])][int(linha[1])] = int(linha[2])

    continuar = True
    while(continuar):
        x = int(input("\nDigite o nodo inicial: "))
        y = int(input("\nDigite o nodo final: "))

        opcao = 0
        while opcao != 1 or opcao != 2:
            print("\n\nOpção 1: Execução simples. Retorna a menor distancia entre o nodo x e nodo y")
            print("Opção 2: Execução completa. Mstra o estado do programa a cada iteração ")

            opcao = int(input("\nDigite sua opção: "))

            dikstra(matriz,x,y,opcao, quant_nodos)

def dikstra(matriz, x, y, opcao, quant_nodos):
    matriz_dikstra = list(range(quant_nodos))

    for x in range(quant_nodos - 1):
        matriz_dikstra.append(['-' for x in range(quant_nodos)])

    print(matriz_dikstra)
main()

