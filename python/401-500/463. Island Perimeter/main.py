from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 1
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 1
                    if i < rows - 1 and grid[i+1][j] == 1:
                        perimeter -= 1
                    if j < cols - 1 and grid[i][j+1] == 1:
                        perimeter -= 1
        
        return perimeter