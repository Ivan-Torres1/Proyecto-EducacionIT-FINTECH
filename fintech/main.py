from modelos.Usuario import Usuario
from modelos.cuentaBancaria import CuentaBancaria


# Creo un usuario
usuario = Usuario("Ivan","Torres",47103883,"ivantorres@gmail.com","1234")
#Le creo una cuenta al usuario
usuario.crearCuenta()
#Deposito dinero en su primer cuenta creada
usuario.cuentas[0].depositar(1000)
#Creo una segunda cuenta
usuario.crearCuenta()
#Deposito dinero en su segunda cuenta
usuario.cuentas[1].depositar(200)
#Retiro dinero de su primer cuenta
usuario.cuentas[0].retirar(100)

#Imprimo todos los movimientos que hubo en la primer cuenta
print("------------------------------")
for i in usuario.cuentas[0].movimientos:
    print(i)

#Imprimo todos los movimientos que hubo en la segunda cuenta
for i in usuario.cuentas[1].movimientos:
    print(i)
