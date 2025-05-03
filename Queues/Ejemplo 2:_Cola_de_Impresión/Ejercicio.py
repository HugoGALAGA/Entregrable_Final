from collections import deque

# Creamos una cola para los documentos a imprimir
cola_impresion = deque()

print("\n--- Ejemplo 2: Cola de Impresión ---")

# 1. Agregar documentos a la cola (Enqueue)
print("Enviando documentos a la impresora...")
cola_impresion.append("Reporte.docx") # Enqueue
cola_impresion.append("Imagen.png")   # Enqueue
cola_impresion.append("Presentacion.pptx") # Enqueue
print(f"Documentos en cola: {list(cola_impresion)}")

# 2. Verificar cuántos documentos están esperando (Size)
print(f"Cantidad de documentos esperando: {len(cola_impresion)}") # Size

# 3. Ver el próximo documento a imprimir sin sacarlo (Peek)
if cola_impresion:
    proximo_documento = cola_impresion[0] # Peek: accede al primer elemento sin remover
    print(f"Próximo documento a imprimir: {proximo_documento}")

# 4. Imprimir documentos desde el frente de la cola (Dequeue)
print("\nImprimiendo documentos...")
while cola_impresion:
    documento_actual = cola_impresion.popleft() # Dequeue: saca el documento del frente
    print(f"Imprimiendo: {documento_actual}")
    print(f"Documentos restantes: {list(cola_impresion)}")

print("\nCola de impresión vacía.")
print(f"Cantidad de documentos al final: {len(cola_impresion)}") # Size
