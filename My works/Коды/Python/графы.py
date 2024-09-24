import matplotlib.pyplot as plt
import random

# Создаем граф с не менее чем 11 вершинами
graph = {
    1: [2, 3, 4],
    2: [1, 3, 5],
    3: [1, 2, 4],
    4: [1, 3, 5, 6],
    5: [2, 4, 7],
    6: [4, 8],
    7: [5, 8],
    8: [6, 7, 9],
    9: [8, 10],
    10: [9, 11],
    11: [10]
}

# Добавим нумерацию к вершинам
numbered_graph = {f'V{vertex}': [f'V{neighbor}' for neighbor in neighbors] for vertex, neighbors in graph.items()}

# Рисуем граф
def draw_graph(graph):
    for vertex in graph:
        for neighbor in graph[vertex]:
            plt.plot([vertex, neighbor], [graph[vertex][0], graph[neighbor][0]], marker='o', color='b')

draw_graph(numbered_graph)
plt.title("Исходный граф")
plt.show()

# Алгоритм поиска Эйлерова цикла
def eulerian_cycle(graph):
    stack = [list(graph.keys())[0]]
    cycle = []

    while stack:
        current_vertex = stack[-1]

        if graph[current_vertex]:
            neighbor = graph[current_vertex].pop(0)
            stack.append(neighbor)
        else:
            cycle.append(stack.pop())

    return cycle[::-1]

# Поиск Эйлерова цикла
euler_cycle = eulerian_cycle(numbered_graph.copy())

# Выводим путь в консоли
print("Эйлеров цикл:", "->".join(euler_cycle))
