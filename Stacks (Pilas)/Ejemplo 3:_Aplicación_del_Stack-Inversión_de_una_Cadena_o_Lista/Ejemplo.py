# Ejemplo 3: Aplicación del Stack - Inversión de una Cadena o Lista

print("\n--- Ejemplo 3: Inversión con Stack ---")

def reverse_with_stack(input_sequence):
    """
    Invierte una secuencia (como una cadena o lista) usando un Stack.
    """
    stack = [] # Usamos una lista como nuestro Stack
    reversed_sequence = [] # Lista para construir el resultado invertido

    print(f"\nSecuencia original: {input_sequence}")
    print("Empujando elementos al Stack:")

    # Paso 1: Empujar todos los elementos de la secuencia al Stack
    for item in input_sequence:
        print(f"  Push: '{item}'")
        stack.append(item) # Push

    print(f"\nStack después de empujar: {stack}")
    print("Sacando elementos del Stack (en orden inverso):")

    # Paso 2: Sacar todos los elementos del Stack y añadirlos a la nueva secuencia
    # El Stack sigue el principio LIFO, por lo que los elementos saldrán en el orden inverso
    while stack: # Mientras el Stack no esté vacío
        item = stack.pop() # Pop
        print(f"  Pop: '{item}'")
        reversed_sequence.append(item)

    # Si la secuencia de entrada era una cadena, juntar los caracteres resultantes
    if isinstance(input_sequence, str):
        return "".join(reversed_sequence)
    else: # Si era una lista u otro iterable, devolver la lista resultante
        return reversed_sequence


# --- Pruebas ---
print("--- Pruebas de inversión con Stack ---")

# Invertir una cadena
cadena_original = "Hola Mundo"
cadena_invertida = reverse_with_stack(cadena_original)
print(f"Cadena original: '{cadena_original}'")
print(f"Cadena invertida: '{cadena_invertida}'") # Debería ser 'odnuM aloH'
print("-" * 20)

# Invertir una lista de números
lista_original = [10, 20, 30, 40, 50]
lista_invertida = reverse_with_stack(lista_original)
print(f"Lista original: {lista_original}")
print(f"Lista invertida: {lista_invertida}") # Debería ser [50, 40, 30, 20, 10]
print("-" * 20)

# Invertir una lista de strings
lista_palabras = ["primero", "segundo", "tercero"]
lista_palabras_invertida = reverse_with_stack(lista_palabras)
print(f"Lista original: {lista_palabras}")
print(f"Lista invertida: {lista_palabras_invertida}") # Debería ser ['tercero', 'segundo', 'primero']
print("-" * 20)


print("\n--- Fin Ejemplo 3 ---")
