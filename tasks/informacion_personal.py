#1. Un diccionario con información personal
informacion_personal = {
    "nombre": "Emilio Senguana",
    "edad": 24,
    "ciudad": "Santo Domingo de los Tsachilas",
    "profesion": "Tencnologo Mencion en Analisis de Sistemas"
}

#2. Acceder y Modificar Valores:
# Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
informacion_personal["ciudad"] = "Macas"  # Cambiamos de Santo Domingo de los Tsachilas a Morona Santiago

# Agregar una nueva clave-valor que represente la profesión
informacion_personal["profesion"] = "Ingeniero de Software"

#3. Verificar Existencia de Claves:
# Verificar si la clave "telefono" existe en el diccionario
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0959889745"  # Si no existe, se agrega un teléfono ficticio

#4. Eliminar una Clave:
# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

#5. Imprimir el Diccionario Final:
print("Diccionario final:", informacion_personal)
