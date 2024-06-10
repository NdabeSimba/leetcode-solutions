[1. Two Sum](https://leetcode.com/problems/two-sum/)

| # | Memory | Time | Time Complexity|
| - | ------ | ---- | -------------- |
| 1 | 14.2 MB| 2259 ms | O(N^2)|
| 2 | 14.2 MB| 49 ms | O(N)|
| 3 | 14.1 MB| 43 ms | O(N)|
| 4 | 14.3 MB| 44 ms | O(N)|

---

## Task
Given an array of integers <code>nums</code> and an integer <code>target</code>, return indices of the two numbers such that they add up to <code>target</code>.

You may assume that each input would have *exactly one solution*, and you may not use the same element twice.

You can return the answer in any order.

---

## Example 1
<pre>
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
</pre>
---

## Example 2
<pre>
Input: nums = [3,2,4], target = 6
Output: [1,2]
</pre>
---

> Most of the times, in such a problem, using dictionary (hastable) helps.
>> try to be comfortable to use three built in functions/methods, enumerate, zip, set.