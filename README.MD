# Mini-API de Tareas con Python, FastAPI y SQL

Este es un proyecto Full-Stack simple que demuestra cómo construir una API RESTful usando Python (FastAPI) y una base de datos SQL (SQLite con SQLAlchemy) para realizar operaciones CRUD (Crear, Leer, Actualizar, Borrar).

El proyecto incluye un backend de API y un frontend de cliente HTML/CSS/JS simple para consumir la API.

### Demo
[¡Aquí deberías poner tu captura de pantalla o, mejor aún, un GIF corto que muestre cómo añades, completas y borras tareas!]

---

### 🚀 Tecnologías Utilizadas

* **Backend:**
    * [Python 3.10+](https://img.shields.io/badge/Python-3.10-3776AB?logo=python)
    * [FastAPI](https://img.shields.io/badge/FastAPI-0.95-009688?logo=fastapi)
    * [SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-1.4-D71F00?logo=sqlalchemy)
    * [SQLite](https://img.shields.io/badge/SQLite-3.0-003B57?logo=sqlite)
    * [Uvicorn](https://img.shields.io/badge/Uvicorn-0.17-2F9E8C?logo=python)
* **Frontend:**
    * [HTML5](https://img.shields.io/badge/HTML5-E34F26?logo=html5)
    * [CSS3](https://img.shields.io/badge/CSS3-1572B6?logo=css3)
    * [JavaScript (Fetch API)](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript)

---

### ⚙️ Instalación y Ejecución

**Requisitos:**
* Python 3.8+

**1. Clonar el repositorio y configurar el entorno:**

```bash
# Clonar el proyecto (si está en GitHub)
# git clone [https://github.com/tu-usuario/api-tareas-python.git](https://github.com/tu-usuario/api-tareas-python.git)
# cd api-tareas-python

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

**2. Instalar dependencias:**

```bash
pip install fastapi "uvicorn[standard]" sqlalchemy
```

**3. Ejecutar el servidor Backend:**

Ejecuta este comando desde la carpeta raíz del proyecto (la que contiene la carpeta `app`).

```bash
# --reload-dir app vigila solo la carpeta 'app' para evitar bucles de recarga
uvicorn app.main:app --reload --reload-dir app
```
El servidor estará corriendo en `http://127.0.0.1:8000`.

**4. Probar el Frontend:**

Simplemente abre el archivo `frontend/index.html` en tu navegador web.

---

### 🗺️ Estructura de la API

La API expone los siguientes endpoints:

* **`GET /api/tareas/`**: Obtiene una lista de todas las tareas.
* **`POST /api/tareas/`**: Crea una nueva tarea.
    * *Body (JSON):* `{ "titulo": "Mi nueva tarea" }`
* **`PUT /api/tareas/{tarea_id}`**: Actualiza el estado (completada/no completada) de una tarea.
* **`DELETE /api/tareas/{tarea_id}`**: Borra una tarea.