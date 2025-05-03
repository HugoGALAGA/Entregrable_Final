import array # Necesitas importar este módulo

# Ejemplo 3: Arrays de Tipo Fijo (array.array) y Algoritmos
print("\n--- Ejemplo 3: Arrays de Tipo Fijo y Algoritmos ---")

# 1. Creación de un Array de Tipo Fijo
# array.array requiere especificar el tipo de dato (código de tipo).
# 'i' para enteros (int), 'f' para flotantes (float), etc.
# Esto hace que sean más eficientes en memoria para grandes colecciones de datos homogéneos.
# Son menos flexibles que las listas (no pueden mezclar tipos).
try:
    array_entero = array.array('i', [1, 2, 3, 4, 5])
    print(f"Array de enteros (array.array): {array_entero}")

    # Intentar añadir un tipo incorrecto dará un error TypeError
    # array_entero.append("string") # Descomenta para ver el error
except TypeError as e:
    print(f"Error de tipo al intentar añadir string a array de enteros: {e}")

# 2. Operaciones Básicas (similar a list)
print(f"\n--- Operaciones Básicas en array.array ---")
print(f"Primer elemento: {array_entero[0]}")
print(f"Tamaño: {len(array_entero)}")
array_entero.append(6)
print(f"Después de append(6): {array_entero}")
array_entero.pop()
print(f"Después de pop(): {array_entero}")

# 3. Algoritmo: Invertir un Array
# Se puede hacer de varias formas. Usaremos un enfoque de dos punteros
# para demostrar la manipulación de elementos en su lugar.
def invertir_array_inplace(arr):
    inicio = 0
    fin = len(arr) - 1
    while inicio < fin:
        # Intercambiar los elementos en los punteros de inicio y fin
        arr[inicio], arr[fin] = arr[fin], arr[inicio]
        # Mover los punteros hacia el centro
        inicio += 1
        fin -= 1
    return arr

print(f"\n--- Algoritmo: Invertir Array ---")
array_para_invertir = array.array('i', [10, 20, 30, 40, 50])
print(f"Array original: {array_para_invertir}")
invertir_array_inplace(array_para_invertir) # Modifica el array original
print(f"Array invertido (inplace): {array_para_invertir}") # Salida: array('i', [50, 40, 30, 20, 10])

# Otra forma sencilla en Python usando slicing (crea una nueva lista)
array_para_invertir_2 = array.array('i', [11, 22, 33, 44])
array_invertido_nuevo = array.array(array_para_invertir_2.typecode, array_para_invertir_2[::-1])
print(f"Array original 2: {array_para_invertir_2}")
print(f"Array invertido (nuevo con slicing): {array_invertido_nuevo}") # Salida: array('i', [44, 33, 22, 11])


# 4. Algoritmo: Contar Frecuencia de Elementos
# Usamos un diccionario para llevar la cuenta de cada elemento.
def contar_frecuencia(arr):
    frecuencia = {} # Un diccionario para almacenar counts
    for elemento in arr:
        # Si el elemento ya está en el diccionario, incrementa su cuenta
        # Si no, añádelo con una cuenta de 1
        frecuencia[elemento] = frecuencia.get(elemento, 0) + 1
    return frecuencia

print(f"\n--- Algoritmo: Contar Frecuencia ---")
array_con_duplicados = array.array('i', [1, 2, 2, 3, 1, 4, 2, 5, 3, 1])
print(f"Array con duplicados: {array_con_duplicados}")
frecuencias = contar_frecuencia(array_con_duplicados)
print(f"Frecuencias de elementos: {frecuencias}") # Salida: {1: 3, 2: 3, 3: 2, 4: 1, 5: 1}


print("\n--- Fin Ejemplo 3 ---")
