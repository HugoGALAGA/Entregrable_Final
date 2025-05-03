# Ejemplo 1: Operaciones Básicas de Arrays (Python List)

print("--- Ejemplo 1: Operaciones Básicas ---")

# 1. Creación de un Array (Lista en Python)
# Puedes crear listas vacías o inicializadas con elementos.
array_vacio = []
array_numeros = [10, 20, 30, 40, 50, 60]
array_mixto = [1, "hola", 3.14, True] # Las listas pueden contener tipos mixtos

print(f"Array de números inicial: {array_numeros}")
print(f"Array mixto inicial: {array_mixto}")

# 2. Acceso a Elementos (Indexación)
# Los arrays permiten acceder a elementos individuales usando su índice (posición).
# Los índices comienzan en 0.
print(f"\n--- Acceso a Elementos ---")
primer_elemento = array_numeros[0] # El elemento en el índice 0
tercer_elemento = array_numeros[2] # El elemento en el índice 2 (el tercero)
print(f"El primer elemento es: {primer_elemento}") # Salida: 10
print(f"El tercer elemento es: {tercer_elemento}") # Salida: 30

# Acceso con índices negativos:
# Los índices negativos cuentan desde el final. -1 es el último, -2 el penúltimo, etc.
ultimo_elemento = array_numeros[-1]
penultimo_elemento = array_numeros[-2]
print(f"El último elemento es: {ultimo_elemento}") # Salida: 60
print(f"El penúltimo elemento es: {penultimo_elemento}") # Salida: 50

# Intentar acceder a un índice fuera de rango causa un error (IndexError)
try:
    elemento_fuera_rango = array_numeros[10]
except IndexError as e:
    print(f"Error al acceder fuera de rango: {e}")

# 3. Modificación de Elementos
# Puedes cambiar el valor de un elemento accediendo a su índice.
print(f"\n--- Modificación de Elementos ---")
print(f"Array antes de modificar: {array_numeros}")
array_numeros[1] = 25 # Cambia el elemento en el índice 1 (el 20) a 25
array_numeros[-1] = 65 # Cambia el último elemento (el 60) a 65
print(f"Array después de modificar: {array_numeros}") # Salida: [10, 25, 30, 40, 50, 65]

# 4. Tamaño del Array
# La función len() devuelve el número de elementos.
print(f"\n--- Tamaño del Array ---")
tamaño = len(array_numeros)
print(f"El tamaño del array es: {tamaño}") # Salida: 6

# 5. Recorrido (Iteración)
# Puedes iterar sobre los elementos usando un bucle for.
print(f"\n--- Recorrido del Array ---")
print("Recorriendo por elementos:")
for elemento in array_numeros:
    print(elemento, end=" ") # Salida: 10 25 30 40 50 65
print("\nRecorriendo por índice:")
for i in range(len(array_numeros)):
    print(f"Elemento en índice {i}: {array_numeros[i]}")

# 6. Búsqueda (Lineal)
# Verificar si un elemento existe o encontrar su índice.
print(f"\n--- Búsqueda de Elementos ---")
buscar_valor = 40
if buscar_valor in array_numeros:
    print(f"{buscar_valor} está en el array.")
    # Encontrar el índice de la primera ocurrencia
    indice_encontrado = array_numeros.index(buscar_valor)
    print(f"El índice de {buscar_valor} es: {indice_encontrado}") # Salida: 3
else:
    print(f"{buscar_valor} no está en el array.")

buscar_valor_no_existente = 99
if buscar_valor_no_existente not in array_numeros:
     print(f"{buscar_valor_no_existente} no está en el array (verificado con 'not in').")

# Intentar encontrar el índice de un elemento que no existe causa un ValueError
try:
    indice_no_existente = array_numeros.index(99)
except ValueError as e:
    print(f"Error al buscar índice de elemento no existente: {e}")


# 7. Slicing (Rebanado)
# Obtener sub-arrays (partes del array original)
print(f"\n--- Slicing (Sub-arrays) ---")
sub_array = array_numeros[1:4] # Desde el índice 1 (incluido) hasta el 4 (excluido)
print(f"Sub-array [1:4]: {sub_array}") # Salida: [25, 30, 40]

sub_array_inicio = array_numeros[:3] # Desde el inicio hasta el índice 3 (excluido)
print(f"Sub-array [:3]: {sub_array_inicio}") # Salida: [10, 25, 30]

sub_array_fin = array_numeros[4:] # Desde el índice 4 (incluido) hasta el final
print(f"Sub-array [4:]: {sub_array_fin}") # Salida: [50, 65]

copia_completa = array_numeros[:] # Una copia de todo el array
print(f"Copia completa [:]: {copia_completa}")

sub_array_paso = array_numeros[::2] # Desde el inicio hasta el fin, saltando de 2 en 2
print(f"Sub-array [::2]: {sub_array_paso}") # Salida: [10, 30, 50]

sub_array_inverso = array_numeros[::-1] # Una forma sencilla de invertir el array
print(f"Sub-array inverso [::-1]: {sub_array_inverso}") # Salida: [65, 50, 40, 30, 25, 10]

# 8. Operaciones Estadísticas Básicas (Built-in)
print(f"\n--- Estadísticas Básicas ---")
print(f"Mínimo: {min(array_numeros)}") # Salida: 10
print(f"Máximo: {max(array_numeros)}") # Salida: 65
print(f"Suma: {sum(array_numeros)}") # Salida: 230


print("\n--- Fin Ejemplo 1 ---")
