# (2825. Make String a Subsequence Using Cyclic Increments)[https://leetcode.com/problems/make-string-a-subsequence-using-cyclic-increments]

__Type:__ Medium <br>
__Topics:__ Two Pointers, String <br>
__Companies:__ Amazon
<hr>

You are given two __0-indexed__ strings `str1` and `str2`.

In an operation, you select a set of indices in `str1`, and for each index `i` in the set, increment `str1[i]` to the next character **cyclically**. That is `'a'` becomes `'b'`, `'b'` becomes `'c'`, and so on, and `'z'` becomes `'a'`.

Return `true` *if it is possible to make* `str2` *a subsequence of* `str1` *by performing the operation ***at most once***, and* `false` *otherwise.*

**Note:** A subsequence of a string is a new string that is formed from the original string by deleting some (possibly none) of the characters without disturbing the relative positions of the remaining characters.
<hr>

### Examples:
- **Example 1:** <br>
**Input:** str1 = "abc", str2 = "ad" <br>
**Output:** true <br>
**Explanation:** Select index 2 in str1. <br>
Increment str1[2] to become 'd'. <br>
Hence, str1 becomes "abd" and str2 is now a subsequence. Therefore, true is returned.

- **Example 2:** <br>
**Input:** str1 = "zc", str2 = "ad" <br>
**Output:** true <br>
**Explanation:** Select indices 0 and 1 in str1. <br>
Increment str1[0] to become 'a'. <br>
Increment str1[1] to become 'd'. <br>
Hence, str1 becomes "ad" and str2 is now a subsequence. Therefore, true is returned.

- **Example 3:** <br>
**Input:** str1 = "ab", str2 = "d" <br>
**Output:** false <br>
**Explanation:** In this example, it can be shown that it is impossible to make str2 a subsequence of str1 using the operation at most once. <br>
Therefore, false is returned.
<hr>

### Constraints:
- <code>1 <= str1.length <= 10<sup>5</sup></code>
- <code>1 <= str2.length <= 10<sup>5</sup></code>
- `str1` and `str2` consist of only lowercase English letters.
<hr>

### Hints
- Consider the indices we will increment separately.
- We can maintain two pointers: pointer `i` for `str1` and pointer `j` for `str2`, while ensuring they remain within the bounds of the strings.
- If both `str1[i]` and `str2[j]` match, or if incrementing `str1[i]` matches `str2[j]`, we increase both pointers; otherwise, we increment only pointer `i`.
- It is possible to make `str2` a subsequence of `str1` if `j` is at the end of `str2`, after we can no longer find a match.