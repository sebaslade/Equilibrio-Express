from pydantic import BaseModel, EmailStr
from typing import Optional

class UsuarioBase(BaseModel):
    nombre: str
    email: EmailStr
    direccion: Optional[str] = None
    telefono: Optional[str] = None

class UsuarioCreate(UsuarioBase):
    password: str

class UsuarioResponse(UsuarioBase):
    id: int
    class Config:
        orm_mode = True