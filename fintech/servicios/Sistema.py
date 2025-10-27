from fintech.utils.database import engine
from fintech.modelos.Usuario import UsuarioModel
from fintech.modelos.cuentaBancaria import Cuentas
from sqlmodel import Session


def logica():
    with Session(engine) as session:
        user = UsuarioModel()
        user.crearUsuario(nombre="Jorge",apellido="Matt",contraseña="Max111",dni=47103884,mail="Jorge@gmail.com",session=session)
        session.commit() 

        cuenta = Cuentas()
        cuenta.crearCuenta(dniUser=47103883,session=session)
        session.commit()