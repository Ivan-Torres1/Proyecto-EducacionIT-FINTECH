from sqlmodel import Session, select
from utils.database import engine
from modelos.Usuario import UsuarioModel
from sqlalchemy.orm import selectinload


class UsuarioNoEncontradoError(Exception):
    pass
class CuentaNoEncontradaError(Exception):
    pass

def encontrarUserConDNI(dni: int,session: Session) -> UsuarioModel:
    with Session(engine) as session:
        consulta = select(UsuarioModel).where(UsuarioModel.dni == dni)
        user = session.exec(consulta).first()
        if user is None:
            return user
        else:
            raise UsuarioNoEncontradoError(f"No se encontró usuario con DNI: {dni}")
        

def encontrarCuentasUsuario(dniUser:int,session: Session) -> UsuarioModel:
    
    with Session(engine) as session:
        consulta = (select(UsuarioModel)
        .options(selectinload(UsuarioModel.cuentas)) 
        .where(UsuarioModel.dni == dniUser)
    )
    cuentaUser = session.exec(consulta).first()  

    if cuentaUser:
        return cuentaUser
    else:
        raise CuentaNoEncontradaError(f"No se encontro la o las cuentas asociadas al DNI {dniUser}")
        