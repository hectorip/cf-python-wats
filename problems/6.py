# Corto circuito de operadores lógicos


def division(a, b):
    print(f"Calculando {a} / {b}")
    return a / b

# Short-circuit

# and
# or

if division(2,4) < 100 and False and division(1, 3) < 0 and division(1, 0) > 0:
    print("Esto terminó bien")
else:
    print("BOOM!")

print("BOOM!")

