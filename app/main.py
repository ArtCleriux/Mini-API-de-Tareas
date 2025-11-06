from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from . import models, schemas
from .database import SessionLocal, engine

# Crea las tablas en la base de datos (si no existen)
models.Base.metadata.create_all(bind=engine)

# Inicia la aplicación FastAPI
app = FastAPI()

# Configura CORS (Cross-Origin Resource Sharing)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todos los orígenes (para este demo)
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos los métodos (GET, POST, etc.)
    allow_headers=["*"],
)


# Dependencia: Cómo obtener una sesión de BD
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# --- ENDPOINTS DE LA API ---


# Endpoint para CREAR una Tarea (POST)
@app.post("/api/tareas/", response_model=schemas.Tarea)
def create_tarea(tarea: schemas.TareaCreate, db: Session = Depends(get_db)):
    # Creamos un objeto Tarea del modelo SQLAlchemy
    db_tarea = models.Tarea(titulo=tarea.titulo, completada=False)
    # Añadimos a la sesión y guardamos en la BD
    db.add(db_tarea)
    db.commit()
    db.refresh(db_tarea)  # Refresca el objeto con el ID creado
    return db_tarea


# Endpoint para LEER todas las Tareas (GET)
@app.get("/api/tareas/", response_model=list[schemas.Tarea])
def read_tareas(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    # Ejecutamos la consulta SQL (a través del ORM)
    tareas = db.query(models.Tarea).offset(skip).limit(limit).all()
    return tareas


# Endpoint para ACTUALIZAR una Tarea (PUT)
@app.put("/api/tareas/{tarea_id}", response_model=schemas.Tarea)
def update_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = db.query(models.Tarea).filter(
        models.Tarea.id == tarea_id).first()
    if db_tarea is None:
        # Aquí usamos HTTPException, que importaste antes
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    # Invierte el estado de "completada"
    db_tarea.completada = not db_tarea.completada
    db.commit()
    db.refresh(db_tarea)
    return db_tarea


# Endpoint para BORRAR una Tarea (DELETE)
@app.delete("/api/tareas/{tarea_id}", response_model=schemas.Tarea)
def delete_tarea(tarea_id: int, db: Session = Depends(get_db)):
    db_tarea = db.query(models.Tarea).filter(
        models.Tarea.id == tarea_id).first()
    if db_tarea is None:
        raise HTTPException(status_code=404, detail="Tarea no encontrada")

    db.delete(db_tarea)
    db.commit()
    return db_tarea
# --- FIN DE LOS ENDPOINTS ---
