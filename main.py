
def dijkstra2(matrix,m,x):
    tabela = [[0 for k in range(m)] for k in range(1)]
    nuvem = []
    nuvem.append(x)
    pos_menor = 0
    for j in range(m):
        tabela[0][j] = matrix[x][j]
    mini = 999
    for x in range(m - 1):
        mini = 999
        for j in range(m):
            print("{0} \t {1} \t {2}".format(tabela, j, nuvem))
            if tabela[0][j] <= mini and tabela[0][j] > 0 and j not in nuvem:
                mini = tabela[0][j]
                pos_menor = j
        nuvem.append(pos_menor)
        for j in range(m):
            if tabela[0][j] > tabela[0][pos_menor] + matrix[pos_menor][j]:
                tabela[0][j] = tabela[0][pos_menor] + matrix[pos_menor][j]
    print("The shortest path", nuvem)
    print("The tabela to various vertices in order", tabela)
#vertex should start with zero
#if you are giving weight above 999 adjust min in program
#result will be the shortest path and the distace to each vertex from source vertex in order
def dijkstra(matrix,m,n):
    k=int(input("Enter the source vertex"))
    cost=[[0 for x in range(m)] for x in range(1)]
    offsets = []
    offsets.append(k)
    elepos=0
    for j in range(m):
        cost[0][j]=matrix[k][j]
    mini=999
    for x in range (m-1):
        mini=999
        for j in range(m):
            print("{0} \t {1} \t {2}".format(cost, j, offsets))
            if cost[0][j]<=mini and j not in offsets and cost[0][j]> 0:
                mini=cost[0][j]
                elepos=j
                print(elepos)
        offsets.append(elepos)
        print("\n")
        for j in range (m):
            if cost[0][j] >cost[0][elepos]+matrix[elepos][j]:
                cost[0][j]=cost[0][elepos]+matrix[elepos][j]
    print("The shortest path",offsets)
    print("The cost to various vertices in order",cost)

def main():
    with open("inst1.dat") as arquivo:  # abertura do arquivo
        primeira_linha = next(arquivo).split(' ')
        quant_nodos, quant_arestas = int(primeira_linha[0]), int(primeira_linha[1])  # extração da primeira linha

        matriz = [[0 for x in range(quant_nodos)] for x in range(quant_nodos)]  # criação da matriz de acordo com os
        # dados da primeira linha
        for linha in arquivo:  # Valores sendo atribuidos a matriz
            linha = linha.split(' ')
            matriz[int(linha[0])][int(linha[1])] = int(linha[2])
            matriz[int(linha[1])][int(linha[0])] = int(linha[2])

    print(matriz)

    continuar = True
    while continuar:
        #x = int(input("\nDigite o nodo inicial: "))
        #y = int(input("\nDigite o nodo final: "))
        #print(quant_nodos)
        dijkstra(matriz, quant_nodos, quant_nodos)
        opcao = 0
        #while opcao != 1 or opcao != 2:
            #print("\n\nOpção 1: Execução simples. Retorna a menor distancia entre o nodo x e nodo y")
            #print("Opção 2: Execução completa. Mstra o estado do programa a cada iteração ")

            #opcao = int(input("\nDigite sua opção: "))
def main2():
    print("Dijkstras algorithum graph using matrix representation \n")
    n=int(input("number of elements in row: "))
    m=int(input("number of elements in column: "))
    #print("enter the values of the matrix")
    matrix=[[0 for x in range(m)] for x in range(n)]
    for i in range (n):
        for j in range (m):
            if matrix[j][i] == 0:
                matrix[i][j]=int(input("enter the values of the matrix[{0}][{1}]: ".format(i,j)))
            else:
                matrix[i][j] = matrix[j][i]
    print(matrix)
    dijkstra(matrix,m,n)
main()

main()

