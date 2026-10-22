from app.core.database import Base
from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Inscripcion(Base):
    __tablename__ = "inscripciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    estudiante_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    materia_id = Column(Integer, ForeignKey("materias.id"), nullable=False)

    # Relaciones
    estudiante = relationship("Usuario", back_populates="inscripciones")
    materia = relationship("Materia", back_populates="estudiantes_inscritos")
