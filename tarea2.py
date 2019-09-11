import unittest


def sumOfIntegers():
    suma = 0
    for number in range(0,101):
        suma = suma + number
    return (suma)
                
    
suma1= sumOfIntegers()

class Prueba(unittest.TestCase):

   def test(self):
        self.assertEqual(5050,sumOfIntegers())
        
   def test2(self):
        self.assertEqual(5051,sumOfIntegers())
        
        
if __name__ == '__main__':
    unittest.main()
