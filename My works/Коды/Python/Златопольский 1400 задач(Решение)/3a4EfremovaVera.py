import matplotlib.pyplot as plt

def plot_data(x, y):
    fig, ax1 = plt.subplots()

    # Построение гистограммы для x
    color = 'tab:blue'
    ax1.set_xlabel('x values')
    ax1.set_ylabel('Frequency', color=color)
    ax1.hist(x, bins=30, alpha=0.7, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    # Создание второго y-axes для рассеянного графика
    ax2 = ax1.twinx()
    color = 'tab:red'
    ax2.set_ylabel('y values', color=color)
    ax2.scatter(x, y, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # Для обеспечения плотного расположения графиков
    plt.show()

# Тестирование функции с различными наборами данных
import numpy as np

# Пример 1
x1 = np.random.randn(1000)
y1 = np.random.randn(1000)
plot_data(x1, y1)

# Пример 2
x2 = np.linspace(0, 10, 500)
y2 = np.sin(x2)
plot_data(x2, y2)
