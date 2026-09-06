# 698. Partition to K Equal Sum Subsets

[https://leetcode.com/problems/partition-to-k-equal-sum-subsets/](https://leetcode.com/problems/partition-to-k-equal-sum-subsets/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         Given an integer array nums and an integer k, return true if it is possible to divide this array into k non-
         empty subsets whose sums are all equal.

         Example 1:

              Input: nums = [4,3,2,3,5,2,1], k = 4
              Output: true
              Explanation: It is possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

         Example 2:

              Input: nums = [1,2,3,4], k = 3
              Output: false

         Constraints:

                  1 <= k <= nums.length <= 16
                  1 <= nums[i] <= 104
                  The frequency of each element is in the range [1, 4].

## Approach / Intuition

_(fill in)_

## Algorithm

If the total sum doesn't divide evenly by `k`, I return False right away, since no partition can work.

I sort `nums` in descending order first, which helps fail bad branches faster, since larger numbers are the most constrained to place. `maxsum = total / k` is the target each of the `k` buckets needs to reach.

`dfs(i, size)` tries to put `nums[i]` into one of the `k` buckets. Base case: if `size == len(nums)`, everything's been placed, so I return True. For each bucket `j`, if adding `nums[i]` wouldn't exceed `maxsum`, I place it there and recurse to the next number (`dfs(i+1, size+1)`), returning True right away if that succeeds. If it doesn't, I undo the placement and try the next bucket.

One optimization: if a bucket is still empty after failing to place the current number there, I stop trying other buckets for this number entirely, since placing it in any other empty bucket would just be the same situation repeated.

I start with `dfs(0, 0)` and return the result.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- A total not divisible by `k` gets caught immediately, with no recursion needed.
- A single number larger than `maxsum` means every bucket fails for it, so `dfs` exhausts all branches and correctly returns False.
- `k = 1` technically works out to True (the whole array is the one bucket), but it still goes through the full recursion instead of being special-cased, which is worth mentioning if asked.
- Sorting descending as a pruning move is worth explaining: larger numbers have the fewest buckets that can actually fit them, so bad branches get cut off early instead of surfacing deep in the recursion.
