import re

# Texto tokenizado
tokens = ["-hello", "example", "hello_", "test", "%%exam-ple--", "word@"]

# Definir una expresión regular para eliminar caracteres especiales al principio o al final de la palabra
pattern = r'^[^a-zA-Z0-9]*|[^a-zA-Z0-9]*$'

# Filtrar las palabras eliminando los caracteres especiales al principio o al final
filtered_tokens = [re.sub(pattern, '', token) for token in tokens]

# Resultado
print(filtered_tokens)


# Texto tokenizado
tokens = ["-hello", "example", "helloi/44", "78", "test", "exam-ple", "word@", "isGood", "goodbye", "2022","3d-5"]

# Definir una expresión regular para eliminar números
pattern = r'\b\d+\b'

# Filtrar las palabras eliminando los números
filtered_tokens = [re.sub(pattern, '', token) for token in tokens]

# Resultado
print(filtered_tokens)


# Texto tokenizado
tokens = ["-hello", "example", "mpg4", "mpg-4", "test", "@special!", "word@", "123"]

# Modificar el patrón para no eliminar números en palabras como "mpg4" o "mpg-4"
pattern = r'(?<=[a-zA-Z])\d+|\d+(?=[a-zA-Z])|\d+|\b[0-9]+[a-zA-Z0-9]+|[a-zA-Z0-9]+[0-9]+\b'

# Filtrar las palabras eliminando los caracteres especiales
filtered_tokens = [re.sub(pattern, '', token) for token in tokens]

# Resultado
print(filtered_tokens)


