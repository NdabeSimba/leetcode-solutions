class Solution(object):
    
    def isAnagram(self, s, t):

        def count_dict(st):
            count = dict()
            for char in st:
                if char in count:
                    count[char] = count.get(char) + 1
                else:
                    count[char] = 1
            return count
        
        return count_dict(s) == count_dict(t)


self = Solution()

s = "anagram"
t = "nagaram"
print(Solution.isAnagram(self, s, t))

s = "rat"
t = "car"
print(Solution.isAnagram(self, s, t))
