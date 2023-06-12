# Knuth-Morris-Pratt
# https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm

# Time complexity: O(n + m)
# Space complexity: O(m)

from collections import defaultdict
from itertools import accumulate
from typing import Hashable, Iterable, Mapping, Sequence

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return next(substring_knuth_morris_pratt(haystack, needle), -1)


T = Hashable
def substring_knuth_morris_pratt(haystack: Iterable[T], needle: Iterable[T]) -> Iterable[int]:
    DFA = Sequence[Mapping[T, int]]

    def dfa(xs: Iterable[T]) -> DFA:
        transitions = []

        t = defaultdict(int)
        for i, x in enumerate(xs):
            transitions.append(t | {x: i + 1})
            t = transitions[t[x]]

        return transitions

    needle_dfa = dfa(needle)
    end_state = len(needle_dfa)

    states = accumulate(haystack, lambda st, x: needle_dfa[st][x], initial=0)
    return (i - end_state for i, st in enumerate(states) if st == end_state)
    
self = Solution()
haystack = "sadbutsad" 
needle = "sad"
print(Solution.strStr(self, haystack, needle))

haystack = "leetcode" 
needle = "leeto"
print(Solution.strStr(self, haystack, needle))