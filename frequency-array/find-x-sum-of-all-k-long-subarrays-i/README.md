# 3610. Find X-Sum of All K-Long Subarrays I

[https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/](https://leetcode.com/problems/find-x-sum-of-all-k-long-subarrays-i/)

**Language:** cpp · **Status:** Accepted

## Problem Statement

Description
         You are given an array nums of n integers and two integers k and x.

         The x-sum of an array is calculated by the following procedure:

                Count the occurrences of all elements in the array.
                Keep only the occurrences of the top x most frequent elements. If two elements have the same
                number of occurrences, the element with the bigger value is considered more frequent.
                Calculate the sum of the resulting array.

         Note that if an array has less than x distinct elements, its x-sum is the sum of the array.

         Return an integer array answer of length n - k + 1 where answer[i] is the x-sum of the subarray nums[i..i
         + k - 1].

         Example 1:

         Input: nums = [1,1,2,2,3,4,2,3], k = 6, x = 2

         Output: [6,10,12]

         Explanation:

                For subarray [1, 1, 2, 2, 3, 4], only elements 1 and 2 will be kept in the resulting array. Hence,
                answer[0] = 1 + 1 + 2 + 2.
                For subarray [1, 2, 2, 3, 4, 2], only elements 2 and 4 will be kept in the resulting array. Hence,
                answer[1] = 2 + 2 + 2 + 4. Note that 4 is kept in the array since it is bigger than 3 and 1 which occur
                the same number of times.
                For subarray [2, 2, 3, 4, 2, 3], only elements 2 and 3 are kept in the resulting array. Hence,
                answer[2] = 2 + 2 + 2 + 3 + 3.

         Example 2:

         Input: nums = [3,8,7,8,7,5], k = 2, x = 2

         Output: [11,15,15,15,12]

         Explanation:

         Since k == x, answer[i] is equal to the sum of the subarray nums[i..i + k - 1].

         Constraints:

                1 <= n == nums.length <= 50
                1 <= nums[i] <= 50
                1 <= x <= k <= nums.length

## Approach / Intuition

_(fill in)_

## Algorithm

First I find the max value in `nums` so I know how large to make my frequency array. Then I slide a window of size `k` across the array, and for every window position I reset `freq` to all zeros and rebuild it from scratch by counting what's in `nums[p .. p+k-1]`. Then I call `findsum(freq, x)` to get that window's answer.

`findsum` runs `x` times. Each time it finds whichever value has the highest frequency (ties go to the larger value, that's the `i > maxpos` check), adds `maxpos * freq[maxpos]` to a running sum, then zeroes that value's frequency out so it isn't picked again.

I return the array of all the per-window answers.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- If there are fewer than `x` distinct values left in a window, `findsum` just keeps finding `max = 0` for the remaining rounds and adds nothing further, so it doesn't break.
- Ties in frequency are deliberately broken toward the larger value, matching what the problem asks for.
- `k = nums.length` just means there's a single window.
- I rebuild the whole frequency array from scratch every window rather than sliding it incrementally, so it ends up roughly O(n·k) overall. That's fine for this easy version's constraints, but the harder follow-up version would need the incremental approach to pass within its limits, worth mentioning if it comes up.
