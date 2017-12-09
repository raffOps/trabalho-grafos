infinito = 9999

def dijkstra(matrix, quant_nodos, x, y, opcao):
    """
    Calcula a distancia minima de um nodo inicial para qualquer outro nodo do grafo
    :param matrix:
    :param quant_nodos:
    :param x:
    :param y:
    :param opcao:
    :return:
    """
    tabela=[0 for nodo in range(quant_nodos)] # Criação da tabela de prioridade
    nuvem = [] # Criacao da nuvem para percorrimento
    nuvem.append(x) # Adiciona o nodo inicial a nuvem

    if x == y and opcao == 1:  # Se a opcao de saida for 1 e nodo adicionado na nuvem for y, entao a distancia
        #  é printada e programa eh finalizado
        print('Distancia de {0} até {1}: {2}'.format(x, y, 0))
        return

    for j in range(quant_nodos): # Inicializa a tabela de prioridades com as distancias de x ate seus vizinhos diretos
        tabela[j] = matrix[x][j]

    if opcao == '2':
        imprime_dados('1', tabela, nuvem, x)

    for etapa in range(quant_nodos-1): # A quantidade total de etapas para completar a nuvem sera a
                                        # quantidades de nodos - 1
        mini = infinito # Distancia minima recebe um valor infinito
        for j in range(quant_nodos): # Identificar o nodo mais perto do nodo atual
            if tabela[j] <= mini and j not in nuvem: # Se o valor correspondente a j na tabela for menor que a
                                                        # distancia minima atual e j nao estiver na nuvem,
                                                        # entao mini eh atualizado com o valor de j na tabela e
                mini = tabela[j]
                elepos = j
        nuvem.append(elepos) # O nodo que estiver mais perto do nodo visitado anteriormente eh adicionado na nuvem
                                        # junto com a distancia entre eles
        if elepos == y and opcao == '1': # Se a opcao de saida for 1 e nodo adicionado na nuvem for y, entao a distancia
                                       #  é printada e programa eh finalizado
            print('Distancia de {0} até {1}: {2}'.format(x, y, mini))
            return
        for j in range(quant_nodos):
            if tabela[j] > tabela[elepos] + matrix[elepos][j]: # Atualizacao da tabela. Se o valor de j na tabela
                                                                # for maior que a distancia do ultimo
                                                                # nodo adicionado na nuvem + a distancia desse nodo para
                                                                # os seus vizinhos na matriz, então j é atualizado com
                                                                # esse valor menor

                tabela[j] = tabela[elepos] + matrix[elepos][j]

        if opcao == 2:#Printagem das saidas caso a opcao seja 2
            imprime_dados(etapa + 2, tabela, nuvem, x)

def imprime_dados(etapa, tabela, nuvem, x):
    """
     #Formatacao dos dados de saida pra melhor vizualizacao na printagem
    :param etapa:
    :param tabela:
    :param nuvem:
    :param x:
    :return:
    """
    tabela_string = '| '
    for k in range(len(tabela)):
        if k in nuvem:
            tabela_string += str(k) + ': - | '
        elif tabela[k] == infinito:
            tabela_string += str(k) + ': Inf | '
        else:
            tabela_string += str(k) + ': ' + str(tabela[k]) + ' | '
    print("-" * 170)
    print(
        'Etapa {0}\nNodo sendo visitado: {1} \t Distancia para {2}: {3} \n\nTabela: {4} \n\nNuvem: {5}'.format(
            etapa, nuvem[-1], x, tabela[nuvem[-1]], tabela_string, nuvem))


def main():
    try:
        arquivo = open(input('Digite o nome do arquivo: '))  # abertura do arquivo
    except FileNotFoundError:
        print('Arquivo nao encontrado')
    else:
        with arquivo:
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
            x = int(input('\nDigite o nodo inicial (entre 0 e {}): '.format(quant_nodos-1)))
            y = int(input('Digite o nodo final (entre 0 e {}): '.format(quant_nodos-1)))
            matriz[x][x] = 0
            opcao = 0
            while opcao != 1 and opcao != 2:
                print('\nOpção 1: Execucao simples. Retorna a menor distancia entre o nodo x e nodo y')
                print('Opção 2: Execucao completa. Mostra o estado do programa a cada iteracao ')
                opcao = int(input("\nDigite sua opcao: "))
            dijkstra(matriz, quant_nodos, x, y, opcao)
            print("-" * 170)
            continuar = int(input('\nExecutar o dijkstra novamente? 1 para sim, 0 para Não: '))


main()
