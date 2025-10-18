from modelos.Movimiento import Movimiento


class CuentaBancaria:
    cuentaId = 0
    def __init__(self,usuarioAsociado:str,titular,saldo=0):
        CuentaBancaria.cuentaId += 1
        self._id = CuentaBancaria.cuentaId
        self.titular = titular
        self.__saldo = saldo
        self._usuarioAsociado = usuarioAsociado
        self.__movimiento = []

    @classmethod          
    def crearDesdeUsuario(cls,usuario,titular,saldo=0):
        return cls(usuario,titular,saldo)

    @property
    def saldo(self):
        if self.__saldo >= 0:
            return self.__saldo
        else:
            raise ValueError("El saldo no puede ser negativo")
        
    @saldo.setter
    def saldo(self,nuevoSaldo: int):
        if nuevoSaldo > 0:
            self.__saldo = nuevoSaldo
        else:
            raise ValueError("El saldo no puede ser negativo")
    
    @property
    def movimientos(self):
        return self.__movimiento.copy()



    def __str__(self):
        return f""" 
    ---
    {self._usuarioAsociado}
    ID de cuenta: {self._id}
    Titular: {self.titular}
    Saldo actual: {self.saldo}
    ---
        """

    def retirar(self,monto: int):
        if monto > 0 and monto <= self.__saldo:
            self.saldo = self.__saldo - monto
            print("OPERACIÓN: RETIRAR")
            print(f"Se retiraron {monto} de su cuenta")
            print(f"Dinero actual en su cuenta: {self.saldo}\n")
            self.registrarMovimiento("Retirar",monto)
        else:
            raise ValueError("El monto es negativo o mayor a su saldo actual")


    def depositar(self,monto: int):
        if monto > 0:
            self.saldo += monto
            print("OPERACIÓN: DEPOSITAR")
            print(f"Operación exitosa, se depositarón {self.saldo}")
            self.registrarMovimiento("Depositar",monto)


    def registrarMovimiento(self, tipo, monto):
        mov = Movimiento(tipo,monto)
        self.__movimiento.append(mov)


   