from openpyxl import Workbook

# PARTE 1: Crear diccionario y entrada de datos
# Crea un diccionario vacío llamado 'estudiantes'
# Usa un ciclo for para pedir 3 nombres y notas (convierte la nota a float)
# Guarda cada par nombre-nota en el diccionario

estudiantes = {}

for i in range(3):
    nombre = input(f"Nombre del estudiante {i+1}: ")
    nota = float(input(f"Nota del estudiante {i+1}: "))
    estudiantes[nombre] = nota

# PARTE 2: Crear archivo Excel
# Crea un nuevo libro de trabajo

libro = Workbook()

# Obtén la hoja activa

hoja = libro.active

# PARTE 3: Escribir encabezado
# Escribe "Aprobados (>=60)" en A1

hoja['A1'] = "Aprobados (>=60)"

# PARTE 4: Escribir aprobados con ciclo y condicional

fila = 2

# Usa un ciclo for para recorrer el diccionario
# Si la nota es >= 60, escribe el nombre en la columna A y aumenta 'fila'

for nombre, nota in estudiantes.items():
    if nota >= 60:
        hoja[f"A{fila}"] = nombre
        fila += 1

# PARTE 5: Guardar archivo
# Guarda el archivo como "ejercicio2.xlsx"

libro.save("ejercicio2.xlsx")
print("¡Ejercicio 2 guardado en ejercicio2.xlsx!")
