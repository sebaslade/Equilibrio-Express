# app/schemas/__init__.py
from .usuarios import UsuarioBase, UsuarioCreate, UsuarioResponse
from .producto import ProductoBase, ProductoCreate, ProductoResponse

__all__ = [
    "UsuarioBase", "UsuarioCreate", "UsuarioResponse",
    "ProductoBase", "ProductoCreate", "ProductoResponse"
]
