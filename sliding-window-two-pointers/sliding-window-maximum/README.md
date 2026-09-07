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

The main approach is to keep a track of the maximum element per window. One can do this either using a heap or a deque. Then, it becomes a simple sliding window problem.

## Algorithm

I use a max-heap (Python's heapq is min-heap, so I push negative values) plus a dict called `consider` that counts how many of each value are currently alive in the window. Instead of physically removing something from the heap once it leaves the window, I just decrement its count in `consider` and clean it up lazily later.

I seed the heap and `consider` with the first `k - 1` elements. Then I slide `p2` from `k - 1` to the end. Each step: push `nums[p2]` into the heap if it's new, and increment its count. Then I look at the top of the heap, and if that value has a count of 0 in `consider` (meaning it already left the window), I pop it, repeating until the top is actually still valid. Whatever's left on top is the max for this window, which I append to the answer. Then I remove `nums[p1]` from the window (decrement its count, or delete the key if it hits 0) and move `p1` forward.

Return the collected maxima at the end.

## Time Complexity

O(N log N) or O(N)
## Space Complexity

O(K)

## Edge Cases

- Duplicate values in the same window are fine, since I'm counting occurrences rather than just tracking presence.
- `k = 1` means every element is its own window, and this still works since `p1` and `p2` effectively move together.
- `k = len(nums)` just means there's one window covering the whole array.
- Sometimes a stale max sits at the top of the heap for several iterations before it gets popped. The while loop handles this by popping as many as needed each time, so it stays correct even if cleanup lags a bit.

