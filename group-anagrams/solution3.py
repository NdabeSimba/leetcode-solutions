class Solution:
    def groupAnagrams(self, strs):
        strs_table = {}
        for string in strs:
            key = [0] * 26
    
            for char in string:
                    key[ord(char)-ord('a')] += 1 
            strs_key = tuple(key)

            if strs_key not in strs_table:
                    strs_table[strs_key] = []

            strs_table[strs_key].append(string)

        return list(strs_table.values())
    

self = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(self, strs))

strs = [""]
print(Solution.groupAnagrams(self, strs))
