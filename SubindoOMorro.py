#Alunos:                                  
#- Leonardo Balan                         
#- Gabriel Santos da Silva                

# Problema do Caixeiro Viajante Resolvido 
# com a heurística Subindo o Morro em Python 


#Importação de bibliotecas
import itertools 
import time

# Função para ler os vértices do arquivo e retornar uma lista de vértices
def ler_arquivo_vertices(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        vertices = [linha.strip() for linha in arquivo.readlines()]
    return vertices
# Função para ler as arestas do arquivo e retornar uma lista de tuplas (aresta, custo)
def ler_arquivo_arestas(nome_arquivo):
    with open(nome_arquivo, 'r') as arquivo:
        arestas = [linha.split() for linha in arquivo.readlines()]
    return [((origem, destino), int(custo)) for origem, destino, custo in arestas]
# Função para calcular o custo total de uma rota do grafo
def calcular_custo_rota(rota, grafo):
    custo_total = 0
    for i in range(len(rota) - 1):
        origem, destino = rota[i]
        if (origem, destino) in grafo:
            custo_total += grafo[(origem, destino)]
    # Se a aresta não existir, a rota não é válida
        else:
            return float('inf')
    # Adiciona o custo para voltar ao vértice de origem
    origem, destino = rota[-1]
    if (origem, destino) in grafo:
        custo_total += grafo[(origem, destino)]
    else:
        return float('inf')
    return custo_total
# Implementação da heurística Subindo o Morro
def subindo_o_morro(grafo, vertices, max_iteracoes):
    primeiro_vertice = vertices[0] # Vértice de Origem sempre o 1º do arquivo
    restantes_vertices = vertices[1:]
  
    # Inicializa das variáveis
    melhor_rota = []
    melhor_custo = float('inf')
    total_iteracoes = 0  
    # Loop sobre todas as permutações possíveis dos vértices restantes
    for permutacao in itertools.permutations(restantes_vertices):
        total_iteracoes += 1  # Incrementa a contagem a cada iteração
        rota_completa = [(primeiro_vertice, permutacao[0])] + list(zip(permutacao, permutacao[1:])) + [(permutacao[-1], primeiro_vertice)]  # Adiciona o retorno ao vértice de origem  
        custo_rota = calcular_custo_rota(rota_completa, grafo) # Criando a rota completa para a permutação atual
        if custo_rota < melhor_custo:
            melhor_custo = custo_rota
            melhor_rota = rota_completa

            # Imprime a execução de cada melhor iteração atualizada
            print(f"Iteração {total_iteracoes}: Melhor rota atual: {[v for v, _ in melhor_rota]}, \nMelhor custo atual: {melhor_custo}")

        # Verifica se atingiu o número máximo de iterações
        if total_iteracoes >= max_iteracoes:
            print(f"\nAtingido o número máximo de iterações ({max_iteracoes}). Abortando a busca.")
            break

    return melhor_rota, melhor_custo, total_iteracoes

# Arquivos de entrada
arquivo_vertices = input("Digite o nome do arquivo de Vértices: ")
arquivo_arestas =  input("\nDigite o nome do arquivo de Arestas: ")
max_iteracoes = int(input("\nDigite o Nº máximo de iterações desejado: "))
print("\n")

# Leitura dos dados
vertices = ler_arquivo_vertices(arquivo_vertices)
arestas = ler_arquivo_arestas(arquivo_arestas)

# Construção do grafo
grafo = {}
for (origem, destino), custo in arestas:
    grafo[(origem, destino)] = custo
    grafo[(destino, origem)] = custo  # Adiciona aresta de volta para grafos não direcionados

if not vertices or not arestas:
    print("Erro: Certifique-se de que os arquivos de entrada contêm dados válidos.")
else:
    # Medição do tempo de execução
    start_time = time.time()

    # Aplicação da heurística Subindo o Morro passando os devidos parâmetros
    melhor_rota, melhor_custo, total_iteracoes = subindo_o_morro(grafo, vertices, max_iteracoes)

    # Fim da medição do tempo de execução
    end_time = time.time()
    elapsed_time = end_time - start_time

    if melhor_rota:
        # Imprime a rota, tempo de exec, custo, iterações no formato feito
        print("\n====================================================")
        print("\nTempo de execução:", elapsed_time, "segundos")
        print("Número total de iterações:", total_iteracoes)
        print("\nMenor Caminho:", [v for v, _ in melhor_rota] + [vertices[0]])
        print("Custo do Caminho:", melhor_custo)
     
        print("\n====================================================")
    else:
        # Se não houver solução para o problema, imprime isso
        print("Não foi possível encontrar uma rota. Verifique os dados de entrada.")