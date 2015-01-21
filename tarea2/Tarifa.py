#
# Autores: Christian Teixeira - 11-11016
#          Carlos Martínez - 11-10584 
#

import datetime

class Tarifa(object):
    '''
    classdocs
    '''
    def calcularMonto(self, llegada, salida):
        horini = llegada.hour
        if(horini == 23):
            horfin = 0
        else:
            horfin = horini + 1
        diaActual = llegada.day
        monto = 0

        while(diaActual <= salida.day):
            print("En este momento horini es " + str(horini) + " y horfin es " + str(horfin) + " y monto es " + str(monto))
            # Nocturno
            if (horfin < 6) or (horini >= 18) or ((horini == 18 or horfin == 6) and llegada.minute == 0):
                print("Nocturno")
                monto = monto + self.horaNocturna
            # Diurno
            if(horini >= 6 and horfin < 18 and horini < horfin) or ((horini == 6 or horfin == 18) and llegada.minute == 0):
                print("Diurno")
                monto = monto + self.horaDiurna
            # Hora mas cara
            if (horini == 17 or horini == 5) and llegada.minute != 0:
                print("Mas cara")
                monto = monto + max(self.horaDiurna, self.horaNocturna)


            if(horini == 23):
                diaActual = diaActual + 1
            horini = horfin
            if(horfin == 23):
                horfin = 0
            else:
                horfin = horfin + 1

            if diaActual == salida.day and (horini > salida.hour or (horfin > salida.hour and llegada.minute == salida.minute)):
                break
        return monto
        


    def __init__(self, horaDiurna, horaNocturna, llegada, salida):
        self.horaDiurna = horaDiurna
        self.horaNocturna = horaNocturna
        self.monto = self.calcularMonto(llegada, salida)
        