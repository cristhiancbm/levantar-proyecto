from app.core.database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship


class Trabajo(Base):
    __tablename__ = "trabajos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(150), nullable=False)
    descripcion = Column(Text, nullable=True)
    puntaje_maximo = Column(Float, nullable=False)

    docente_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)

    # Relaciones
    docente = relationship("Usuario", back_populates="trabajos_creados")
    materia = relationship("Materia", back_populates="trabajos")
    calificaciones = relationship("Calificacion", back_populates="trabajo")
