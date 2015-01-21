
import unittest
import datetime
from reserva import reservacion

class Test(unittest.TestCase):

    def testValidateShortInterval(self):
        res = reservacion()
        hoy = datetime.datetime.now()
        res.setFechaInicio(hoy.year, hoy.month, hoy.day, 0, 30)
        res.setFechaFin(hoy.year, hoy.month, hoy.day, 0, 44)
        self.assertEqual(res.validateTimeInterval(), -1)
        
    def testValidateBigInterval(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()