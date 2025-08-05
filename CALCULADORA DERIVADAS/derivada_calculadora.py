import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

# Habilitar impresión paso a paso
sp.init_printing(use_unicode=True)

# Entrada del usuario
expresion_input = input("Ingresa una función para derivar (en x):\nEjemplo: x**2 + sqrt(x) + 1/x\n\nf(x) = ")

# Definir variable simbólica
x = sp.Symbol('x')

# Parsear expresión del usuario
try:
    funcion = sp.sympify(expresion_input)
except sp.SympifyError:
    print("❌ Error: La expresión no se pudo entender.")
    exit()

# Derivar
derivada = sp.diff(funcion, x)

# Mostrar procedimiento paso a paso
print("\n✅ Derivación paso a paso:\n")
pasos = sp.simplify(sp.derive_by_array(funcion, x, evaluate=False))
sp.pprint(pasos[0])

# Mostrar derivada final
print("\n🧮 Derivada simplificada final:")
sp.pprint(derivada)

# Gráfica
x_vals = np.linspace(-10, 10, 1000)
f_lambdified = sp.lambdify(x, funcion, modules=['numpy'])
d_lambdified = sp.lambdify(x, derivada, modules=['numpy'])

plt.figure(figsize=(10, 5))
plt.plot(x_vals, f_lambdified(x_vals), label='f(x)', linewidth=2)
plt.plot(x_vals, d_lambdified(x_vals), label="f'(x)", linestyle='--', linewidth=2)
plt.title("Gráfica de la función y su derivada")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(True)
plt.legend()
plt.show()
