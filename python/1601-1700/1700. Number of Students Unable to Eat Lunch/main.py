from typing import List

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        remaining = [0, 0]
        
        for student in students:
            remaining[student] += 1
        
        for sandwich in sandwiches:
            if remaining[sandwich] == 0:
                break
            remaining[sandwich] -= 1
        
        return sum(remaining)