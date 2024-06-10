from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        
        start, end = set(), set()

        for cities in paths:
            start.add(cities[0])
            end.add(cities[1])

        for city in end:
            if city in start:
                continue
            else:
                return city