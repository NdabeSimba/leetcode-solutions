from typing import List

class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_rows = set()
        max_cols = set()

        for row in matrix:
            min_rows.add(min(row))
        for col in zip(*matrix):
            max_cols.add(max(col))

        return list(min_rows & max_cols)
