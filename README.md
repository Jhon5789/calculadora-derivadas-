"""
Calculadora de Derivadas paso a paso

Cómo usar:
1. Instala dependencias:
   pip install sympy matplotlib numpy

2. Ejecuta este archivo:
   python calculadora_derivada.py

3. Ingresa tu función en la consola cuando se te pida.
"""

import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

def main():
    sp.init_printing(use_unicode=True)
    x = sp.Symbol('x')

    expresion = input("Ingresa una función para derivar en x (ejemplo: x**2 + sqrt(x) + 1/x):\n\nf(x) = ")

    try:
        funcion = sp.sympify(expresion)
    except sp.SympifyError:
        print("❌ No se pudo entender la expresión. Intenta de nuevo.")
        return

    derivada = sp.diff(funcion, x)

    print("\n✅ Derivación paso a paso:\n")
    pasos = sp.simplify(sp.derive_by_array(funcion, x, evaluate=False))
    sp.pprint(pasos[0])

    print("\n🧮 Derivada simplificada final:")
    sp.pprint(derivada)

    x_vals = np.linspace(-10, 10, 1000)
    f_lamb = sp.lambdify(x, funcion, 'numpy')
    d_lamb = sp.lambdify(x, derivada, 'numpy')

    plt.figure(figsize=(10,5))
    plt.plot(x_vals, f_lamb(x_vals), label='f(x)')
    plt.plot(x_vals, d_lamb(x_vals), label="f'(x)", linestyle='--')
    plt.title("Función y su derivada")
    plt.axhline(0, color='black', lw=0.5)
    plt.axvline(0, color='black', lw=0.5)
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
