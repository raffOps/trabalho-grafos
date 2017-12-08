infinito = 9999
nome_arquivo = "inst3.dat"

def dijkstra(matrix, quant_nodos, x, y, opcao):
    tabela=[0 for nodo in range(quant_nodos)] # Criação da tabela de prioridade
    nuvem = [] # Criacao da nuvem
    nuvem.append(x) # Adiciona o nodo inicial a nuvem
    for j in range(quant_nodos): # Inicializa a tabela de prioridades com as distancias de x ate seus vizinhos diretos
        tabela[j] = matrix[x][j]

    if opcao == 2:
        imprime_tabela(1, tabela, nuvem, x)

    for etapa in range(quant_nodos-1): # A quantidade total de etapas para completar a nuvem sera a
                                        # quantidades de nodos - 1
        mini = infinito # Distancia minima recebe um valor infinito
        for j in range(quant_nodos): # Identificar o nodos mais perto do nodo atual
            if tabela[j] <= mini and j not in nuvem: # Se o valor correspondente a j na tabela for menor que a
                                                        # distancia minima atual e j nao estiver na nuvem,
                                                        # entao mini eh atualizado com o valor de j na tabela e
                mini = tabela[j]
                elepos = j
        nuvem.append(elepos) # O nodo que estiver mais perto do nodo visitado anteriormente eh adicionado na nuvem
                                        # junto com a distancia entre eles
        if elepos == y and opcao == 1: # Se a opcao de saida for 1 e nodo adicionado na nuvem for y, entao a distancia
                                       #  é printada e programa eh finalizado
            print("Distância de {0} até {1}: {2}".format(x, y, mini))
            return
        for j in range(quant_nodos):
            if tabela[j] > tabela[elepos] + matrix[elepos][j]: # Atualizacao da tabela. Se o valor de j na tabela
                                                                # for maior que a distancia do ultimo
                                                                # nodo adicionado na nuvem + a distancia desse nodo para
                                                                # os seus vizinhos na matriz, então j é atualizado com
                                                                # esse valor menor

                tabela[j] = tabela[elepos] + matrix[elepos][j]

        if opcao == 2:#Printagem das saidas caso a opcao seja 2
            imprime_tabela(etapa + 2, tabela, nuvem, x)

def imprime_tabela(etapa, tabela, nuvem, x):
    tabela_copia = tabela.copy()
    for x in range(len(tabela_copia)): #Formatacao da tabela pra melhor vizualizacao na printagem
        if x in nuvem:
            tabela_copia[x] = str(x) + ": -"
        elif tabela_copia[x] == infinito:
            tabela_copia[x] = str(x) + ": Inf"
        else:
            tabela_copia[x] = str(x) + ": " + str(tabela_copia[x])
    print("-" * 190)
    print(
        "Etapa {0}\nNodo sendo visitado: {1} \t Distancia para {2}: {3} \nTabela: {4} \nNuvem: {5}".format(
            etapa, nuvem[-1], x, tabela[nuvem[-1]], tabela_copia, nuvem))


def main():
    with open(nome_arquivo) as arquivo:  # abertura do arquivo
        primeira_linha = next(arquivo).split(' ')
        quant_nodos, quant_arestas = int(primeira_linha[0]), int(primeira_linha[1])  # extracao da primeira linha

        matriz = [[0 for x in range(quant_nodos)] for x in range(quant_nodos)]  # criacao da matriz de acordo com os
        # dados da primeira linha
        for linha in arquivo:  # Valores sendo atribuidos a matriz
            linha = linha.split(' ')
            matriz[int(linha[0])][int(linha[1])] = int(linha[2])
            matriz[int(linha[1])][int(linha[0])] = int(linha[2])

    for linha in range(quant_nodos): # Troca valores 0 por valor que representa o infinito
        for coluna in range(quant_nodos):
            if matriz[linha][coluna] == 0:
                matriz[linha][coluna] = infinito

    #for linha in matriz:
     #   print(linha)

    continuar = True
    while continuar:
        x = int(input("\nDigite o nodo inicial: "))
        y = int(input("Digite o nodo final: "))
        matriz[x][x] = 0
        opcao = 0
        while opcao != 1 and opcao != 2:
            print("\nOpção 1: Execução simples. Retorna a menor distancia entre o nodo x e nodo y")
            print("Opção 2: Execução completa. Mostra o estado do programa a cada iteração ")
            opcao = int(input("\nDigite sua opção: "))
        dijkstra(matriz, quant_nodos, x, y, opcao)
        continuar = int(input("\nExecutar o dijkstra novamente? 1 para sim, 0 para Não: "))


main()