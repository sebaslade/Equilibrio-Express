from sqlalchemy import Column, Integer, String, Text, Numeric, Boolean
from app.core.database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)
    precio = Column(Numeric(10,2), nullable=False)
    stock = Column(Integer, nullable=False, default=0)
    imagen_url = Column(Text, nullable=True)
