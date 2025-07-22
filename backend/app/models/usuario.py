from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    telefono = Column(String, nullable=True)
    direccion = Column(Text, nullable=True)
    password_hash = Column(Text, nullable=False)
