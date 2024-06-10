# Brute Force, Sliding Window

# Time complexity: O(n*m)
# Space complexity: O(m)

from collections import deque
from itertools import islice, starmap, zip_longest
from operator import eq
from typing import Hashable, Iterable, Sequence


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return next(substring_brute_force(haystack, needle), -1)


T = Hashable
def substring_brute_force(haystack: Iterable[T], needle: Sequence[T]) -> Iterable[int]:
    haystack = iter(haystack)
    window = deque(islice(haystack, len(needle) - 1), maxlen=len(needle))
    for i, x in enumerate(haystack):
        window.append(x)
        if all(starmap(eq, zip_longest(window, needle, fillvalue=""))):
            yield i
    
self = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode" 
needle = "leeto"
print(Solution.strStr(self, haystack, needle))