[13. Roman to Integer](https://leetcode.com/problems/roman-to-integer/)

| # | Memory | Time |
| - | ----- | -------- |
| 1 |16.2 MB|60 ms
| 2 |16.2 MB|68 ms

---

## Task
Roman numerals are represented by seven different symbols: <code>I, V, X, L, C, D and M</code>.
<pre>
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
</pre>
For example, <code>2</code> is written as <code>II</code> in Roman numeral, just two ones added together. <code>12</code> is written as <code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:

- <code>I</code> can be placed before <code>V (5) and X (10)</code> to make 4 and 9. 
- <code>X</code> can be placed before <code>L (50) and C (100)</code> to make 40 and 90. 
- <code>C</code> can be placed before <code>D (500) and M (1000)</code> to make 400 and 900.

Given a roman numeral, convert it to an integer.

---

## Example 1
<pre>
Input: s = "III"
Output: 3
Explanation: III = 3.
</pre>

---

## Example 2
<pre>
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
</pre>
---

## Example 3
<pre>
Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>