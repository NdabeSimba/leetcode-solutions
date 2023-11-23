import collections


class Solution(object):
    def groupAnagrams(self, strs):
        answer = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            
            for c in s:
                count[ord(c) - ord("a")] += 1
            answer[tuple(count)].append(s)
            
        return answer.values()
        


self = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]
print(Solution.groupAnagrams(self, strs))

strs = [""]
print(Solution.groupAnagrams(self, strs))
