import numpy as np
import matplotlib.pyplot as plt


h_values = [0.01, 0.005]
dist = [(0, 1), (2, 15), (-5, 5)]


def func1(x):
    return np.exp(-x / 2)

def func2(x):
    return np.sin(3 * x**4 / 5)**3

def func3(x):
    return np.cos(x / (x + 1))**2

def func4(x):
    return np.log(x + np.sqrt(4 + x**2))

def func5(x):
    return x * np.arctan(2 * x) / (x**2 + 4)

functions = [func1, func2, func3, func4, func5]
function_names = ["exp(-x/2)", "sin(3x^4/5)^3", "cos^2(x/(x+1))", "log(x + sqrt(4 + x^2))", "x * arctan(2x) / (x^2 + 4)"]
line_colors = ["blue", "red", "green", "purple", "orange"]


def compute_derivatives(functions, h_values, dist):
    results = []
    for h in h_values:
        h_results = []
        for interval in dist:
            x = np.arange(interval[0], interval[1], h)
            derivatives = [np.diff(func(x)) / h for func in functions]
            h_results.append((x[:-1], derivatives))
        results.append(h_results)
    return results


derivatives = compute_derivatives(functions, h_values, dist)


for h_idx, h in enumerate(h_values):
    fig, axs = plt.subplots(len(functions), len(dist), figsize=(15, 10), sharex=True)

    for dist_idx, (interval, (x, funcs_derivatives)) in enumerate(zip(dist, derivatives[h_idx])):
        for func_idx, y_derivative in enumerate(funcs_derivatives):
            axs[func_idx, dist_idx].plot(
                x, y_derivative, label=f"h={h}", linewidth=1.5, color=line_colors[func_idx]
            )
            axs[func_idx, dist_idx].set_title(
                f"{function_names[func_idx]}, interval {interval}"
            )
            axs[func_idx, dist_idx].set_ylabel("y'")
            axs[func_idx, dist_idx].legend(fontsize=8)
            axs[func_idx, dist_idx].grid(True, linewidth=0.5)

    axs[-1, 0].set_xlabel("x")
    plt.tight_layout()
    plt.show()
