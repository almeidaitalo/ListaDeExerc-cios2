#3) Realize a implementação do algoritmo LCS utilizando a linguagem Python.

def lcs(X: str, Y: str):
    m = len(X)
    n = len(Y)

    # Tabela de tamanhos
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Preenche DP
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstruir a subsequência comum máxima
    i, j = m, n
    seq_reversa = []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            seq_reversa.append(X[i - 1])
            i -= 1
            j -= 1
        else:
            if dp[i - 1][j] >= dp[i][j - 1]:
                i -= 1
            else:
                j -= 1

    seq_reversa.reverse()
    lcs_seq = ''.join(seq_reversa)

    return dp[m][n], lcs_seq


# Teste 
if __name__ == "__main__":
    length, seq = lcs("ABCBDAB", "BDCABA")
    print("Tamanho:", length)  
    print("LCS:", seq)         
