import main
import unittest
import numpy as np


class TestFourRussiansAlgorithm(unittest.TestCase):

    def big_matrices_test(self):
        matrix_A = np.random.randint(2, size=(100,100))
        matrix_B = np.random.randint(2, size=(100,100))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

    def very_big_matrices_test(self):
        matrix_A = np.random.randint(2, size=(250,250))
        matrix_B = np.random.randint(2, size=(250,250))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

    def large_matrices_test(self):
        matrix_A = np.random.randint(2, size=(500,500))
        matrix_B = np.random.randint(2, size=(500,500))
        result_1 = np.dot(matrix_A.astype(bool), matrix_B.astype(bool))
        result_1 = result_1.astype(int)
        result_2 = main.four_russians_alg(matrix_A, matrix_B)
        result_2 = result_2.astype(int)
        np.testing.assert_array_equal(result_1, result_2)

if __name__ == '__main__':
    unittest.main()
