from collections import deque

# Creamos una cola para las llamadas
cola_llamadas = deque()

print("\n--- Ejemplo 3: Cola de Llamadas en un Call Center ---")

print("Call Center Abierto.")

# 1. Simular llamadas entrantes (Enqueue)
print("Llamadas entrando...")
cola_llamadas.append("Llamada de Cliente A") # Enqueue
cola_llamadas.append("Llamada de Cliente B") # Enqueue
print(f"Estado de la cola: {list(cola_llamadas)}")

# 2. Verificar cuántas llamadas están esperando (Size)
print(f"Número de llamadas en espera: {len(cola_llamadas)}") # Size

# 3. Simular que un agente toma una llamada (Dequeue)
print("\nUn agente está libre...")
if cola_llamadas: # Verificar si la cola no está vacía (isEmpty)
    llamada_siendo_atendida = cola_llamadas.popleft() # Dequeue: saca la llamada más antigua
    print(f"Atendiendo: {llamada_siendo_atendida}")
else:
    print("No hay llamadas en espera. Agente libre.")

# 4. Verificar estado de la cola después de atender una llamada
print(f"Estado actual de la cola: {list(cola_llamadas)}")
print(f"Número de llamadas en espera: {len(cola_llamadas)}") # Size

# 5. Simular otra llamada entrante
print("\nOtra llamada entrando...")
cola_llamadas.append("Llamada de Cliente C") # Enqueue
print(f"Estado de la cola: {list(cola_llamadas)}")
print(f"Número de llamadas en espera: {len(cola_llamadas)}") # Size

# 6. Simular que otro agente toma una llamada
print("\nOtro agente está libre...")
if cola_llamadas: # Verificar si la cola no está vacía (isEmpty)
    llamada_siendo_atendida = cola_llamadas.popleft() # Dequeue
    print(f"Atendiendo: {llamada_siendo_atendida}")
else:
    print("No hay llamadas en espera. Agente libre.")

print(f"Estado final de la cola: {list(cola_llamadas)}")
print(f"¿Hay llamadas esperando al final? {len(cola_llamadas) > 0}") # isEmpty check
