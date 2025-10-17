import datetime


class Movimiento:
    def __init__(self,tipo,monto):
        self.tipo = tipo
        self.monto = monto
        self.fecha = datetime.datetime.now()

    def __str__(self):
        return f"[{self.fecha.strftime('%Y-%m-%d %H:%M')}] Tipo: {self.tipo}, Monto: ${self.monto:.2f}"