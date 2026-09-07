# 42. Trapping Rain Water

[https://leetcode.com/problems/trapping-rain-water/](https://leetcode.com/problems/trapping-rain-water/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given n non-negative integers representing an elevation map where the width of each bar is 1, compute
         how much water it can trap after raining.

         Example 1:

              Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
              Output: 6
              Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].

         Example 2:

              Input: height = [4,2,0,3,2,5]
              Output: 9

         Constraints:

                  n == height.length
                  1 <= n <= 2 * 104
                  0 <= height[i] <= 105

## Approach / Intuition

_(fill in)_

## Algorithm

My approach splits the array into what I'm calling the main region and the end region, and handles them with two separate passes instead of the usual two-pointer-with-running-max method.

Main region, left to right: I scan until I find the first nonzero height, which becomes my left wall (`lim`, at index `limi`). As I keep scanning right, I subtract each shorter bar's height from a running deficit called `maybe`, until I hit a bar `>= lim`. That bar becomes the new right wall, so I add `maybe + (gap width) * lim` to `water`, then treat this right wall as my new left wall and continue (I actually step `i` back by one so the same index gets reprocessed as a left wall).

If the last wall I find reaches the end of the array, I set `finish = 1`, meaning there's no leftover unbound region.

End region, right to left: if `finish` is still 0, there's a chunk past the last confirmed right wall where water couldn't be bound looking left to right, but small dips between bumps there can still hold water when viewed from the right side. So I redo the same wall-finding logic in reverse, starting from the end and working back to `revlimi` (the last left wall found in the main pass).

I add up water from both passes and return the total.

## Time Complexity

O(n) as there are only two sweeps over the input array

## Space Complexity

O(1)

## Edge Cases

- An all-zero array, or a strictly increasing/decreasing one, means no water gets trapped: `l` never becomes 1, or the main loop just never finds a right wall `>= lim`.
- A single-peak array is handled fully by the main pass alone.
- Very short arrays (length 0, 1, or 2) can't trap anything, since the loop bounds naturally prevent any wall from forming.
- Water trapped only near the very end of the array is exactly why the end-region reverse pass is needed. One forward pass alone would miss it, which is worth explaining if I'm asked why I split it into two passes.
