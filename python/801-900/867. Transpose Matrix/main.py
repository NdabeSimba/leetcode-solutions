from typing import List

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        side = len(matrix)
        top = len(matrix[0])
        for col in range(top):
            temp = []
            for row in range(side):
                temp.append(matrix[row][col])
            result.append(temp)
        return result