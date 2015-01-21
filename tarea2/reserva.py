
import datetime
import decimal

class tarifa:
    
    def _init_(self):
        self.diurna = decimal(0)
        self.nocturna = decimal(0)
    
    def setDiurna(self, monto):
        self.diurna = monto
        
    def setNocturna(self, monto):
        self.nocturna = monto

class reservacion:
    
    def __init__(self):
        self.fechaInicio = datetime.datetime.now()
        self.fechaFin = datetime.datetime.now()
        
    def setFechaInicio(self, year, month, day, hour, minute):
        self.fechaInicio = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute)
        
    def setFechaFin(self, year, month, day, hour, minute):
        self.fechaFin = datetime.datetime(year = year, month = month, day = day, hour = hour, minute = minute)
    
    def validateTimeInterval(self):
        deltaTime = self.fechaFin - self.fechaInicio
        if (deltaTime.seconds / 60) < 15:
            print("La reservación debe ser de al menos 15 minutos.")
            return -1
        elif (deltaTime.seconds / (3600*24)) > 3:
            print("La reservación debe ser de a lo sumo 72 horas.")
            return 1
        else:
            return 0
            