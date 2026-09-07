# 238. Product of Array Except Self

[https://leetcode.com/problems/product-of-array-except-self/](https://leetcode.com/problems/product-of-array-except-self/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the
         elements of nums except nums[i].

         The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

         You must write an algorithm that runs in O(n) time and without using the division operation.

         Example 1:

              Input: nums = [1,2,3,4]
              Output: [24,12,8,6]

         Example 2:

              Input: nums = [-1,1,0,-3,3]
              Output: [0,0,9,0,0]

         Constraints:

                  2 <= nums.length <= 105
                  -30 <= nums[i] <= 30
                  The input is generated such that answer[i] is guaranteed to fit in a 32-bit integer.

         Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count
         as extra space for space complexity analysis.)

## Approach / Intuition

Instead of accessing each element in the array per element, which would lead to O(n2) time complexity, we can simply sweep the array twice, maintinaing a prefix and suffix array, and multiplying the rest of the elements into prefix and suffix. Even better actually would be maintaining a single array instead of two different prefix and suffix arrays.

## Algorithm

I build a `prefix` array where `prefix[i]` is the product of everything to the left of `i` (starting at 1, accumulated left to right). Then a `suffix` array built the same way, but from the right.

The answer at each index is just `prefix[i] * suffix[i]`, since that's everything except `nums[i]` itself.

## Time Complexity

O(n)

## Space Complexity

O(n)

## Edge Cases

- One zero in the array: that index correctly gets the product of everything else (which is nonzero), while every other index becomes 0, since either its prefix or suffix product will include that zero.
- Two or more zeros: every result becomes 0.
- Negative numbers are fine, since the sign just works itself out through normal multiplication.
- An array of length 1: `prefix[0]` and `suffix[0]` both stay at their initial value of 1, so the result is 1.
