#Alunos:                                  
#- Leonardo Balan                         
#- Gabriel Santos da Silva                
                                
# Problema do Caixeiro Viajante Resolvido 
# com a Busca em Profundidade em Python   


#Importação de bibliotecas
import time

#Classe que engloba todo o código de definições das funções
class Caixeiro_Viajante:
    def __init__(lista):
        lista.vertices = []  # Lista para armazenar os vértices do grafo
        lista.graph = None   # Matriz de adjacência para representar o grafo
        lista.iteracoes = 0  # Variável para armazenar o número de iterações

    # Lê os vértices do arquivo e armazena na lista
    def Ler_Vertices(lista, vertices_arq):
        with open(vertices_arq, 'r') as file:
            lista.vertices = [line.strip() for line in file]

    # Lê as arestas do arquivo e armazena na matriz de adjacência
    def Ler_Arestas(lista, arestas_arq):
        # Inicializa a matriz de adjacência
        lista.graph = [[float('inf') for _ in range(len(lista.vertices))] for _ in range(len(lista.vertices))]

        with open(arestas_arq, 'r') as file:
            for line in file:
                V_origem, V_destino, custo = line.strip().split()  # Lê os dados da aresta do arquivo
                V_origem_indice = lista.vertices.index(V_origem)   # Obtém o índice do vértice de origem
                V_destino_indice = lista.vertices.index(V_destino)  # Obtém o índice do vértice de destino
                custo = int(custo)
                lista.graph[V_origem_indice][V_destino_indice] = custo  # Preenche a matriz de adjacência com o custo da aresta
                lista.graph[V_destino_indice][V_origem_indice] = custo  # A matriz é simétrica para grafos não direcionados

    def Busca_Profundidade(lista, V_origem, visitado, caminho, custo, min_custo, min_caminho, max_iteracoes):
        if lista.iteracoes >= max_iteracoes:
            return  # Interrompe a busca se atingir o número máximo de iterações

        print(f"Visitando Vértice {lista.vertices[V_origem]} - Caminho: {caminho} - Custo: {custo}")
        lista.iteracoes += 1  # Incremento do número de iterações

        visitado[V_origem] = True
        caminho.append(V_origem)

        if len(caminho) == len(lista.vertices):
            if custo + lista.graph[V_origem][caminho[0]] < min_custo[0]:
                min_custo[0] = custo + lista.graph[V_origem][caminho[0]]
                min_caminho[0] = caminho.copy()
        # Itera sobre os próximos vértices possíveis a partir do vértice de origem (V_origem)
        for proximo_vertice in range(len(lista.vertices)):
            if not visitado[proximo_vertice] and lista.graph[V_origem][proximo_vertice] != float('inf'):
                lista.Busca_Profundidade(proximo_vertice, visitado.copy(), caminho.copy(), custo + lista.graph[V_origem][proximo_vertice], min_custo, min_caminho, max_iteracoes)
   
  # Chama as funções definidas acima para resolver o Caixeiro Viajante
    def Resolve_Caixeiro(lista, V_inicial, max_iteracoes):
        lista.iteracoes = 0  # Reinicia o contador de iterações
        visitado = [False] * len(lista.vertices)
        caminho = []
        min_custo = [float('inf')]
        min_caminho = [[]]

        # Calcular tempo de execução
        start_time = time.time()
      
        # Chama a busca em profundidade
        lista.Busca_Profundidade(V_inicial, visitado, caminho, 0, min_custo, min_caminho, max_iteracoes)
      
        # Termina de contar o tempo de execução
        end_time = time.time()
        print("\n====================================================")
        print(f"\nTempo de Execução: {end_time - start_time} segundos")
        print(f"Número total de Iterações: {lista.iteracoes}")

        return min_caminho[0], min_custo[0]

# Arquivos de entrada
Resul = Caixeiro_Viajante()
Resul.Ler_Vertices(input("Digite o nome do arquivo de Vértices: "))
Resul.Ler_Arestas(input("\nDigite o nome do arquivo de Arestas: "))
max_iteracoes = int(input("\nDigite o Nº máximo de iterações desejado: "))
print("\n")

# Vértice Inicial (Sempre o primeiro do arquivo de vértices)
V_inicial = 0
# O menor caminho e menor custo receberão a resolução (melhores valores)
min_caminho, min_custo = Resul.Resolve_Caixeiro(V_inicial, max_iteracoes)

if min_custo != float('inf'):
    # Imprime o menor caminho e menor custo encontrado
    print(f"\nMenor caminho: {[Resul.vertices[i] for i in min_caminho] + [Resul.vertices[V_inicial]]}")
    print(f"Custo do Caminho: {min_custo}")
    print("\n====================================================")
else:
    # Se não houver solução para o problema, imprime isso
    print("\nNão há solução para o problema do caixeiro viajante.")