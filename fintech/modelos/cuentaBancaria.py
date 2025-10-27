from typing import Optional
# from sqlmodel import SQLModel, Field, Relationship,Session
from sqlmodel import SQLModel,Field,Relationship,Session
from fintech.modelos.Movimiento import Movimientos
from datetime import datetime
from fintech.utils.helpModels import encontrarUserConDNI


class Cuentas(SQLModel,table=True):
    __tablename__ = "cuentas"
    id:Optional[int]= Field(default=None,primary_key=True)
    usuarioId: int = Field(foreign_key="usuariomodel.id")
    saldo: float = Field(default=0, ge=0)
    usuario: "usuariomodel" = Relationship(back_populates="cuentas")
    movimientos: "movimientos" = Relationship(back_populates="cuenta")


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
        user = encontrarUserConDNI(dniUser,Session)
        cuenta = Cuentas(usuarioId=user.id)
        session.add(cuenta)
    

