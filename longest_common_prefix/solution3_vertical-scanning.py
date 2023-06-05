# vertical scanning
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        strs.sort(key=lambda x: len(x)) 
        
        if len(strs) == 0:
            return
        else:
            for i in range(len(strs[0])):
                for j in range(1, len(strs)):
                    if strs[0][i] != strs[j][i]:
                        return strs[0][:i]
            return strs[0]
        
# strs 원소 개수: n
# 가장 짧은 원소 글자 수: m
# time complexity: O(n×logn) -> for loop 시간 복잡도 O(m×n) + sort 시간 복잡도 O(logn)
# 