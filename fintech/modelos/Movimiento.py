from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field, Relationship

class Movimientos(SQLModel,table=True):
    __tablename__ = "movimientos"
    id: Optional[int]= Field(default=None, primary_key=True)
    idCuenta: int = Field(foreign_key="cuentas.id")
    monto: float = Field(gt=0)
    fecha: datetime = Field(default_factory=datetime.utcnow)
    descripcion: Optional[str]= None
    cuenta: "Cuentas" = Relationship(back_populates="movimientos")



    

