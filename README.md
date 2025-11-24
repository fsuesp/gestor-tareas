🗂️ Gestor de Tareas (Python)

Un pequeño proyecto en Python que permite crear, listar y gestionar tareas desde consola, utilizando persistencia en un archivo JSON.

🚀 Funcionalidades

Crear tareas nuevas

Listar todas las tareas

Guardar las tareas en un archivo tareas.json

Cargar automáticamente las tareas existentes al iniciar

Interfaz simple por consola

📂 Estructura del proyecto

gestor-tareas/
│
├── gestor.py        # Lógica principal del gestor
├── main.py          # Menú e interacción con el usuario
├── tareas.json      # Archivo donde se guardan las tareas
└── README.md

▶️ Ejecución

Desde la carpeta del proyecto:

python main.py

🧠 Cómo funciona

El sistema:

Crea un archivo tareas.json si no existe

Carga las tareas cuando inicia

Permite agregar nuevas tareas (que se guardan automáticamente)

Muestra un menú simple para manejar todo desde consola

🛠️ Tecnologías usadas

Python 3.x

JSON para guardar la información
