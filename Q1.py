#1) Elabore um algoritmo para resolver o problema de agendamento de eventos com complexidade O(n log n)


from typing import List, Tuple

# Cada evento é uma tupla (inicio, fim). Ex.: (1, 4)
Event = Tuple[int, int]

def agendar_max_eventos(eventos: List[Event]) -> List[Event]:
    """
    Estratégia gulosa: ordenar por horário de término e selecionar compatíveis.

    Complexidade:
        - Ordenação: O(n log n)
        - Varrida/seleção: O(n)
        - Total: O(n log n)
    """
    if not eventos:
        return []

    # Ordena por fim crescente; em empate, pelo início
    eventos_ordenados = sorted(eventos, key=lambda e: (e[1], e[0]))

    selecionados: List[Event] = []
    fim_ultimo = float("-inf")

    for inicio, fim in eventos_ordenados:
        # Usa >= para permitir eventos encostando (fim == início)
        if inicio >= fim_ultimo:
            selecionados.append((inicio, fim))
            fim_ultimo = fim

    return selecionados


# Exemplo de uso
if __name__ == "__main__":
    eventos = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    solucao = agendar_max_eventos(eventos)
    print("Selecionados:", solucao)  
    
    # Ex.: [(1, 4), (5, 7), (8, 9)]
