# app/core/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# URL de conexión, por ejemplo:
# postgresql://usuario:contraseña@localhost:5432/equilibrio_express
DATABASE_URL = os.getenv("DATABASE_URL")

# Crear el engine
engine = create_engine(DATABASE_URL)

# Crear una sesión local
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()

# Dependencia para obtener una sesión de BD en los routers
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
