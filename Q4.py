import math

infinito = float('inf')  # Representa um valor infinito para limites superiores

def copiaParaFinal(caminho_atual, caminho_final, N):
    """
    Copia o caminho percorrido atual para o caminho final de solução,
    garantindo que o caminho finalize na cidade inicial.
    """
    caminho_final[:N + 1] = caminho_atual[:]
    caminho_final[N] = caminho_atual[0]

def primeiroMinimo(matriz, i, N):
    """
    Retorna o menor custo (aresta) saindo da cidade i
    """
    minimo = infinito
    for k in range(N):
        if matriz[i][k] < minimo and i != k:
            minimo = matriz[i][k]
    return minimo

def segundoMinimo(matriz, i, N):
    """
    Retorna o segundo menor custo (aresta) saindo da cidade i
    """
    primeiro, segundo = infinito, infinito
    for j in range(N):
        if i == j:
            continue
        if matriz[i][j] <= primeiro:
            segundo = primeiro
            primeiro = matriz[i][j]
        elif matriz[i][j] < segundo and matriz[i][j] != primeiro:
            segundo = matriz[i][j]
    return segundo

def caixeiroRecursivo(matriz, limite, peso_atual, nivel, caminho_atual, visitado, resultado_final, caminho_final, N):
    """
    Função recursiva principal do Branch and Bound:
  
    """
    # Caso base: todas as cidades foram visitadas, fecha o ciclo retornando à cidade inicial
    if nivel == N:
        if matriz[caminho_atual[nivel - 1]][caminho_atual[0]] != 0:
            resultado = peso_atual + matriz[caminho_atual[nivel - 1]][caminho_atual[0]]
            # Atualiza solução se custo menor for encontrado
            if resultado < resultado_final[0]:
                copiaParaFinal(caminho_atual, caminho_final, N)
                resultado_final[0] = resultado
        return

    # Explora os ramos ainda não visitados
    for i in range(N):
        if (matriz[caminho_atual[nivel - 1]][i] != 0 and not visitado[i]):
            temp = limite  # Salva limite atual para restauração posterior
            peso_atual += matriz[caminho_atual[nivel - 1]][i]  # Adiciona custo da próxima cidade

            # Atualiza o limite inferior com base nos mínimos locais
            if nivel == 1:
                limite -= ((primeiroMinimo(matriz, caminho_atual[nivel - 1], N) + primeiroMinimo(matriz, i, N)) / 2)
            else:
                limite -= ((segundoMinimo(matriz, caminho_atual[nivel - 1], N) + primeiroMinimo(matriz, i, N)) / 2)

            # Só continua a explorar se o custo total estimado for melhor que o resultado atual
            if limite + peso_atual < resultado_final[0]:
                caminho_atual[nivel] = i
                visitado[i] = True
                caixeiroRecursivo(matriz, limite, peso_atual, nivel + 1, caminho_atual, visitado, resultado_final, caminho_final, N)

            # Restaura peso e limite para backtracking
            peso_atual -= matriz[caminho_atual[nivel - 1]][i]
            limite = temp

            # Atualiza vetor visitado para o estado anterior
            visitado = [False] * len(visitado)
            for j in range(nivel):
                if caminho_atual[j] != -1:
                    visitado[caminho_atual[j]] = True

def caixeiroViajante(matriz):
    """
    Inicializa e executa o algoritmo Branch and Bound para o TSP.
    """
    N = len(matriz)
    limite = 0
    caminho_atual = [-1] * (N + 1)  # Armazena caminho atual temporário
    visitado = [False] * N
    caminho_final = [None] * (N + 1)  # Armazena melhor caminho encontrado
    resultado_final = [infinito]  # Melhor resultado encontrado (mutável)

    # Calcula limite inicial baseado nos mínimos de cada cidade
    for i in range(N):
        limite += (primeiroMinimo(matriz, i, N) + segundoMinimo(matriz, i, N))

    limite = math.ceil(limite / 2)
    visitado[0] = True  # Cidade inicial marcada como visitada
    caminho_atual[0] = 0  # Começa a partir da cidade 0

    caixeiroRecursivo(matriz, limite, 0, 1, caminho_atual, visitado, resultado_final, caminho_final, N)

    print("Custo minimo:", resultado_final[0])
    print("Melhor caminho encontrado:", caminho_final)

# Exemplo de uso:
matriz_adj = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

caixeiroViajante(matriz_adj)

