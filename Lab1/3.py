import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, y0, t, h):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * f(t[i - 1], y[i - 1])
    return y

def centroid_euler_method(f, y0, t, h):
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(1, len(t)):
        y[i] = y[i - 1] + h * f(t[i - 1] + 0.5 * h, y[i - 1] + 0.5 * h * f(t[i - 1], y[i - 1]))
    return y


def f1(x, y):
    return 0.5 * y

def f2(x, y):
    return 2 * x + 3 * y

def euler_system(f, y0, t, h):
    y = np.zeros((len(t), len(y0)))
    y[0, :] = y0
    for i in range(1, len(t)):
        y[i, :] = y[i - 1, :] + h * f(t[i - 1], y[i - 1, :])
    return y

def c_euler_system(f, y0, t, h):
    y = np.zeros((len(t), len(y0)))
    y[0, :] = y0
    for i in range(1, len(t)):
        y[i, :] = y[i - 1, :] + h * f(t[i - 1] + 0.5 * h, y[i - 1, :] + 0.5 * h * f(t[i - 1], y[i - 1, :]))
    return y

def system1(t, y):
    x1, x2 = y
    return np.array([x2, -x1])

def system2(t, y):
    x1, x2 = y
    return np.array([x2, 4 * x1])


t = np.arange(0, 10, 0.025)


fig, axs = plt.subplots(4, 2, figsize=(12, 16))


y1 = euler_method(f1, y0=1, t=t, h=0.025)
y11 = centroid_euler_method(f1, y0=1, t=t, h=0.025)
axs[0, 0].plot(t, y1, label="Euler", color='black')
axs[0, 1].plot(t, y11, label="Centroid Euler", color='black')


y2 = euler_method(f2, y0=-2, t=t, h=0.025)
y22 = centroid_euler_method(f2, y0=-2, t=t, h=0.025)
axs[1, 0].plot(t, y2, label="Euler", color='black')
axs[1, 1].plot(t, y22, label="Centroid Euler", color='black')


solution1 = euler_system(system1, y0=[1, 0], t=t, h=0.025)
solution11 = c_euler_system(system1, y0=[1, 0], t=t, h=0.025)
axs[2, 0].plot(t, solution1[:, 0], label="x1(t)", color='black')
axs[2, 0].plot(t, solution1[:, 1], label="x2(t)", linestyle="--", color='black')
axs[2, 1].plot(t, solution11[:, 0], label="x1(t)", color='black')
axs[2, 1].plot(t, solution11[:, 1], label="x2(t)", linestyle="--", color='black')


solution2 = euler_system(system2, y0=[1, 1], t=t, h=0.025)
solution22 = c_euler_system(system2, y0=[1, 1], t=t, h=0.025)
axs[3, 0].plot(t, solution2[:, 0], label="x1(t)", color='black')
axs[3, 0].plot(t, solution2[:, 1], label="x2(t)", linestyle="--", color='black')
axs[3, 1].plot(t, solution22[:, 0], label="x1(t)", color='black')
axs[3, 1].plot(t, solution22[:, 1], label="x2(t)", linestyle="--", color='black')

titles = [
    "Euler Method: y' = 1/2 * y",
    "Centroid Euler Method: y' = 1/2 * y",
    "Euler Method: y' = 2x + 3y",
    "Centroid Euler Method: y' = 2x + 3y",
    "Euler Method: System 1",
    "Centroid Euler Method: System 1",
    "Euler Method: System 2",
    "Centroid Euler Method: System 2",
]

for ax, title in zip(axs.flat, titles):
    ax.set_title(title)
    ax.set_xlabel("t")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(True)

plt.tight_layout()
plt.show()
