# 303. Range Sum Query - Immutable

[https://leetcode.com/problems/range-sum-query-immutable/](https://leetcode.com/problems/range-sum-query-immutable/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums, handle multiple queries of the following type:

               1. Calculate the sum of the elements of nums between indices left and right inclusive where left <=
                  right.

         Implement the NumArray class:

                  NumArray(int[] nums) Initializes the object with the integer array nums.
                  int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and
                  right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).

         Example 1:

              Input
              ["NumArray", "sumRange", "sumRange", "sumRange"]
              [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
              Output
              [null, 1, -1, -3]

              Explanation
              NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
              numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
              numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
              numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3

         Constraints:

                  1 <= nums.length <= 104
                  -105 <= nums[i] <= 105
                  0 <= left <= right < nums.length
                  At most 104 calls will be made to sumRange.

## Approach / Intuition

A fairly straightforward prefix sum question. Given the array, we precompute the prefix array so future range queries will run in constant time.

## Algorithm

In the constructor, I build a running prefix sum array `pre`, where `pre[i]` is the sum of everything from index 0 to `i`.

For `sumRange(left, right)`, just computing `pre[right] - pre[left]` would exclude `nums[left]` itself, since `pre[left]` already includes it, so I add `num[left]` back in to correct for that: `pre[right] - pre[left] + num[left]`.

Each query after the initial setup runs in O(1).

## Time Complexity

O(n)

## Space Complexity

O(n)

## Edge Cases

- `left == right` correctly reduces down to just `num[left]`.
- `left == 0` still works, since `pre[0]` is just `num[0]` to begin with.
- Negative numbers don't cause any issues, since it's just addition with no assumption of positivity.
- Repeated queries stay O(1) each, regardless of how large the range is, which is really the whole point of precomputing the prefix sums.
