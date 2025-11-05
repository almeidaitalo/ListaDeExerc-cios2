"""
2) Suponha que, no problema de busca por padrão em uma cadeia, seja possível
incluir em um padrão P um caracter especial, digamos #, que indica a possibilidade de casamentos com zero ou mais caracteres consecutivos do
texto. Elabore um algoritmo para dado um padrão que inclui zero ou mais
caracteres especiais não consecutivos, e um texto, identificar se o padrão
ocorre ou não no texto. A sua solução deve incluir o algoritmo em pseudolinguagem, o cálculo da complexidade de seu algoritmo e a implementação do
seu algoritmo.
"""

def padrao_ocorre(pattern: str, text: str) -> bool:
    m = len(pattern)
    n = len(text)

    # DP[i][j] = True se pattern[:i] casa com text[:j]
    DP = [[False] * (n + 1) for _ in range(m + 1)]
    DP[0][0] = True

    # Preencher primeira coluna (text vazio)
    for i in range(1, m + 1):
        if pattern[i - 1] == '#':
            DP[i][0] = DP[i - 1][0]
        else:
            DP[i][0] = False

    # Preencher o resto
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if pattern[i - 1] != '#':
                DP[i][j] = DP[i - 1][j - 1] and (pattern[i - 1] == text[j - 1])
            else:
                # '#' pode casar com vazio OU comer mais um char do texto
                DP[i][j] = DP[i - 1][j] or DP[i][j - 1]

    # Agora, checar se o padrão inteiro (i = m)
    # casou com QUALQUER prefixo de text (j = 0..n)
    for j in range(n + 1):
        if DP[m][j]:
            return True
    return False


# Pequenos testes
if __name__ == "__main__":
    print(padrao_ocorre("ab#cd", "xxabZZcdyy"))   # True
    print(padrao_ocorre("a#b", "acccb"))         # True
    print(padrao_ocorre("a#b", "ab"))            # True (# casa vazio)
    print(padrao_ocorre("a#b", "acccx"))         # False
    print(padrao_ocorre("#abc", "123abc456"))    # True
    print(padrao_ocorre("abc#", "xxabc123"))     # True
    print(padrao_ocorre("abc", "zzab"))          # False
