# 448. Find All Numbers Disappeared in an Array

[https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/](https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/)

**Language:** python · **Status:** Accepted

## Problem Statement

Description
         Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in
         the range [1, n] that do not appear in nums.

         Example 1:

              Input: nums = [4,3,2,7,8,2,3,1]
              Output: [5,6]

         Example 2:

              Input: nums = [1,1]
              Output: [2]

         Constraints:

                  n == nums.length
                  1 <= n <= 105
                  1 <= nums[i] <= n

         Follow up: Could you do it without extra space and in O(n) runtime? You may assume the returned list
         does not count as extra space.

## Approach / Intuition

_(fill in)_

## Algorithm

The trick here is using the array itself as a hash table. For every number, I go to its "home index" (`abs(num) - 1`) and negate whatever's sitting there, as long as it isn't already negative. That negation is what marks a number as seen.

I use `abs(num)` when computing the index, because by the time I get to some numbers, earlier steps may have already flipped their sign.

After that pass, I scan the array again. Any index that's still positive means that number (`index + 1`) was never marked, so it's missing. I collect all of those and return them.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- A number showing up more than twice is handled fine, since the `if nums[index] > 0` check stops me from double-negating something already negative.
- If every number from 1 to n appears exactly once, everything gets negated and I return an empty list.
- If the same number repeats across the whole array (like `[1,1,1]`), only index 0 ever gets touched, so indices 1 and 2 correctly show up as missing (2 and 3).
- This runs in O(1) extra space, which is really the whole point. I should be ready to explain how encoding "visited" as a sign flip directly in the input array works, since it doesn't look like a frequency array at first glance.
