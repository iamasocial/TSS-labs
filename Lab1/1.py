import numpy as np
import matplotlib.pyplot as plt


def func1(x):
    return np.exp(-x / 2)

def func2(x):
    return np.sin(3 * x)

def func3(x):
    return np.square(np.cos(5 * x))

functions = [func1, func2, func3]
function_names = ["exp(-x/2)", "sin(3x)", "cos^2(5x)"]
h_values = [0.01, 0.005, 0.001]
dist = [(0, np.pi / 2), (2, 10), (-3, 3)]


colors = {
    "line": ["darkorange", "purple", "teal"],
    "point": ["gold", "magenta", "cyan"]
}


def compute_function_values(functions, intervals, step):
    x_values = [np.arange(d[0], d[1], step) for d in intervals]
    y_values = [[func(x) for func in functions] for x in x_values]
    return x_values, y_values


h_original = 0.0001
x_original, y_original = compute_function_values(functions, dist, h_original)
x_values, y_values = zip(*[compute_function_values(functions, dist, h) for h in h_values])


fig, axes = plt.subplots(len(h_values), len(dist), figsize=(15, 10), constrained_layout=True)

for i, h in enumerate(h_values):
    for j, (interval, x_h) in enumerate(zip(dist, x_values[i])):
        ax = axes[i, j]

        
        for k, (func_name, line_color) in enumerate(zip(function_names, colors["line"])):
            ax.plot(
                x_original[j], y_original[j][k], label=f"{func_name} (original)",
                linestyle="-", linewidth=1, color=line_color
            )

        
        for k, (func_name, point_color) in enumerate(zip(function_names, colors["point"])):
            ax.scatter(
                x_h, y_values[i][j][k], label=f"{func_name} (h={h})",
                s=10, marker="o", color=point_color
            )

        
        ax.set_title(f"h={h}, interval={interval}")
        ax.legend(fontsize=8)
        ax.grid(True, linewidth=0.5)
        ax.set_xlabel("x", fontsize=10)
        ax.set_ylabel("y", fontsize=10)

plt.suptitle("Comparison of original and grid graphs of functions", fontsize=14)
plt.show()
