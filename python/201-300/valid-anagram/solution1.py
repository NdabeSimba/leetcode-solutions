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

# Jan 6 2023 submission
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        def letters(st):
            st_dict = dict()

            for l in st:
                if l in st_dict:
                    st_dict[l] += 1
                else:
                    st_dict[l] = 1
            
            return st_dict

        return letters(s) == letters(t)