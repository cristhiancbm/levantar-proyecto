from app.core.database import Base
from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship


class Materia(Base):
    __tablename__ = "materias"

    id = Column(Integer, primary_key=True, autoincrement=True)
    sigla = Column(String(20), unique=True, nullable=False)
    nombre = Column(String(100), nullable=False)
    descripcion = Column(Text, nullable=True)

    # Relaciones
    estudiantes_inscritos = relationship("Inscripcion", back_populates="materia")
    trabajos = relationship("Trabajo", back_populates="materia")
