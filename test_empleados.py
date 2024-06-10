import unittest
from clases import Empleado, Gerente

class TestEmpleado(unittest.TestCase):

    def setUp(self):
        self.empleado = Empleado("Carlos", 45, 70000)
        self.gerente = Gerente("María", 50, 90000, 15000)

    def test_creacion_empleado(self):
        self.assertEqual(self.empleado.nombre, "Carlos")
        self.assertEqual(self.empleado.edad, 45)
        self.assertEqual(self.empleado.salario_anual, 70000)

    def test_creacion_gerente(self):
        self.assertEqual(self.gerente.nombre, "María")
        self.assertEqual(self.gerente.edad, 50)
        self.assertEqual(self.gerente.salario_anual, 90000)
        self.assertEqual(self.gerente.bono, 15000)

    def test_propiedades_empleado(self):
        self.empleado.nombre = "Luis Alberto"
        self.assertEqual(self.empleado.nombre, "Luis Alberto")
        
        self.empleado.edad = 33
        self.assertEqual(self.empleado.edad, 33)

        self.empleado.salario_anual = 58000
        self.assertEqual(self.empleado.salario_anual, 58000)

    def test_propiedades_gerente(self):
        self.gerente.bono = 20000
        self.assertEqual(self.gerente.bono, 20000)

    def test_calculo_salario_empleado(self):
        self.assertEqual(self.empleado.calcular_salario_mensual(), 70000 / 12)

    def test_calculo_salario_gerente(self):
        self.assertEqual(self.gerente.calcular_salario_mensual(), (90000 + 15000) / 12)

    def test_polimorfismo(self):
        def mostrar_salario(empleado):
            if isinstance(empleado, Empleado):
                return empleado.calcular_salario_mensual()

        self.assertEqual(mostrar_salario(self.empleado), 70000 / 12)
        self.assertEqual(mostrar_salario(self.gerente), (90000 + 15000) / 12)

if __name__ == '__main__':
    unittest.main()
