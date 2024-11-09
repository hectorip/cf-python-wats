# Representación de valores en el intérprete de Python

a = 200
b = 3

x = a * b  # 6
y = b * a  # 6

# python interning
# Python caches integer objects in the range [-5, 256]

print(x is y)  # True 
