import numpy as np
import math


def split_block(matrix, start, row, size):
    """
    Split block from matrix (row or column):
        matrix: matrix to extract from
        start: start index to cut from
        row: true if extracting block is a row, false if it is a column
        size: size of extracting block
        return: extracted block
    """

    if row:
        block_size = min(size, matrix.shape[0])
        extracted_row = matrix[start: start + block_size]
        extracted_block = np.asmatrix(extracted_row)
    else:
        block_size = min(size, matrix.shape[1])
        extracted_column = []
        for i in range(matrix.shape[0]):
            extracted_column.append(matrix[i][start: start + block_size])
        extracted_block = np.asmatrix(extracted_column)
    return extracted_block



def _block_size(matrix_A, matrix_B):
    """
    Block size calculation:
        matrix_A: Left matrix
        matrix_B: Right matrix
        return: block size (if matrices are incorrect, returns -1)
    """

    size_a = matrix_A.shape[0]
    size_b = matrix_B.shape[0]
    if size_a == size_b:
        return math.floor(math.log2(size_a))
    else:
        return -1


def rows_addition(matrix_A, matrix_B, matrix_A_index, matrix_B_index):
    """
    Rows (vectors) addition:
        matrix_A: left matrix
        matrix_B: right matrix
        matrix_A_index: left matrix index
        matrix_B_index: right matrix index
        return: final row vector
    """

    row_vector = matrix_A[matrix_A_index].copy()
    column_vector = np.asarray(matrix_B[matrix_B_index]).reshape(-1)
    for i, item in enumerate(column_vector):
        row_vector[i] = int(row_vector[i]) | int(item)
    return row_vector


def int_convertation(row):
    """
    Converting binary row to int number:
        row: bool vector
        return: int number
    """

    row = np.asarray(row).reshape(-1)
    bit_str = ""
    for i in range(len(row)):
        bit_str += str(row[i])
    return int(bit_str,2)


def matrix_multiplication(left_matrix, right_matrix):
    """
    Matrix multiplication:
        left_matrix: row matrix block
        right_matrix: column matrix block
        return: multiplied matrix
    """

    size = left_matrix.shape[0]
    matrix = np.zeros((size, size))
    vectors = np.zeros((pow(2, left_matrix.shape[1]), size))
    between_powers = 1
    count = 0
    for i in range(1, pow(2, left_matrix.shape[1])):
        new_row = rows_addition(vectors, right_matrix, i - pow(2, count), right_matrix.shape[0] - count - 1)
        vectors[i,:] = new_row
        if between_powers == 1:
            between_powers = i + 1
            count += 1
        else:
            between_powers -= 1
    for i in range(size):
        matrix[i] = vectors[int_convertation(left_matrix[i])]
    return matrix



def matrices_OR(matrix_A, matrix_B):
    """
    OR operation for matrices:
        matrix_A: left matrix
        matrix_B: right matrix
        return: result matrix
    """

    for i in range(matrix_A.shape[0]):
            for j in range(matrix_A.shape[1]):
                matrix_A[i][j] = int(matrix_A[i][j]) | int(matrix_B[i][j])
    return matrix_A


def four_russians_alg(matrix_A, matrix_B):
    """
    Implementation of matrix multiplication by Four Russians algorithm
        matrix_A: first matrix
        matrix_B: second matrix
        return: final matrix
    """

    dim = matrix_A.shape[0]
    block_size = _block_size(matrix_A, matrix_B)
    number_of_blocks = math.ceil(dim/block_size)
    matrix = np.zeros((dim, dim))
    for i in range(number_of_blocks):
        column_block = split_block(matrix_A, i * block_size, False, block_size)
        row_block = split_block(matrix_B, i * block_size, True, block_size)
        multiplied_block = matrix_multiplication(column_block, row_block)
        matrix = matrices_OR(matrix, multiplied_block)
    return matrix.astype(int)


def main():
    # Matrix_A - left matrix
    matrix_A = np.loadtxt("matrixA.txt", dtype='i', delimiter=',')

    # Matrix_B - right matrix
    matrix_B = np.loadtxt("matrixB.txt", dtype='i', delimiter=',')

    if (matrix_A.shape[0] == matrix_A.shape[1] & matrix_B.shape[0] == matrix_B.shape[1] & matrix_A.shape[0] == matrix_B.shape[1]):
        print(four_russians_alg(matrix_A, matrix_B))


if __name__ == "__main__":
    main()
