---

## 🤝 Pull Requests (Solicitudes de Extracción)

Un Pull Request (PR), también conocido como Merge Request (MR) en plataformas como GitLab, es el mecanismo estándar para **proponer cambios** en un repositorio y **solicitar que sean revisados y fusionados** en otra rama (generalmente una rama principal como `main` o `develop`).

---

### 🤔 ¿Qué es un Pull Request y Cuál es su Propósito?

**¿Qué es?**

Un Pull Request es esencialmente una **conversación sobre un conjunto específico de cambios** (los commits de una rama) que se proponen incorporar a otra rama de destino. No es solo una "petición para jalar mi código", sino una **solicitud formal para discutir, revisar y finalmente fusionar** el código.

Vive en las **plataformas de alojamiento de repositorios remotos** (como GitHub, GitLab, Bitbucket, etc.), no directamente en tu repositorio local de Git.

**¿Cuál es su Propósito?**

*   **Revisión de Código (Code Review):** Permite que otros miembros del equipo revisen los cambios propuestos, identifiquen posibles errores, sugieran mejoras o alternativas antes de que el código se integre. Esta es su función principal y más valiosa.
*   **Discusión y Colaboración:** Proporciona un espacio centralizado para que el equipo discuta los cambios, el diseño, las implicaciones de la implementación, etc., antes de que el código se integre.
*   **Control de Calidad:** Permite integrar pruebas automatizadas (CI/CD) que se ejecutan automáticamente sobre los cambios propuestos en el PR, asegurando que no rompen funcionalidades existentes.
*   **Documentación del Cambio:** El propio PR, con su descripción, commits, comentarios y historial de revisiones, se convierte en parte de la documentación sobre *por qué* y *cómo* se hicieron ciertos cambios.
*   **Gestión del Flujo de Trabajo:** Formaliza el proceso de integrar nuevo código, haciendo que sea predecible y rastreable.

Piensa en un PR como un **borrador de un documento importante** que envías a tus colegas para que lo revisen, hagan comentarios y lo aprueben antes de incorporarlo al documento final.

### ⚙️ ¿Cómo Funcionan los Pull Requests (El Flujo Típico)?

El flujo de trabajo con Pull Requests sigue generalmente estos pasos:

1.  **Crear una Rama de Feature/Tema:** Comienzas trabajando en una rama nueva y separada de la rama principal (ej: `main` o `develop`) para tu tarea (una nueva característica, una corrección de bug, una mejora).
    *   `git switch -c mi-nueva-feature` (o `git checkout -b mi-nueva-feature`)
2.  **Desarrollar y Commitear:** Haces tus cambios en el código y los registras con commits en tu rama de feature.
    *   `git add .`
    *   `git commit -m "Implementar parte de la feature X"`
3.  **Subir la Rama al Remoto:** Una vez que tus commits están listos para ser revisados, subes tu rama de feature a la plataforma de alojamiento del repositorio remoto.
    *   `git push origin mi-nueva-feature`
4.  **Abrir el Pull Request:** Vas a la interfaz web de la plataforma (GitHub, GitLab, etc.). La plataforma a menudo detecta que has subido una nueva rama y te sugiere abrir un PR. Creas un nuevo PR especificando:
    *   La **rama base/destino** (a la que quieres fusionar, ej: `main`).
    *   Tu **rama comparadora/origen** (la que contiene tus cambios, ej: `mi-nueva-feature`).
    *   Un **título y descripción claros** del PR (explicando *qué* hace y *por qué*).
5.  **Revisión y Discusión:** Otros desarrolladores (revisores) ven el PR. Pueden:
    *   Ver todos los **commits** incluidos.
    *   Ver el **diff** (la comparación línea a línea de los archivos cambiados).
    *   Dejar **comentarios** generales o comentarios específicos en líneas de código.
    *   Solicitar **cambios**.
6.  **Iteración (si es necesario):** Si hay comentarios o se solicitan cambios, regresas a tu rama de feature **local**, haces los ajustes necesarios, creas nuevos commits y los `push`eas a la **misma rama remota**. ¡El PR se actualiza automáticamente con los nuevos commits!
    *   `git add .`
    *   `git commit -m "Atender comentarios de revisión Y"`
    *   `git push origin mi-nueva-feature`
7.  **Checks Automatizados:** La plataforma o un sistema de CI/CD configurado (como GitHub Actions, GitLab CI, Jenkins) ejecuta pruebas automatizadas (unitarias, de integración, linting, etc.) sobre los cambios del PR. El estado de estos checks (pasó/falló) se muestra en el PR.
8.  **Aprobación:** Una vez que los revisores están satisfechos, aprueban el PR.
9.  **Fusión (Merge):** Cuando el PR ha sido aprobado y todos los checks automáticos han pasado, el PR se puede **fusionar**. Un desarrollador con permisos (a menudo el autor o un mantenedor) fusiona la rama de feature en la rama base (ej: `main`). Las plataformas ofrecen diferentes métodos de fusión:
    *   **Merge Commit (por defecto):** Crea un nuevo commit de fusión que une el historial de ambas ramas.
    *   **Squash and Merge:** Combina *todos* los commits de la rama de feature en *un único* nuevo commit en la rama base. Mantiene un historial más limpio en la rama principal.
    *   **Rebase and Merge:** Re-aplica los commits de la rama de feature uno por uno sobre la punta de la rama base, creando un historial lineal (similar a hacer `git rebase` localmente antes de fusionar). También mantiene un historial lineal.
10. **Cerrar el PR y Eliminar la Rama:** Una vez fusionado, el PR se cierra automáticamente (o manualmente). La rama de feature ya no es necesaria y suele eliminarse para mantener el repositorio limpio.

### 📊 Componentes Clave de una Interfaz de Pull Request

Al ver un PR en una plataforma, típicamente encontrarás las siguientes secciones:

*   **Conversación/Discussion:** El corazón del PR. Contiene la descripción inicial, los comentarios, las respuestas, menciones de otros PRs/Issues, etc.
*   **Commits:** Lista de todos los commits que están incluidos en la rama de origen del PR desde que se ramificó de la base.
*   **Files Changed:** La vista más importante para la revisión. Muestra un "diff" (diferencia) visual entre el contenido de los archivos en la rama de origen y la rama de destino. Aquí es donde los revisores suelen añadir comentarios línea por línea.
*   **Checks/Status:** Muestra el resultado de las pruebas automatizadas y otras validaciones (ej: ¿el código cumple con el estilo? ¿pasan las pruebas unitarias?).
*   **Reviews/Approvals:** Resumen de quién ha revisado el PR y si lo han aprobado, solicitado cambios, o comentado.

### ✅ Ventajas del Flujo de Trabajo con Pull Requests

*   **Mejora la Calidad del Código:** Múltiples ojos revisando el código capturan más errores y fallos de diseño.
*   **Comparte Conocimiento:** Los revisores aprenden sobre el nuevo código, y el autor aprende de los comentarios y sugerencias. Fomenta la propiedad compartida del código.
*   **Reduce Riesgos:** Evita fusionar código defectuoso o inestable a las ramas principales.
*   **Historial Enriquecido:** La discusión y la justificación de los cambios quedan registradas junto al código.
*   **Integración con CI/CD:** Permite ejecutar pruebas automáticamente antes de fusionar.
*   **Permisos Granulares:** Puedes configurar quién tiene permiso para fusionar PRs en ramas protegidas (como `main`).

### 🧩 Conceptos Relacionados

*   **Ramas (Branches):** Los PRs operan entre dos ramas.
*   **Commits:** Los cambios se agrupan en commits dentro de la rama del PR.
*   **Repositorios Remotos:** Donde residen los PRs (en plataformas como GitHub, GitLab).
*   **Code Review:** La actividad principal que ocurre dentro de un PR.
*   **CI/CD:** Sistemas automatizados que se integran con PRs para validar código.
*   **Issues:** A menudo, un PR se abre para abordar un Issue específico. Las plataformas permiten vincular PRs a Issues.
*   **Conflictos de Fusión:** Pueden ocurrir si la rama base cambia después de que ramificaste tu feature y modificas los mismos archivos. Deben resolverse antes de poder fusionar el PR.

### 💡 ¿Cuándo Usar Pull Requests?

Siempre que estés trabajando en un equipo, o incluso solo en un proyecto personal importante, usar Pull Requests es una **práctica recomendada**. Formaliza la integración de cambios, mejora la calidad y proporciona un historial valioso. Son especialmente cruciales cuando la rama base (ej. `main`) debe mantenerse siempre estable y desplegable.

---

**Conclusión:**

Los Pull Requests son mucho más que una simple solicitud para traer código; son la **pieza central del flujo de trabajo colaborativo** en Git. Proporcionan una plataforma estructurada para la revisión de código, la discusión, la ejecución de pruebas automatizadas y la gestión controlada de la integración de cambios de una rama a otra. Dominar el proceso de Pull Request, tanto abriéndolos como revisándolos, es una habilidad indispensable para cualquier desarrollador que trabaje en un equipo y quiera contribuir de manera efectiva y segura.
