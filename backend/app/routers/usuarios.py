from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models import Usuario
from app.schemas import UsuarioBase, UsuarioCreate, UsuarioResponse
from app.helpers.auth_helper import get_current_user
from passlib.context import CryptContext
from typing import List

router = APIRouter()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@router.get("/usuarios/perfil")
def leer_mi_perfil(usuario_actual: Usuario = Depends(get_current_user)):
    return usuario_actual

@router.get("/usuarios/", response_model=List[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    usuarios = db.query(Usuario).all()
    return usuarios

@router.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario

@router.post("/usuarios/", response_model=UsuarioResponse, status_code=status.HTTP_201_CREATED)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.email == usuario.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Email ya registrado")

    hashed_password = hash_password(usuario.password)
    nuevo_usuario = Usuario(
        nombre=usuario.nombre,
        email=usuario.email,
        direccion=usuario.direccion,
        telefono=usuario.telefono,
        password_hash=hashed_password
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)
    return nuevo_usuario

@router.get("/usuarios/{usuario_id}", response_model=UsuarioResponse)
def obtener_usuario(usuario_id: int, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return usuario