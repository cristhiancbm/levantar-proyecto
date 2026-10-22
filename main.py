from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import Base, engine, verificar_conexion_db
from app.routers import usuario
import app.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    verificar_conexion_db()

# Crea las tablas
    Base.metadata.create_all(bind=engine)

    yield

# Instancia principal de la aplicación
app = FastAPI(
    title="Mi API REST",
    description="API para la gestión de productos y usuarios",
    version="1.0.0",
    lifespan=lifespan
)

# rutas / endpoints
app.include_router(usuario.router)