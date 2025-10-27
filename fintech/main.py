# python -m fintech.utils.main  
from fintech.modelos.cuentaBancaria import Cuentas
from fintech.modelos.Usuario import UsuarioModel
from fintech.modelos.Movimiento import Movimientos
from fintech.utils.database import createAll
from fintech.servicios.Sistema import logica


if __name__ == "__main__":
    createAll()
    logica()
   

