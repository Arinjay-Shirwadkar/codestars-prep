# 239. Sliding Window Maximum

[https://leetcode.com/problems/sliding-window-maximum/](https://leetcode.com/problems/sliding-window-maximum/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         You are given an array of integers nums, there is a sliding window of size k which is moving from the very
         left of the array to the very right. You can only see the k numbers in the window. Each time the sliding
         window moves right by one position.

         Return the max sliding window.

         Example 1:

              Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
              Output: [3,3,5,5,6,7]
              Explanation:
              Window position                Max
              ---------------               -----
              [1 3 -1] -3 5 3 6 7             3
               1 [3 -1 -3] 5 3 6 7            3
               1 3 [-1 -3 5] 3 6 7            5
               1 3 -1 [-3 5 3] 6 7            5
               1 3 -1 -3 [5 3 6] 7            6
               1 3 -1 -3 5 [3 6 7]            7

         Example 2:

              Input: nums = [1], k = 1
              Output: [1]

         Constraints:

                  1 <= nums.length <= 105
                  -104 <= nums[i] <= 104
                  1 <= k <= nums.length

## Approach / Intuition

_(fill in)_

## Algorithm

_(fill in)_

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

_(fill in)_
