# python -m fintech.utils.main  
from modelos.cuentaBancaria import Cuentas
from modelos.Usuario import UsuarioModel
from modelos.Movimiento import Movimientos
from utils.database import createAll
from servicios.Sistema import logica


if __name__ == "__main__":
    createAll()
    logica()
   

