#1) Elabore um algoritmo para resolver o problema de agendamento de eventos com complexidade O(n log n)

def agendar_eventos(eventos):
    # eventos é uma lista de tuplas (inicio, fim)
    eventos.sort(key=lambda x: x[1])  # Ordena pelo horário de término -> O(n log n)

    selecionados = []
    ultimo_fim = float('-inf')

    for inicio, fim in eventos:
        if inicio >= ultimo_fim:
            selecionados.append((inicio, fim))
            ultimo_fim = fim

    return selecionados


# Exemplo de uso
eventos = [(1, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
resultado = agendar_eventos(eventos)
print("Eventos selecionados:", resultado)
