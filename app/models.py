from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Tarea(Base):
    __tablename__ = "tareas"

    # Definimos las columnas
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String, index=True)
    completada = Column(Boolean, default=False)
