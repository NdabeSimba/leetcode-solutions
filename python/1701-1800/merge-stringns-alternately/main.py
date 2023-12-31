class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        leng = min(len(word1), len(word2))
        ind = 0
        result = list()
        
        while ind < leng:
            result.append(word1[ind])
            result.append(word2[ind])
            ind += 1

        if len(word1) > leng:
            result.append(word1[ind:])
        else:
            result.append(word2[ind:])

        result = "".join(result)

        return result




self = Solution()

word1 = "ab" 
word2 = "pqrs"
print(Solution.mergeAlternately(self, word1, word2))
