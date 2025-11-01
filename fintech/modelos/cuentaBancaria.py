from typing import Optional
from sqlmodel import SQLModel,Field,Relationship,Session
from datetime import datetime
from servicios.helpModels import encontrarUserConDNI
from modelos.Movimiento import Movimientos
from servicios.loggingConfig import log

class Cuentas(SQLModel,table=True):
    __tablename__ = "cuentas"
    id:Optional[int]= Field(default=None,primary_key=True)
    usuarioId: Optional[int] = Field(foreign_key="usuariomodel.id")
    saldo: float = Field(default=0, ge=0)
    usuario: "UsuarioModel" = Relationship(back_populates="cuentas")
    movimientos: "Movimientos" = Relationship(back_populates="cuenta")


    def depositar(self, monto: float, session: Session, descripcion: str = None):
            if monto <= 0:
                raise ValueError("El monto debe ser mayor que cero")

            self.saldo += monto
            movimiento = Movimientos(
                cuenta_id=self.id,
                tipo="deposito",
                monto=monto,
                fecha=datetime.utcnow(),
                descripcion=descripcion
            )
            session.add(movimiento)

    def retirar(self, monto: float, session: Session, descripcion: str = None):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero")
        if self.saldo < monto:
            raise ValueError("Saldo insuficiente")

        self.saldo -= monto
        movimiento = Movimientos(
            cuenta_id=self.id,
            tipo="retiro",
            monto=monto,
            fecha=datetime.utcnow(),
            descripcion=descripcion
        )
        session.add(movimiento)

    def crearCuenta(self,session: Session,dniUser:int):
        log("DEBUG","\nINTENTANDO CREAR LA CUENTA...")
        user = encontrarUserConDNI(dniUser,Session)
        cuenta = Cuentas(usuarioId=user.id)
        session.add(cuenta)
        log("INFO","Cuenta creada correctamente")

