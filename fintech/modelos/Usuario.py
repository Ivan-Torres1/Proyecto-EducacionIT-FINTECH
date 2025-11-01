from typing import Optional, List,Annotated
from sqlmodel import SQLModel, Field, Relationship, Session
from pydantic import EmailStr,Field as pydanticField,field_validator #Para validación que no sea de bbdd
from servicios.loggingConfig import log



DNI = Annotated[str, pydanticField(pattern=r"^\d{8}$")]

class UsuarioModel(SQLModel,table=True):
    __tablename__ = "usuariomodel"
    id: Optional[int] = Field(default=None,primary_key=True)
    nombre:str = Field(min_length=3,max_length=50)
    apellido:str = Field(min_length=3,max_length=50)
    contraseña: str
    mail:EmailStr = Field(unique=True)
    dni:DNI = Field(unique=True)

    cuentas: List["Cuentas"] = Relationship(back_populates="usuario")

    @field_validator("contraseña")
    @classmethod
    def validar_contraseña(cls, value):
        if len(value) < 7:
            raise ValueError("La contraseña debe tener al menos 7 caracteres")
        if not any(c.isupper() for c in value):
            raise ValueError("La contraseña debe tener al menos una letra mayúscula")
        if not any(c.isdigit() for c in value):
            raise ValueError("La contraseña debe tener al menos un número")
        return value

    def __str__(self):
        return f"""
    Nombre: {self.nombre}
    Apellido: {self.apellido}
    Mail: {self.mail}
    DNI: {self.dni}
                """




    def crearUsuario(self,session: Session,nombre: str,apellido: str,contraseña:str,mail: str,dni: str):
        log("DEBUG","INTENTANDO CREAR UN USUARIO...")
        user = UsuarioModel(nombre=nombre,apellido=apellido,
                contraseña=contraseña,mail=mail,dni=dni)
        session.add(user)
        log("INFO","USUARIO CREADO CORRECTAMENTE") 

    
        










    # def crearCuenta(self):
    #         titular = self.nombre+self.apellido
    #         cuenta = CuentaBancaria.crearDesdeUsuario(self,titular=self.nombre+self.apellido)
    #         self.__cuentas.append(cuenta)
    #         print(f"{self.nombre} su cuenta fue creada correctamente")
    #         print("DATOS DE LA CUENTA")
    #         print(cuenta)

    # def mostrarCuentas(self):
    #     for cuenta in self.__cuentas:
    #         print(cuenta)