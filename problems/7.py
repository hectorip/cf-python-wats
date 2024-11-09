# Funcionamiento de IF y de función find
name = "Wally"
text = "Wally está aquí"

# find devuelve el índice del substring
# find devuelve -1 si no encuentra nada

if text.find(name): # Espero un booleano
    print("Encontrado!")
else:
    print(":(")

# *args
# **kwargs
