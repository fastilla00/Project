import numpy as np
import matplotlib.pyplot as plt

# Создание массива значений x от -2π до 2π
x = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
y = np.tan(x)

# Создание фигуры и осей
fig, ax = plt.subplots()

# Построение графика
ax.plot(x, y, color='blue', linestyle='--', marker='o', label='y = tan(x)')

# Добавление заголовка
ax.set_title('График функции y = tan(x)')

# Добавление подписей к осям
ax.set_xlabel('x')
ax.set_ylabel('y')

# Установка масштаба осей
ax.set_xlim([-2 * np.pi, 2 * np.pi])
ax.set_ylim([-10, 10])

# Добавление сетки
ax.grid(True)

# Добавление легенды
ax.legend()

# Сохранение графика в файл
plt.savefig('/mnt/data/tan_graph.png')

# Отображение графика
plt.show()
