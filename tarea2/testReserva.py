#
# Autores: Christian Teixeira - 11-11016
#          Carlos Martínez - 11-10584 
#

import unittest
import datetime
import Reservacion

class Test(unittest.TestCase):

    def testValidateShortInterval(self):
        res = Reservacion()
        hoy = datetime.datetime.now()
        res.setFechaInicio(hoy.year, hoy.month, hoy.day, 0, 30)
        res.setFechaFin(hoy.year, hoy.month, hoy.day, 0, 44)
        self.assertEqual(res.validateTimeInterval(), -1)
        
    def testValidateBigInterval(self):
        res = Reservacion()
        hoy = datetime.datetime.now()
        res.setFechaInicio(hoy.year, hoy.month, hoy.day, 0, 30)
        res.setFechaFin(hoy.year, hoy.month, hoy.day + 4, 0, 30)
        self.assertEqual(res.validateTimeInterval(), 1)
    
    def testValidInterval_1(self):
        res = Reservacion()
        hoy = datetime.datetime.now()
        res.setFechaInicio(hoy.year, hoy.month, hoy.day, 0, 30)
        res.setFechaFin(hoy.year, hoy.month, hoy.day, 0, 45)
        self.assertEqual(res.validateTimeInterval(), 0)
        
    def testValidInterval_2(self):
        res = Reservacion()
        hoy = datetime.datetime.now()
        res.setFechaInicio(hoy.year, hoy.month, hoy.day, 1, 0)
        res.setFechaFin(hoy.year, hoy.month, hoy.day + 3, 0, 59)
        self.assertEqual(res.validateTimeInterval(), 0)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()