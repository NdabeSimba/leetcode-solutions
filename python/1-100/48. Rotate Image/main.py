from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side = len(matrix)
        top = 0
        bottom = len(matrix) - 1

        while top < bottom:
            for col in range(side):
                matrix[top][col], matrix[bottom][col] = matrix[bottom][col], matrix[top][col]
            top += 1
            bottom -= 1

        for row in range(side):
            for col in range(row + 1, side):
                # using row + 1 to ensure elements are swapped only once
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        return matrix