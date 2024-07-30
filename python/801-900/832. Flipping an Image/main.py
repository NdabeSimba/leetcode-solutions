from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        side = len(image)
        top = len(image[0])
        for row in range(side):
            image[row] = image[row][::-1]
            for col in range(top):
                if image[row][col] == 0:
                    image[row][col] = 1
                else:
                    image[row][col] = 0
        return image
