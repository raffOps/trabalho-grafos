infinito = 9999
#vertex should start with zero
#if you are giving weight above 999 adjust min in program
#result will be the shortest path and the distace to each vertex from source vertex in order
def dijkstra(matrix, quant_nodos, x, y, opcao):
    tabela=[0 for nodo in range(quant_nodos)] # Criação da tabela de prioridade
    nuvem = []
    nuvem.append(x) # Adiciona o nodo inicial a nuvem
    for j in range(quant_nodos): # Inicializa a tabela de prioridades com as distancias de x até seus vizinhos diretos
        tabela[j] = matrix[x][j]

    if opcao == 2:
        print(
            "Nodo sendo visitado: {0} \t Distancia para {1}: {2} \nTabela: {3} \nNuvem: {4}\n ".format(
                nuvem[-1], x, tabela[nuvem[-1]], imprime_tabela(tabela, nuvem), nuvem))

    for etapa in range(quant_nodos-1): # A quantidade total de etapas para completar a nuvem será a
                                        # quantidades de nodos - 1
        mini = infinito # Distancia mímima recebe um valor infinito
        for j in range(quant_nodos): # Identificar o nodos mais perto do nodo atual
            if tabela[j] <= mini and j not in nuvem: # Se o valor correspondente a j na tabela for menor que a
                                                        # distancia minima atual e j não estiver na nuvem,
                                                        # então mini é atualizado com o valor de j na tabela e
                mini = tabela[j]
                elepos = j
        nuvem.append(elepos) # O nodo que estiver mais perto do nodo visitado anteriormente é adicionado na nuvem
                                        # junto com a distancia entre eles
        if elepos == y and opcao == 1:
            print("Distância de {0} até {1}: {2}".format(x, y, mini))
            return
        for j in range(quant_nodos):
            if tabela[j] > tabela[elepos] + matrix[elepos][j]:
                tabela[j] = tabela[elepos] + matrix[elepos][j]
        if opcao == 2:
            print(
                "Nodo sendo visitado: {0} \t Distancia para {1}: {2} \nTabela: {3} \nNuvem: {4}\n ".format(
                    nuvem[-1], x, tabela[nuvem[-1]], imprime_tabela(tabela,nuvem),  nuvem))

def imprime_tabela(tabela, nuvem):
    tabela_copia = tabela.copy()
    for x in range(len(tabela_copia)):
        if x in nuvem:
            tabela_copia[x] = '-'
    return tabela_copia


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

    for linha in range(quant_nodos):
        for coluna in range(quant_nodos):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna] = infinito

    #print(matriz)
    continuar = True
    while continuar:
        x = int(input("\nDigite o nodo inicial: "))
        y = int(input("Digite o nodo final: "))
        matriz[x][x] = 0
        opcao = 0
        while opcao != 1 and opcao != 2:
            print("\nOpção 1: Execução simples. Retorna a menor distancia entre o nodo x e nodo y")
            print("Opção 2: Execução completa. Mstra o estado do programa a cada iteração ")
            opcao = int(input("\nDigite sua opção: "))
        dijkstra(matriz, quant_nodos, x, y, opcao)
        continuar = int(input("\nExecutar o dijkstra novamente? 1 para sim, 0 para Não: "))


main()