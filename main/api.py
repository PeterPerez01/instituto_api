from fastapi import FastAPI, HTTPException, status
from fastapi import status
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm.exc import NoResultFound
from modelos import Alumno, Maestro, Materia, Base
from sqlalchemy.orm import Session
from sqlalchemy.orm.exc import NoResultFound
from typing import List

app = FastAPI()

# Configuración de la base de datos
engine = create_engine('sqlite:///instituto.db')
Session = sessionmaker(bind=engine)
Base.metadata.create_all(bind=engine)


class AlumnoCreate(BaseModel):
    nombre: str
    apellido: str


class MaestroCreate(BaseModel):
    nombre: str
    apellido: str


class MateriaCreate(BaseModel):
    nombre: str
    maestro_id: int


@app.post('/alumnos', status_code=status.HTTP_201_CREATED)
def create_alumno(alumno_data: AlumnoCreate):
    session = Session()
    try:
        alumno = Alumno(nombre=alumno_data.nombre, apellido=alumno_data.apellido)
        session.add(alumno)
        session.commit()
        return {'message': 'Alumno creado exitosamente'}
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al crear el alumno')
    finally:
        session.close()


@app.get('/alumnos/{alumno_id}')
def get_alumno(alumno_id: int):
    session = Session()
    try:
        alumno = session.query(Alumno).filter_by(id=alumno_id).one()
        return alumno
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alumno no encontrado')
    finally:
        session.close()


@app.put('/alumnos/{alumno_id}')
def update_alumno(alumno_id: int, alumno_data: AlumnoCreate):
    session = Session()
    try:
        alumno = session.query(Alumno).filter_by(id=alumno_id).one()
        alumno.nombre = alumno_data.nombre
        alumno.apellido = alumno_data.apellido
        session.commit()
        return {'message': 'Alumno actualizado exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alumno no encontrado')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al actualizar el alumno')
    finally:
        session.close()


@app.delete('/alumnos/{alumno_id}')
def delete_alumno(alumno_id: int):
    session = Session()
    try:
        alumno = session.query(Alumno).filter_by(id=alumno_id).one()
        session.delete(alumno)
        session.commit()
        return {'message': 'Alumno eliminado exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alumno no encontrado')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al eliminar el alumno')
    finally:
        session.close()


@app.get('/alumnos')
def get_alumnos():
    session = Session()
    try:
        alumnos = session.query(Alumno).all()
        return alumnos
    finally:
        session.close()


@app.post('/maestros', status_code=status.HTTP_201_CREATED)
def create_maestro(maestro_data: MaestroCreate):
    session = Session()
    try:
        maestro = Maestro(nombre=maestro_data.nombre, apellido=maestro_data.apellido)
        session.add(maestro)
        session.commit()
        return {'message': 'Maestro creado exitosamente'}
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al crear el maestro')
    finally:
        session.close()


@app.get('/maestros/{maestro_id}')
def get_maestro(maestro_id: int):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=maestro_id).one()
        return maestro
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Maestro no encontrado')
    finally:
        session.close()


@app.put('/maestros/{maestro_id}')
def update_maestro(maestro_id: int, maestro_data: MaestroCreate):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=maestro_id).one()
        maestro.nombre = maestro_data.nombre
        maestro.apellido = maestro_data.apellido
        session.commit()
        return {'message': 'Maestro actualizado exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Maestro no encontrado')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al actualizar el maestro')
    finally:
        session.close()


@app.delete('/maestros/{maestro_id}')
def delete_maestro(maestro_id: int):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=maestro_id).one()
        session.delete(maestro)
        session.commit()
        return {'message': 'Maestro eliminado exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Maestro no encontrado')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al eliminar el maestro')
    finally:
        session.close()


@app.get('/maestros')
def get_maestros():
    session = Session()
    try:
        maestros = session.query(Maestro).all()
        return maestros
    finally:
        session.close()


@app.post('/materias', status_code=status.HTTP_201_CREATED)
def create_materia(materia_data: MateriaCreate):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=materia_data.maestro_id).one()
        materia = Materia(nombre=materia_data.nombre, maestro_id=maestro.id)
        session.add(materia)
        session.commit()
        return {'message': 'Materia creada exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Maestro no encontrado')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al crear la materia')
    finally:
        session.close()


@app.get('/materias/{materia_id}')
def get_materia(materia_id: int):
    session = Session()
    try:
        materia = session.query(Materia).filter_by(id=materia_id).one()
        return materia
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Materia no encontrada')
    finally:
        session.close()


@app.put('/materias/{materia_id}')
def update_materia(materia_id: int, materia_data: MateriaCreate):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=materia_data.maestro_id).one()
        materia = session.query(Materia).filter_by(id=materia_id).one()
        materia.nombre = materia_data.nombre
        materia.maestro_id = maestro.id
        session.commit()
        return {'message': 'Materia actualizada exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Materia no encontrada')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al actualizar la materia')
    finally:
        session.close()


@app.delete('/materias/{materia_id}')
def delete_materia(materia_id: int):
    session = Session()
    try:
        materia = session.query(Materia).filter_by(id=materia_id).one()
        session.delete(materia)
        session.commit()
        return {'message': 'Materia eliminada exitosamente'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Materia no encontrada')
    except SQLAlchemyError:
        session.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail='Error al eliminar la materia')
    finally:
        session.close()


@app.get('/materias')
def get_materias():
    session = Session()
    try:
        materias = session.query(Materia).all()
        return materias
    finally:
        session.close()

@app.get('/alumnos/{alumno_id}/materias')
def get_materias_alumno(alumno_id: int):
    session = Session()
    try:
        alumno = session.query(Alumno).filter_by(id=alumno_id).one()
        materias = alumno.materias

        if not materias:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontraron materias para el alumno')

        return {'materias': [materia.nombre for materia in materias]}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Alumno no encontrado')
    finally:
        session.close()


@app.get('/maestros/{maestro_id}/info')
def get_maestro_materias(maestro_id: int):
    session = Session()
    try:
        maestro = session.query(Maestro).filter_by(id=maestro_id).one()
        materias = session.query(Materia).filter_by(maestro_id=maestro_id).all()
        return {'maestro': maestro.nombre+' '+maestro.apellido, 'materias': materias}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Maestro no encontrado')
    finally:
        session.close()

@app.post('/materias/{materia_id}/alumnos/{alumno_id}')
def agregar_alumno_a_materia(materia_id: int, alumno_id: int):
    session = Session()
    try:
        materia = session.query(Materia).filter_by(id=materia_id).one()
        alumno = session.query(Alumno).filter_by(id=alumno_id).one()
        
        # Verificar si el alumno ya está asociado a la materia
        if alumno in materia.alumnos:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='El alumno ya está asociado a la materia')
        
        materia.alumnos.append(alumno)
        session.commit()
        return {'message': 'Alumno agregado exitosamente a la materia'}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Materia o alumno no encontrado')
    finally:
        session.close()

@app.get('/materias/{materia_id}/alumnos')
def get_alumnos_en_materia(materia_id: int):
    session = Session()
    try:
        materia = session.query(Materia).filter_by(id=materia_id).one()
        alumnos = materia.alumnos

        if not alumnos:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No se encontraron alumnos en la materia')

        return {'alumnos': [alumno.nombre + " " + alumno.apellido for alumno in alumnos]}
    except NoResultFound:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Materia no encontrada')
    finally:
        session.close()

