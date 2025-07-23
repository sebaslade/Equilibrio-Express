from fastapi import FastAPI
from app.core.database import engine, Base  
from app import models
from app.routers import usuarios  # aquí luego irás agregando más routers
from app.routers import auth  # Importa el router de autenticación si lo tienes
from app.routers import productos

# Crear las tablas en la BD si no existen
Base.metadata.create_all(bind=engine)

# Crear instancia de la app
app = FastAPI(
    title="Equilibrio Express API",
    description="API para el backend de la aplicación de comida saludable",
    version="1.0.0"
)

# Incluir los routers (cuando los tengas listos)
app.include_router(usuarios.router)
app.include_router(auth.router)
app.include_router(productos.router)

# Ruta raíz
@app.get("/")
def root():
    return {"message": "API de Equilibrio Express funcionando 🚀"}
