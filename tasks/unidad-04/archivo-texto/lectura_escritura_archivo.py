#1. Escritura en archivo de texto
# Abre el archivo 'my_notes.txt' en modo escritura ('w').
# Si el archivo no existe, lo crea; si ya existe, sobrescribe el contenido.
with open("my_notes.txt", "w") as file:
    # Escribe tres líneas de texto en el archivo.
    file.write("Aprendiendo a trabajar con archivos en Python.\n")
    file.write("Usando metodo 'write' para escribir datos en el archivo.\n")
    file.write("El uso de 'with' facilita la gestión de archivos.\n")

# 2. Lectura del archivo de texto
# Abre el archivo 'my_notes.txt' en modo lectura ('r').
with open("my_notes.txt", "r") as file:
    # Lee el archivo línea por línea.
    for line in file:
        # Imprime cada línea eliminando saltos de línea innecesarios al final.
        print(line.strip())


