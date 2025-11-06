from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definimos la URL de nuestra BD. Será un archivo .db en la misma carpeta.
SQLALCHEMY_DATABASE_URL = "sqlite:///./tareas.db"

# Creamos el "motor" de SQLAlchemy
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Creamos una "Sesión" que usaremos para comunicarnos con la BD
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Una clase base para nuestros modelos (tablas)
Base = declarative_base()
