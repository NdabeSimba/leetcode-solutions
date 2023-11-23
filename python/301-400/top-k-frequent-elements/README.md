| #   | Name                                                                                               | Difficulty |
| --- | -------------------------------------------------------------------------------------------------- | ---------- |
| 347 | [347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/description/) | Medium     |

---

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

---

## Example 1

<pre>
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
</pre>

---

## Example 2

<pre>
Input: nums = [1], k = 1
Output: [1]
</pre>

---

## Example 3

<pre>
Input: nums = [4,1,-1,2,-1,2,3], k = 2
Output: [-1, 2]
</pre>

## Constraints

- 1 <= nums.length <= 105
- -104 <= nums[i] <= 104
- k is in the range [1, the number of unique elements in the array].
- It is guaranteed that the answer is unique.

**Follow up**: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
