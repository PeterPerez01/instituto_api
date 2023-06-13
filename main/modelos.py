from sqlalchemy import Column, ForeignKey, Integer, String, Table
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

alumno_materia_table = Table(
    'alumno_materia',
    Base.metadata,
    Column('alumno_id', Integer, ForeignKey('alumnos.id')),
    Column('materia_id', Integer, ForeignKey('materias.id'))
)


class Alumno(Base):
    __tablename__ = 'alumnos'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)
    materias = relationship('Materia', secondary=alumno_materia_table, backref='alumnos')


class Maestro(Base):
    __tablename__ = 'maestros'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    apellido = Column(String)


class Materia(Base):
    __tablename__ = 'materias'

    id = Column(Integer, primary_key=True)
    nombre = Column(String, unique=True)
    maestro_id = Column(Integer, ForeignKey('maestros.id'))
    maestro = relationship(Maestro, backref='materias')
