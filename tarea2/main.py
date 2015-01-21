#
# Autores: Christian Teixeira - 11-11016
#          Carlos Martínez - 11-10584 
#

import Reservacion, Tarifa
if __name__ == '__main__':
    newReservation = Reservacion()
    print("FECHA DE ENTRADA")
    year = input("Introduzca año: ")
    month = input("Introduzca mes: ")
    day = input("Introduzca dia: ")
    hour = input("Introduzca hora: ")
    minute = input("Introduzca minuto: ")
    
    newReservation.setEntrada(year, month, day, hour, minute)
    
    print("FECHA SALIDA")
    year = input("Introduzca año: ")
    month = input("Introduzca mes: ")
    day = input("Introduzca dia: ")
    hour = input("Introduzca hora: ")
    minute = input("Introduzca minuto: ")
    
    newReservation.setSalida(year, month, day, hour, minute)
    
    horaDiurna = input("Escoja monto hora diurna: ")
    horaNocturna = input("Escoja monto hora nocturna: ")
    
    nuevaTarifa = Tarifa(horaDiurna, horaNocturna, newReservation.entrada, newReservation.salida)