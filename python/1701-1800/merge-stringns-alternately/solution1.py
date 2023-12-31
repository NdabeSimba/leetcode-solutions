class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ind = 0
        result = list()
        
        while ind < len(word1) or ind < len(word2):
            if ind < len(word1):
                result.append(word1[ind])
            if ind < len(word2):
                result.append(word2[ind])
            
            ind += 1

        result = "".join(result)

        return result




self = Solution()

word1 = "ab" 
word2 = "pqrs"
print(Solution.mergeAlternately(self, word1, word2))
