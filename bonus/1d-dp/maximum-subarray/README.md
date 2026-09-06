# 53. Maximum Subarray

[https://leetcode.com/problems/maximum-subarray/](https://leetcode.com/problems/maximum-subarray/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums, find the subarray with the largest sum, and return its sum.

         Example 1:

              Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
              Output: 6
              Explanation: The subarray [4,-1,2,1] has the largest sum 6.

         Example 2:

              Input: nums = [1]
              Output: 1
              Explanation: The subarray [1] has the largest sum 1.

         Example 3:

              Input: nums = [5,4,-1,7,8]
              Output: 23
              Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

         Constraints:

                  1 <= nums.length <= 105
                  -104 <= nums[i] <= 104

         Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and
         conquer approach, which is more subtle.

## Approach / Intuition

_(fill in)_

## Algorithm

I set `max` to `nums[0]` to start (this matters for all-negative arrays) and `sum` to 0. I go through the array adding each element into `sum`, and after each addition I check whether `sum` is now bigger than `max`, updating `max` if so.

The main idea: if `sum` ever goes negative, I reset it back to 0, since a negative running sum can only drag down any future subarray, so it's better to just start fresh from the next element. This is the core Kadane's algorithm insight.

I return `max`.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- An all-negative array still works, since `max` starts at `nums[0]`. Even though `sum` keeps getting reset to 0, the true answer (the least negative single element) still gets caught by the `max` comparison before each reset.
- A single-element array: both `max` and `sum` correctly resolve to that one value.
- When the best subarray starts somewhere after a negative prefix, that's exactly what the `sum < 0` reset handles, and I should be ready to explain why discarding a negative running sum is always safe.
