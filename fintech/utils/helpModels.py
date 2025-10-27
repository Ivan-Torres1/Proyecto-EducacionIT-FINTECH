from sqlmodel import Session, select
from fintech.utils.database import engine
from fintech.modelos.Usuario import UsuarioModel


class UsuarioNoEncontradoError(Exception):
    pass

def encontrarUserConDNI(dni: int,session: Session) -> UsuarioModel:
    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.dni == dni)
        user = session.exec(consulta).first()
        if user:
            return user
        else:
            raise UsuarioNoEncontradoError(f"No se encontró usuario con DNI: {dni}")
        