import re

texto = "Esta es una cadena con 123 números y también algunas palabras 4567890."

# Define una expresión regular para encontrar números en el texto.
patron = r'\d+'

# Utiliza re.sub para eliminar los números del texto.
texto_sin_numeros = re.sub(patron, '', texto)

numeros = re.findall(patron, texto)

# Imprime el texto resultante sin números.
print("Texto sin números:", texto_sin_numeros)
print("numeros°:", numeros)

