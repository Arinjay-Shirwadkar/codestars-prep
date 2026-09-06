# 1993. Sum of All Subset XOR Totals

[https://leetcode.com/problems/sum-of-all-subset-xor-totals/](https://leetcode.com/problems/sum-of-all-subset-xor-totals/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         The XOR total of an array is defined as the bitwise XOR of all its elements, or 0 if the array is empty.

                  For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.

         Given an array nums, return the sum of all XOR totals for every subset of nums.

         Note: Subsets with the same elements should be counted multiple times.

         An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements
         of b.

         Example 1:

              Input: nums = [1,3]
              Output: 6
              Explanation: The 4 subsets of [1,3] are:
              - The empty subset has an XOR total of 0.
              - [1] has an XOR total of 1.
              - [3] has an XOR total of 3.
              - [1,3] has an XOR total of 1 XOR 3 = 2.
              0 + 1 + 3 + 2 = 6

         Example 2:

              Input: nums = [5,1,6]
              Output: 28
              Explanation: The 8 subsets of [5,1,6] are:
              - The empty subset has an XOR total of 0.
              - [5] has an XOR total of 5.
              - [1] has an XOR total of 1.
              - [6] has an XOR total of 6.
              - [5,1] has an XOR total of 5 XOR 1 = 4.
              - [5,6] has an XOR total of 5 XOR 6 = 3.
              - [1,6] has an XOR total of 1 XOR 6 = 7.
              - [5,1,6] has an XOR total of 5 XOR 1 XOR 6 = 2.
              0 + 5 + 1 + 6 + 4 + 3 + 7 + 2 = 28

         Example 3:

              Input: nums = [3,4,5,6,7,8]
              Output: 480
              Explanation: The sum of all XOR totals for every subset is 480.

         Constraints:

                  1 <= nums.length <= 12
                  1 <= nums[i] <= 20

## Approach / Intuition

_(fill in)_

## Algorithm

I wrote a recursive helper `dfs(i, run)`, where `run` is the XOR accumulated so far for whatever subset I'm currently building, and `i` is the index I'm deciding on next.

Base case: once `i` reaches the end of `nums`, that means I've finished deciding on one complete subset, so I return its accumulated XOR (`run`).

Otherwise I branch two ways: one where I include `nums[i]` (`dfs(i+1, run ^ nums[i])`) and one where I don't (`dfs(i+1, run)`), and I add the two results together.

I start it off with `dfs(0, 0)`, which ends up exploring all 2ⁿ subsets and summing each one's XOR total.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- An empty array hits the base case immediately, since `i >= len(nums)` is already true, returning 0.
- A single-element array `[a]` gives two branches: include `a` (XOR total `a`) or don't (XOR total 0), so the sum ends up being `a`.
- An all-zero array means every subset's XOR total is 0, so the whole sum is 0.
- This is honestly just brute-force O(2ⁿ), so it doesn't really show off a clever bit-manipulation trick. The neater way to do this is `(OR of all nums) << (n - 1)`, since every bit set in any number ends up set in exactly half of all subset XORs. I should have that reasoning ready, since that's probably the actual point of this problem.
