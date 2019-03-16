import numpy as np

class RotateMatrix(object):

    def rotate90(self, matrix):
        """
        To rotate a matrix by 90 degrees, transpose it first, then reverse each column.
        :param matrix:
        :return:
        """
        tmatrix = self.transpose(matrix)
        rmatrix = self.reverseColumns(tmatrix)
        return rmatrix

    def transpose(self, matrix):
        for i in range(matrix.shape[0]):
            for j in range(i, matrix.shape[1]):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = tmp
        return matrix

    def reverseColumns(self, matrix):
        """
        For every column:
            swap elements from beginning to start, until the column is reversed.
        :param matrix:
        :return:
        """
        for i in range(matrix.shape[0]):
            j = 0
            k = matrix.shape[0] - 1
            while j < k:
                tmp = matrix[j][i]
                matrix[j][i] = matrix[k][i]
                matrix[k][i] = tmp
                j += 1
                k -= 1
        return matrix


if __name__ == "__main__":
    matrix = np.array([
        [1,2],
        [4,5]
    ])
    rm = RotateMatrix()
    result = rm.rotate90(matrix)
    print(result)
