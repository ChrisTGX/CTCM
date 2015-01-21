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
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()