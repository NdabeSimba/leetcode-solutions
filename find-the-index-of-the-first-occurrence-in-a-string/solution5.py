# Boyer–Moore string-search algorithm
# https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_string-search_algorithm

# Time complexity: O(n + m)
# Space complexity: O(m)

from collections import defaultdict, deque
from itertools import islice
from typing import Hashable, Iterable, Mapping, Sequence


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return next(substring_boyer_moore(haystack, needle), -1)


T = Hashable
def substring_boyer_moore(haystack: Iterable[T], needle: Sequence[T]) -> Iterable[int]:
    SkipTable = Mapping[T, int]

    def skip_table(xs: Iterable[T]) -> SkipTable:
        return defaultdict(lambda: -1, {ch: i for i, ch in enumerate(xs)})

    n = len(needle)
    skip_t = skip_table(needle)
    
    haystack = iter(haystack)
    xs = tuple(islice(haystack, n))
    if len(xs) < n: return
    window = deque(xs, maxlen=n)

    i = 0
    while xs:
        j = next((j for j in range(n - 1, -1, -1) if window[j] != needle[j]), -1)
        if j < 0: yield i
        steps = max(1, j - skip_t[window[j]])
        xs = tuple(islice(haystack, steps))
        window.extend(xs)
        i += steps
    
self = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode" 
needle = "leeto"
print(Solution.strStr(self, haystack, needle))