import re

texto = " -Esto- -- es un ejemplo, de una palabra Rara! ¿Y aquí hay otra palabra99? Pero algunas no cumplen con este criterio."

# Define una expresión regular que busca palabras con caracteres diferentes antes y después.
patron = r'(?<=[\W\s])\w+(?=[\W\s])'

# Busca las coincidencias en el texto.
coincidencias = re.findall(patron, texto)

# Itera sobre las coincidencias y verifica si tienen caracteres diferentes antes y después.
for palabra in coincidencias:
    print(f"Palabra con caracteres diferentes antes y después: {palabra}")


