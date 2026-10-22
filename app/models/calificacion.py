from app.core.database import Base
from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Calificacion(Base):
    __tablename__ = "calificaciones"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nota_obtenida = Column(Float, nullable=False)

    estudiante_id = Column(Integer, ForeignKey("usuarios.id"), nullable=False)
    trabajo_id = Column(Integer, ForeignKey("trabajos.id"), nullable=False)

    # Relaciones
    estudiante = relationship("Usuario", back_populates="calificaciones")
    trabajo = relationship("Trabajo", back_populates="calificaciones")
