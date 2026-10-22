from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
from app.models.enums import RolEnum


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    apellidos = Column(String(100), nullable=False)
    nombres = Column(String(100), nullable=False)
    profesion = Column(String(100), nullable=True)
    carnet = Column(Integer, nullable=False)
    matricula = Column(String(20), nullable=True)
    celular = Column(String(8), nullable=False)
    correo = Column(String(100), unique=True, index=True, nullable=False)
    rol = Column(Enum(RolEnum), nullable=False)
