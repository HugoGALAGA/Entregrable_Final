# (Asumir que las clases Node y LinkedList están definidas arriba)

print("--- Ejemplo 1: Gestión Simple de Tareas Pendientes ---")
task_list = LinkedList()

# 1. Verificar si está vacía al inicio
print(f"¿La lista de tareas está vacía? {task_list.is_empty()}") # is_empty

# 2. Agregar tareas (append)
print("\nAgregando tareas...")
task_list.append("Comprar leche")
task_list.append("Pagar facturas")
task_list.append("Llamar a Juan")
print("Tareas actuales:")
task_list.display() # display

# 3. Marcar una tarea como completada (eliminar)
print("\nMarcando 'Pagar facturas' como completada...")
success = task_list.delete_node("Pagar facturas") # delete_node
if success:
    print("Tarea eliminada.")
else:
    print("La tarea no se encontró.")
print("Tareas restantes:")
task_list.display() # display

# 4. Intentar eliminar una tarea que no existe
print("\nIntentando marcar 'Ir al gimnasio' como completada...")
success = task_list.delete_node("Ir al gimnasio") # delete_node
if success:
     print("Tarea eliminada.")
else:
     print("La tarea no se encontró.")
print("Tareas restantes:")
task_list.display() # display

# 5. Eliminar las tareas restantes para dejar la lista vacía
print("\nCompletando las tareas restantes...")
task_list.delete_node("Comprar leche")
task_list.delete_node("Llamar a Juan")
print("Tareas restantes:")
task_list.display() # display

# 6. Verificar si está vacía al final
print(f"\n¿La lista de tareas está vacía al final? {task_list.is_empty()}") # is_empty
