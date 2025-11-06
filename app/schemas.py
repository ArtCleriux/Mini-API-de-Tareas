from pydantic import BaseModel


# Schema para crear una tarea (lo que recibimos del usuario)
class TareaCreate(BaseModel):
    titulo: str


# Schema para leer una tarea (lo que enviamos al usuario)
class Tarea(BaseModel):
    id: int
    titulo: str
    completada: bool

    # Configuración para que Pydantic entienda los modelos de SQLAlchemy
    class Config:
        orm_mode = True
