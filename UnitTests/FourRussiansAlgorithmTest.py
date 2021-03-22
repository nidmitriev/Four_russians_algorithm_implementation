import main
import unittest
import numpy as np


class TestFourRussiansAlgorithm(unittest.TestCase):

    def simple_test(self):
        matrix_A = np.random.randint(2, size=(3,3))
        matrix_B = np.random.randint(2, size=(3,3))
        res1ult_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = res1ult_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

    def medium_test(self):
        matrix_A = np.random.randint(2, size=(10,10))
        matrix_B = np.random.randint(2, size=(10,10))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

    def difficult_test(self):
        matrix_A = np.random.randint(2, size=(50,50))
        matrix_B = np.random.randint(2, size=(50,50))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

    def complex_test(self):
        matrix_A = np.random.randint(2, size=(75, 75))
        matrix_B = np.random.randint(2, size=(75, 75))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

if __name__ == '__main__':
    unittest.main()
