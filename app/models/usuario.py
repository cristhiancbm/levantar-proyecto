from app.core.database import Base
from app.models.enums import RolEnum
from sqlalchemy import Column, Enum, Integer, String
from sqlalchemy.orm import relationship


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
    contrasena = Column(String(255), nullable=False)

    # Relaciones
    inscripciones = relationship("Inscripcion", back_populates="estudiante")
    trabajos_creados = relationship("Trabajo", back_populates="docente")
    calificaciones = relationship("Calificacion", back_populates="estudiante")

