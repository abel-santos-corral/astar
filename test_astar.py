import unittest
from astar import Nodo, heuristica, generar_sucesores, reconstruir_camino, busqueda_Astar

class TestAStar(unittest.TestCase):
    def test_heuristica(self):
        self.assertEqual(heuristica([1,2,3,4]), 0)
        self.assertEqual(heuristica([4,3,2,1]), 6)
        self.assertEqual(heuristica([4,1,3,2]), 4)
        self.assertEqual(heuristica([2,3,4,1]), 10)  # Default case

    def test_generar_sucesores(self):
        nodo = Nodo([4,3,2,1])
        sucesores = generar_sucesores(nodo)
        self.assertEqual(len(sucesores), 3)  # Three possible swaps
        self.assertIn([3,4,2,1], [s.estado for s in sucesores])
        self.assertIn([4,2,3,1], [s.estado for s in sucesores])
        self.assertIn([4,3,1,2], [s.estado for s in sucesores])

    def test_reconstruir_camino(self):
        nodo1 = Nodo([1,2,3,4])
        nodo2 = Nodo([1,3,2,4], nodo1)
        nodo3 = Nodo([1,3,4,2], nodo2)
        self.assertEqual(reconstruir_camino(nodo3), [[1,2,3,4], [1,3,2,4], [1,3,4,2]])

    def test_busqueda_Astar(self):
        resultado = busqueda_Astar()
        self.assertEqual(resultado[0], [4,3,2,1])  # Initial state
        self.assertEqual(resultado[-1], [1,2,3,4])  # Goal state

if __name__ == "__main__":
    unittest.main()
