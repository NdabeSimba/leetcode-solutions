from typing import List


def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
    result = []
    total = len(matrix[0]) * len(matrix)

    while left <= right and top <= bottom:
        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1  # went through top row

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1  # went through right column

        for col in range(right, left - 1, -1):
            result.append(matrix[bottom][col])
        bottom -= 1  # went through bottom row

        for row in range(bottom, top - 1, -1):
            result.append(matrix[row][left])
        left += 1  # went through left column

        # go back to top for loop, going through top + 1 row

    return result[:total]
