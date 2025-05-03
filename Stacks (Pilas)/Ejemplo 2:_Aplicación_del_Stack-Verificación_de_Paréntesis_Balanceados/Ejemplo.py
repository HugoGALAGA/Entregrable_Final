# Ejemplo 2: Aplicación del Stack - Verificación de Paréntesis Balanceados

print("\n--- Ejemplo 2: Verificación de Paréntesis ---")

def are_parentheses_balanced(expression):
    """
    Verifica si los paréntesis, corchetes y llaves en una cadena
    están correctamente balanceados y anidados usando un Stack.
    """
    stack = [] # Usamos una lista como nuestro Stack
    # Mapeo de delimitadores de cierre a apertura
    mapping = {')': '(', ']': '[', '}': '{'}
    # Conjunto de delimitadores de apertura
    opening_brackets = set(mapping.values())
    # Conjunto de delimitadores de cierre
    closing_brackets = set(mapping.keys())

    print(f"\nAnalizando expresión: {expression}")

    # Recorrer cada carácter en la expresión
    for char in expression:
        print(f"Procesando caracter: '{char}'")
        # Si es un delimitador de apertura, hacemos push al Stack
        if char in opening_brackets:
            print(f"'{char}' es de apertura, haciendo push al Stack.")
            stack.append(char) # Push
            print(f"Stack actual: {stack}")

        # Si es un delimitador de cierre
        elif char in closing_brackets:
            print(f"'{char}' es de cierre.")
            # Si el Stack está vacío, significa que hay un delimitador de cierre sin apertura
            if not stack:
                print(f"Error: Stack vacío. Cierre '{char}' sin apertura.")
                return False
            # Sacamos el último delimitador de apertura del Stack
            last_open = stack.pop() # Pop
            print(f"Pop del Stack: '{last_open}'. Esperado para '{char}' era '{mapping[char]}'")

            # Verificamos si el delimitador de apertura sacado
            # coincide con el delimitador de apertura esperado para el cierre actual
            if last_open != mapping[char]:
                print(f"Error: Desbalance. Encontrado '{last_open}', esperado '{mapping[char]}'.")
                return False
            print("Coincidencia encontrada.")
            print(f"Stack actual: {stack}")

    # Al final, si el Stack está vacío, significa que todos los delimitadores de apertura
    # tuvieron su correspondiente cierre.
    print("\nFin del análisis.")
    if not stack:
        print("Stack final está vacío. Expresión balanceada.")
        return True
    else:
        print(f"Stack final no está vacío: {stack}. Expresión no balanceada.")
        return False

# --- Pruebas ---
print("--- Pruebas de balance de paréntesis ---")
print(f"Resultado: {are_parentheses_balanced('()[]{}')}") # Debería ser True
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('([{}])')}") # Debería ser True
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('([)]')}") # Debería ser False (mal anidado)
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('(((')}") # Debería ser False (paréntesis abiertos sin cerrar)
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced(')))')}") # Debería ser False (paréntesis cerrados sin abrir)
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('')}") # Debería ser True (cadena vacía)
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('{ [ ( ] ) }')}") # Debería ser False (mal anidado, con espacios)
print("-" * 20)
print(f"Resultado: {are_parentheses_balanced('int main() { return 0; }')}") # Debería ser True (ignora otros caracteres)


print("\n--- Fin Ejemplo 2 ---")
