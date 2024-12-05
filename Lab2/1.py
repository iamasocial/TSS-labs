import numpy as np
import matplotlib.pyplot as plt

m = 2.0        # масса
v_h = 0        # коэффициент демпфирования
k = 16.0       # жесткость
x0 = 1.0       # начальное положение
v = 0.0        # начальная скорость
f = lambda t: 3 * np.sin(4 * t)  # внешняя сила

T = 50.0       # общее время моделирования
dt = 0.01      # шаг по времени
N = int(T / dt)  # количество временных шагов

t_values = np.linspace(0, T, N)
x1_values = np.zeros(N)  # для x(t)
x2_values = np.zeros(N)  # для x'(t)

x1_values[0] = x0
x2_values[0] = v

for i in range(1, N):
    x1_values[i] = x1_values[i-1] + dt * x2_values[i-1]
    x2_values[i] = x2_values[i-1] + dt * (f(t_values[i-1]) - v_h * x2_values[i-1] - k * x1_values[i-1]) / m

plt.figure(figsize=(12, 6))
plt.plot(t_values, x1_values, label='x(t) position', color='blue')
plt.plot(t_values, x2_values, label="x'(t) velocity", color='red', linestyle='--')
plt.title('Position and Velocity of the Oscillator')
plt.xlabel('Time t')
plt.ylabel('Values')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
