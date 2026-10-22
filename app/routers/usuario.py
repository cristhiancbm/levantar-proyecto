from app.core.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioCreate, UsuarioResponse, UsuarioUpdate
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])


@router.post("/", response_model=UsuarioResponse, status_code=201)

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
@router.get("/", response_model=list[UsuarioResponse])
def listar_usuarios(db: Session = Depends(get_db)):
    # Retorna todos los usuarios registrados
    return db.query(Usuario).all()

@router.put("/{usuario_id}", response_model=UsuarioResponse)
def actualizar_usuario_completo(
    usuario_id: int,
    usuario: UsuarioCreate,  # Exige absolutamente todos los campos
    db: Session = Depends(get_db),
):
    # Buscamos al usuario
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    # Actualizamos todos los campos de golpe
    db_usuario.nombres = usuario.nombres
    db_usuario.apellidos = usuario.apellidos
    db_usuario.profesion = usuario.profesion
    db_usuario.carnet = usuario.carnet
    db_usuario.matricula = usuario.matricula
    db_usuario.celular = usuario.celular
    db_usuario.correo = usuario.correo
    db_usuario.rol = usuario.rol
    db_usuario.contrasena = usuario.contrasena

    # Guardamos los cambios
    db.commit()
    db.refresh(db_usuario)

    return db_usuario

@router.patch("/{usuario_id}")
def actualizar_parcial_usuario(
    usuario_id: int,
    usuario: UsuarioUpdate,
    db: Session = Depends(get_db),
):
    # Filtramos solo los datos que el usuario envió realmente
    datos_update = usuario.model_dump(exclude_unset=True)

    if not datos_update:
        raise HTTPException(
            status_code=400, detail="No se enviaron datos para actualizar."
        )

    # Actualizamos directamente en la base de datos en una sola línea
    db.query(Usuario).filter(Usuario.id == usuario_id).update(datos_update)
    db.commit()

    return {"mensaje": "Usuario actualizado exitosamente"}

@router.delete("/{usuario_id}")
def eliminar_usuario(usuario_id: int, db: Session = Depends(get_db)):
    # Buscar si el usuario existe en la base de datos
    db_usuario = db.query(Usuario).filter(Usuario.id == usuario_id).first()
    if not db_usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado.")

    # Eliminar el registro y confirmar los cambios
    db.delete(db_usuario)
    db.commit()

    # Retornar un mensaje de confirmación
    return {"mensaje": "Usuario eliminado exitosamente"}

