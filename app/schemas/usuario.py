from app.models.enums import RolEnum
from pydantic import BaseModel, EmailStr


class UsuarioBase(BaseModel):
  nombres: str
  apellidos: str
  profesion: str | None = None
  carnet: int
  matricula: str | None = None
  celular: str
  correo: EmailStr
  rol: RolEnum


# Esquema para CREAR (Aquí SÍ va la contraseña)
class UsuarioCreate(UsuarioBase):
  contrasena: str


# Esquema de RESPUESTA (Aquí NO va la contraseña)
class UsuarioResponse(UsuarioBase):
  id: int

  class Config:
    from_attributes = True

class UsuarioUpdate(BaseModel):
    nombres: str | None = None
    apellidos: str | None = None
    profesion: str | None = None
    carnet: int | None = None
    matricula: str | None = None
    celular: str | None = None
    correo: EmailStr | None = None
    rol: RolEnum | None = None
    contrasena: str | None = None
    