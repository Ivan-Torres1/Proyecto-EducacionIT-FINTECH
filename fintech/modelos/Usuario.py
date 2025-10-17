from fintech.modelos.cuentaBancaria import CuentaBancaria


class Usuario:
    usuarioId = 0
    def __init__(self,nombre: str,apellido: str,dni: int,mail: str,contraseña: str):
        Usuario.usuarioId +=1
        self.id = Usuario.usuarioId
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
   
    def verMovimientos(self,idCuenta):
        pass


    def crearCuenta(self):
        titular = self.nombre+self.apellido
        cuenta = CuentaBancaria.crearDesdeUsuario(self,titular=self.nombre+self.apellido)
        self.__cuentas.append(cuenta)
        print(f"{self.nombre} su cuenta fue creada correctamente")

    def mostrarCuentas(self):
        for cuenta in self.__cuentas:
            print(cuenta)