from typing import List

class Solution:
    # def findCenter(self, edges: List[List[int]]) -> int:
    #     leng = len(edges)
    #     hashmap = [0] * (leng + 2)
    #     print(hashmap)
    #     for n1, n2 in edges:
    #         print(n1, n2)
    #         hashmap[n1] += 1
    #         hashmap[n2] += 1
    #     print(hashmap)
    #     for i in range(1, leng + 2):
    #         if hashmap[i] == leng:
    #             return i

    #     return -1

    def findCenter(self, edges: List[List[int]]) -> int:
        hashset = set()

        for n1, n2 in edges:
            if n1 in hashset:
                return n1

            if n2 in hashset:
                return n2

            hashset.add(n1)
            hashset.add(n2)
