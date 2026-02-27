import numpy as np
import time
import matplotlib.pyplot as plt
from numba import njit

N     = 10_000_000
N_PY  = 10_000_000
MOD   = int(2**62)

# ===============================
# Python Puro — INT (int nativo, sem overflow)
# ===============================
def py_int_add(n):
    x = 1
    for i in range(n):
        x = (x * 3 + 7) % MOD
    return x

def py_int_mul(n):
    x = 3
    for i in range(n):
        x = (x * 3 + 7) % MOD
    return x

def py_int_div(n):
    x = n
    for i in range(1, n + 1):
        x = x // i + i
    return x

def py_int_sqrt(n):
    x = n
    for i in range(1, n + 1):
        x = int(x ** 0.5) + i
    return x

# ===============================
# Python Puro — FLOAT
# ===============================
def py_float_add(n):
    y = 1.0
    for i in range(n):
        y = y * 1.0000001 + 0.000001
    return y

def py_float_mul(n):
    y = 1.0000001
    for i in range(n):
        y = y * 1.0000001 + 0.000001
    return y

def py_float_div(n):
    y = 1.0
    for i in range(n):
        y = (y + 1.0000001) / 1.0000001
    return y

def py_float_sqrt(n):
    y = 2.0
    for i in range(n):
        y = y ** 0.5 + 1.0000001
    return y

# ===============================
# Numba — INT
# ===============================
@njit
def nb_int_add(n):
    x = np.int64(1)
    MOD = np.int64(2**62)
    for i in range(n):
        x = (x * np.int64(3) + np.int64(7)) % MOD
    return x

@njit
def nb_int_mul(n):
    x = np.int64(3)
    MOD = np.int64(2**62)
    for i in range(n):
        x = (x * np.int64(3) + np.int64(7)) % MOD
    return x

@njit
def nb_int_div(n):
    x = np.int64(n)
    for i in range(1, n + 1):
        x = x // np.int64(i) + np.int64(i)
    return x

@njit
def nb_int_sqrt(n):
    x = np.int64(n)
    for i in range(1, n + 1):
        x = np.int64(x ** 0.5) + np.int64(i)
    return x

# ===============================
# Numba — FLOAT
# ===============================
@njit
def nb_float_add(n):
    y = 1.0
    for i in range(n):
        y = y * 1.0000001 + 0.000001
    return y

@njit
def nb_float_mul(n):
    y = 1.0000001
    for i in range(n):
        y = y * 1.0000001 + 0.000001
    return y

@njit
def nb_float_div(n):
    y = 1.0
    for i in range(n):
        y = (y + 1.0000001) / 1.0000001
    return y

@njit
def nb_float_sqrt(n):
    y = 2.0
    for i in range(n):
        y = y ** 0.5 + 1.0000001
    return y

# ===============================
# Warm-up Numba
# ===============================
print("Compilando Numba (warm-up)...")
for fn in [nb_int_add, nb_int_mul, nb_int_div, nb_int_sqrt,
           nb_float_add, nb_float_mul, nb_float_div, nb_float_sqrt]:
    fn(1000)
print("Pronto! Iniciando benchmark...\n")

# ===============================
# Função de benchmark
# ===============================
def bench(fn, n, label=""):
    start = time.perf_counter()
    fn(n)
    elapsed = time.perf_counter() - start
    gops = (n / elapsed) / 1e9
    print(f"  {label:<30} {gops:.4f} G ops/s  ({elapsed:.3f}s)")
    return gops

ops = ["ADD", "MUL", "DIV", "SQRT"]

print(f"=== Python Puro — INT (GIPS)  [N={N_PY:,}] ===")
py_int = [bench(f, N_PY, ops[i]) for i, f in enumerate([py_int_add, py_int_mul, py_int_div, py_int_sqrt])]

print(f"\n=== Python Puro — FLOAT (GFLOPS)  [N={N_PY:,}] ===")
py_flt = [bench(f, N_PY, ops[i]) for i, f in enumerate([py_float_add, py_float_mul, py_float_div, py_float_sqrt])]

print(f"\n=== Numba — INT (GIPS)  [N={N:,}] ===")
nb_int = [bench(f, N, ops[i]) for i, f in enumerate([nb_int_add, nb_int_mul, nb_int_div, nb_int_sqrt])]

print(f"\n=== Numba — FLOAT (GFLOPS)  [N={N:,}] ===")
nb_flt = [bench(f, N, ops[i]) for i, f in enumerate([nb_float_add, nb_float_mul, nb_float_div, nb_float_sqrt])]

# ===============================
# Gráfico agrupado
# ===============================
x = np.arange(len(ops))
width = 0.2

fig, ax = plt.subplots(figsize=(13, 6))
fig.patch.set_facecolor("#0f0f0f")
ax.set_facecolor("#1a1a1a")

colors = {
    "py_int": "#e05c5c",
    "py_flt": "#e09c5c",
    "nb_int": "#5c9ee0",
    "nb_flt": "#5ce07a",
}

b1 = ax.bar(x - 1.5*width, py_int, width, label="Python INT (GIPS)",     color=colors["py_int"], alpha=0.9)
b2 = ax.bar(x - 0.5*width, py_flt, width, label="Python FLOAT (GFLOPS)", color=colors["py_flt"], alpha=0.9)
b3 = ax.bar(x + 0.5*width, nb_int, width, label="Numba INT (GIPS)",       color=colors["nb_int"], alpha=0.9)
b4 = ax.bar(x + 1.5*width, nb_flt, width, label="Numba FLOAT (GFLOPS)",   color=colors["nb_flt"], alpha=0.9)

for bars in [b1, b2, b3, b4]:
    for bar in bars:
        h = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, h + 0.005,
                f"{h:.3f}", ha="center", va="bottom",
                fontsize=7.5, color="white", fontweight="bold")

ax.set_xticks(x)
ax.set_xticklabels(ops, fontsize=13, color="white", fontweight="bold")
ax.set_ylabel("Giga Operações por Segundo", fontsize=11, color="#cccccc")
ax.set_title("GIPS vs GFLOPS — Python Puro vs Numba (JIT)\nADD · MUL · DIV · SQRT",
             fontsize=14, color="white", fontweight="bold", pad=15)

ax.tick_params(colors="white")
ax.spines[["top", "right", "left", "bottom"]].set_color("#333333")
ax.yaxis.label.set_color("#aaaaaa")
ax.grid(axis="y", color="#2a2a2a", linewidth=0.8)

ax.legend(loc="upper right", framealpha=0.3,
          facecolor="#111111", edgecolor="#444444",
          labelcolor="white", fontsize=9)

plt.tight_layout()
plt.savefig("benchmark_gips_gflops.png", dpi=150, bbox_inches="tight",
            facecolor=fig.get_facecolor())
plt.show()

print("\n=== Speedups Numba vs Python ===")
for i, op in enumerate(ops):
    print(f"  {op}  INT:  {nb_int[i]/py_int[i]:>8.1f}x  |  FLOAT: {nb_flt[i]/py_flt[i]:>8.1f}x")
