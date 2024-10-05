from typing import List
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()

        for i, num in enumerate(nums):
            while window and window[-1] < num:
                window.pop()
            window.append(num)
            # make window, keeping the window elements in descending order
            # (to make first element of the window max number)
            # --> if last element is smaller than num, pop that element to keep the descending order

            if i >= k and nums[i - k] == window[0]:
                window.popleft()
            # deleting first element of the window from index == k
            # cheking if first element matches nums[i - k],
            # it might not be the same because of window making max element index 0

            if i >= k - 1:
                result.append(window[0])
            # when window reaches size k (index k - 1), start appending max element(first element in window) to result

        return result
