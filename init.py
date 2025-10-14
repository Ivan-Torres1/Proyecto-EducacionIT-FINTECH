class CuentaBancaria:
    def __init__(self,usuarioAsociado:str,titular,saldo=0):
        if not isinstance(usuarioAsociado,Usuario):
            raise TypeError("Se necesita un usuario para crear una cuenta bancaria.")
        self.titular = titular
        self.__saldo = saldo
        self._usuarioAsociado = usuarioAsociado

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
    
    
    def retirar(self,monto: int):
        if monto > 0 and monto <= self.__saldo:
            self.saldo = self.__saldo - monto
            print(f"\nSe retiraron {monto} de su cuenta")
            print(f"Dinero actual en su cuenta {self.saldo}\n")
        else:
            raise ValueError("El monto es negativo o mayor a su saldo actual")

    def depositar(self,monto: int):
        if monto > 0:
            self.saldo += monto
            print("\nOperación exitosa")
            print(f"Saldo actual {self.saldo}\n")

    def __str__(self):
        return f""" 
    ---
    {self._usuarioAsociado}
    Titular: {self.titular}
    Saldo actual: {self.saldo}
    ---
        """


    @classmethod          
    def crearDesdeUsuario(cls,usuario,titular,saldo=0):
        return cls(usuario,titular,saldo)
        


class Usuario:
    def __init__(self,nombre: str,apellido: str,dni: int,mail: str,contraseña: str):
        self.nombre = nombre
        self.apellido = apellido
        self.mail = mail
        self._dni = dni
        self.__contraseña = contraseña
        self.__cuentas = [] 


    @property
    def contraseña(self):
        return "***"
    
    @property
    def dni(self):
        return self._dni
    @property
    def cuentas(self):
        return self.__cuentas
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nApellido: {self.apellido}\nMail: {self.mail}\nContraseña: {self.contraseña}"

    def crearCuenta(self):
        titular = self.nombre+self.apellido
        cuenta = CuentaBancaria.crearDesdeUsuario(self,titular=self.nombre+self.apellido)
        self.__cuentas.append(cuenta)
        print("Cuenta creada correctamente")
        # print(cuenta)

    def mostrarCuentas(self):
        for cuenta in self.__cuentas:
            print(cuenta)

usuario = Usuario("Ivan","Torres",47103883,"ivantorres@gmail.com","1234")
usuario.crearCuenta()
usuario.cuentas[0].depositar(1000)
usuario.mostrarCuentas()
usuario.crearCuenta()
usuario.cuentas[1].depositar(2500)
usuario.cuentas[1].retirar(100)
usuario.mostrarCuentas()



