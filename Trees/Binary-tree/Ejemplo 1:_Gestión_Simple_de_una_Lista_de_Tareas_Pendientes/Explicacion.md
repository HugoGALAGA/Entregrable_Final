# Explicación del Ejemplo 1: Gestión Simple de Tareas Pendientes

Este ejemplo simula una lista básica de tareas donde las nuevas tareas se añaden a la lista y las tareas completadas se eliminan. Es un caso de uso simple que demuestra las operaciones fundamentales de una lista enlazada.

**Funcionalidades Demostradas:**

1.  **`append` (Agregar al final):** La operación `task_list.append()` añade nuevos nodos (tareas) al *final* de la lista. Esto es útil cuando el orden de llegada importa o cuando se quiere procesar la lista desde el principio, manteniendo los nuevos elementos al final. La implementación recorre la lista hasta el último nodo y enlaza el nuevo nodo a él.

2.  **`display` (Mostrar):** El método `task_list.display()` recorre la lista enlazada desde la `head` hasta el último nodo (`next` es `None`), recogiendo los datos de cada nodo y mostrándolos en orden. Esto permite visualizar el contenido actual de la lista sin modificarla.

3.  **`delete_node` (Eliminar por valor):** La operación `task_list.delete_node()` busca un nodo específico por su valor (`key`) y lo elimina de la lista. Si el nodo a eliminar es la cabeza, actualiza la `head`. Si está en medio, ajusta el puntero `next` del *nodo anterior* para que apunte al nodo *siguiente* del nodo a eliminar, efectivamente saltándose el nodo a eliminar. Si el nodo no se encuentra, la lista no cambia.

4.  **`is_empty` (Verificar si está vacía):** La función `task_list.is_empty()` simplemente comprueba si la `head` de la lista es `None`. Si es así, significa que no hay nodos en la lista. Se utiliza al principio y al final para verificar el estado de la lista.

**En Resumen:**

Este ejemplo ilustra cómo una lista enlazada puede ser usada para gestionar una colección dinámica de elementos (tareas) donde se necesitan añadir elementos, visualizarlos, y remover elementos específicos por su contenido, destacando la flexibilidad de las operaciones de inserción y eliminación en nodos no contiguos en memoria.
