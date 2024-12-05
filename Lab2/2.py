import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve_banded

# Параметры
N = 300  # число шагов
a, b = 0.5, 1.0  # границы интервала
h = (b - a) / N  # шаг
x = np.linspace(a, b, N + 1)

# Инициализация коэффициентов
lower = np.zeros(N + 1)  # поддиагональ
main = np.zeros(N + 1)   # главная диагональ
upper = np.zeros(N + 1)  # наддиагональ
d = np.zeros(N + 1)      # правая часть

# Краевые условия
main[0], upper[0], d[0] = 2 + 1 / h, -1 / h, 6       # левое
main[N], lower[N], d[N] = 1 + 3 / h, -3 / h, -1     # правое

# Внутренние точки
xi = x[1:-1]
lower[1:-1] = 1 / h**2 + xi**2 / (2 * h)
main[1:-1] = -2 / h**2 - 2 / xi**2
upper[1:-1] = 1 / h**2 - xi**2 / (2 * h)
d[1:-1] = 1 + 4 / xi**2

# Формирование матрицы для solve_banded
ab = np.zeros((3, N + 1))
ab[0, 1:] = upper[:-1]    # наддиагональ
ab[1, :] = main           # главная диагональ
ab[2, :-1] = lower[1:]    # поддиагональ

# Решение системы
y = solve_banded((1, 1), ab, d)

# Построение графика
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y(x)', color='b')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.title('Finite difference solution')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
