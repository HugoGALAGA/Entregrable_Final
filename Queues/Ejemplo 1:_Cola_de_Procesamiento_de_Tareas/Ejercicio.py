from collections import deque

# Creamos una cola vacía para las tareas
cola_tareas = deque()

print("--- Ejemplo 1: Cola de Procesamiento de Tareas ---")

# 1. Agregar tareas a la cola (Enqueue)
print("Agregando tareas...")
cola_tareas.append("Tarea A") # Enqueue
cola_tareas.append("Tarea B") # Enqueue
cola_tareas.append("Tarea C") # Enqueue
print(f"Estado actual de la cola: {list(cola_tareas)}")
print(f"¿La cola está vacía? {len(cola_tareas) == 0}") # isEmpty

# 2. Procesar tareas desde el frente de la cola (Dequeue)
print("\nProcesando tareas...")
while cola_tareas: # Mientras la cola no esté vacía (isEmpty)
    tarea_actual = cola_tareas.popleft() # Dequeue: saca el elemento del frente
    print(f"Procesando: {tarea_actual}")
    print(f"Tareas restantes: {list(cola_tareas)}")

print("\nTodas las tareas procesadas.")
print(f"¿La cola está vacía al final? {len(cola_tareas) == 0}") # isEmpty
