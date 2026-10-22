from app.core.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioResponse)
def crear_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    # Verificar si el correo ya está registrado en la base de datos
    db_user = db.query(Usuario).filter(Usuario.correo == usuario.correo).first()
    if db_user:
        raise HTTPException(
            status_code=400, detail="El correo electrónico ya está registrado."
        )

    # Crear la instancia del modelo SQLAlchemy directamente con los datos
    nuevo_usuario = Usuario(**usuario.model_dump())

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario
