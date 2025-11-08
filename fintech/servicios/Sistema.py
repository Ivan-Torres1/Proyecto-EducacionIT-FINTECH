from utils.database import engine
from modelos.Usuario import UsuarioModel
from modelos.cuentaBancaria import Cuentas
from servicios.helpModels import encontrarUserConDNI,encontrarCuentasUsuario
from sqlmodel import Session


def logica():
    # Donde ejecutamos la logica del codigo (donde pruebo los metodos y 
    # funciones para saber que funcionan correctamente)
    with Session(engine) as session:
        #                   Crear un usuario
        # user = UsuarioModel()
        # user.crearUsuario(nombre="David",apellido="Zalazar",contraseña="1233",dni=10293884,mail="davidZ@gmail.com",session=session)
        #                   Crear una cuenta para ese usuario
        # cuenta = Cuentas()
        # cuenta.crearCuenta(dniUser=37103993,session=session)
        #                   Buscar cuenta de un usuario a travez de su DNI
        # cuentas = encontrarCuentasUsuario(dniUser=47100000,session=session)
        # for i in cuentas:
        #     print(f"""
        # ID: {i.id}
        # Saldo: {i.saldo}""")
        pass