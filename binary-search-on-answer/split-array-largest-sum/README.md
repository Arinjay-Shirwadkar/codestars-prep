# 410. Split Array Largest Sum

[https://leetcode.com/problems/split-array-largest-sum/](https://leetcode.com/problems/split-array-largest-sum/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums and an integer k, split nums into k non-empty subarrays such that the largest
         sum of any subarray is minimized.

         Return the minimized largest sum of the split.

         A subarray is a contiguous part of the array.

         Example 1:

              Input: nums = [7,2,5,10,8], k = 2
              Output: 18
              Explanation: There are four ways to split nums into two subarrays.
              The best way is to split it into [7,2,5] and [10,8], where the largest sum among the two subarrays is on

         Example 2:

              Input: nums = [1,2,3,4,5], k = 2
              Output: 9
              Explanation: There are four ways to split nums into two subarrays.
              The best way is to split it into [1,2,3] and [4,5], where the largest sum among the two subarrays is onl

         Constraints:

                  1 <= nums.length <= 1000
                  0 <= nums[i] <= 106
                  1 <= k <= min(50, nums.length)

## Approach / Intuition

This one was pretty tricky, to be honest. To recognize that the problem had a definite search space was pretty tough, but once one sees that the minimum sum itself lies in a range, from the maximum element to the sum of all elements, one can run binary search on this set and check is, for any given `mid`, one can divide the array in less that or equal to k partitions (using a greedy approach).

## Algorithm

I binary search on the answer again, this time the largest subarray sum. `l` is the biggest single element, `u` is the sum of the whole array.

For a candidate `mid`, I greedily count how many subarrays I'd need if no subarray can exceed `mid`. I keep a running sum, and whenever adding the next element would push past `mid`, I start a new subarray (bump the count `t`, reset `sum` to just that element).

If the resulting count `t <= k`, `mid` is feasible, so I save it as `validm` and try to shrink further (`u = mid - 1`). If `t > k`, `mid` is too small (would need more than `k` subarrays), so I search up (`l = mid + 1`).

I return `validm`.

## Time Complexity

O(Nlog(M))

## Space Complexity

O(1)
## Edge Cases

- `k = 1` forces `validm` to be the sum of the whole array, since only one subarray is allowed.
- `k >= len(nums)` means each element can be its own subarray, so `validm` converges to `max(nums)`.
- A single-element array: `l` and `u` are both just `nums[0]`, regardless of `k`.
- All elements equal: the greedy split behaves predictably, which makes it a good problem to trace through by hand if I'm asked to walk through the binary search live.
