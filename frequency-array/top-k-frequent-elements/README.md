# 347. Top K Frequent Elements

[https://leetcode.com/problems/top-k-frequent-elements/](https://leetcode.com/problems/top-k-frequent-elements/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums and an integer k, return the k most frequent elements. You may return the
         answer in any order.

         Example 1:

         Input: nums = [1,1,1,2,2,3], k = 2

         Output: [1,2]

         Example 2:

         Input: nums = [1], k = 1

         Output: [1]

         Example 3:

         Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2

         Output: [1,2]

         Constraints:

                1 <= nums.length <= 105
                -104 <= nums[i] <= 104
                k is in the range [1, the number of unique elements in the array].
                It is guaranteed that the answer is unique.

         Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

## Approach / Intuition

_(fill in)_

## Algorithm

I build a frequency hashmap of every number in `nums`, then copy the entries into a 2D array `arr` where `arr[i] = [value, frequency]`. I sort that array in descending order of frequency using bubble sort, a nested loop swapping adjacent pairs when they're out of order. Not the most efficient way, but it gets the job done.

I take the first `k` entries' values as the result.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- If a bunch of elements tie on frequency, my bubble sort is stable here (only swapping on strict `<`), so the tie-break order depends on whatever order the hashmap iterated in, which isn't technically guaranteed. The problem says the answer is unambiguous either way, so it's fine in practice.
- `k` equal to the total number of distinct elements just returns the whole sorted array.
- All elements identical means a single entry in the frequency map, which trivially works regardless of `k`.
- Worth mentioning this is O(n²) because of the bubble sort, not the optimal O(n log n) heap-based approach or O(n) bucket sort. I should be ready to explain the more efficient version if asked, since efficiency is explicitly part of what's being evaluated here.
