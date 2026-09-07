# 907. Koko Eating Bananas

[https://leetcode.com/problems/koko-eating-bananas/](https://leetcode.com/problems/koko-eating-bananas/)

**Language:** python  · **Status:** Accepted

## Problem Statement

Description
         Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards
         have gone and will come back in h hours.

         Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas
         and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will
         not eat any more bananas during this hour.

         Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

         Return the minimum integer k such that she can eat all the bananas within h hours.

         Example 1:

              Input: piles = [3,6,7,11], h = 8
              Output: 4

         Example 2:

              Input: piles = [30,11,23,4,20], h = 5
              Output: 30

         Example 3:

              Input: piles = [30,11,23,4,20], h = 6
              Output: 23

         Constraints:

                  1 <= piles.length <= 104
                  piles.length <= h <= 109
                  1 <= piles[i] <= 109

## Approach / Intuition

The key insight is to recognize that the answer lies in a bounded search space - 1 to the maximum number of bananas in the piles. From here, it is not difficult to use binary search.

## Algorithm

I find the largest pile, which becomes my upper bound `u` for possible eating speeds, since eating faster than the biggest pile is pointless. Lower bound `l = 1`.

I binary search on the answer (the eating speed `hours`) rather than the array itself. For a candidate `mid`, I work out how many hours it would take at that speed, summing `pile +mid-1//mid` across all piles.

If that total exceeds `h`, `mid` is too slow, so I search the upper half (`l = mid + 1`). If it's `<= h`, `mid` works, so I save it as `optimal` and try to go lower (`u = mid - 1`).

Once `l > u`, I return `optimal`.

## Time Complexity

O(nlog(M))

## Space Complexity

O(1)

## Edge Cases

- `h` exactly equal to the number of piles forces the maximum possible speed, since Koko can only touch one pile per hour.
- A single pile: `l` and `u` converge fast, and the answer is just `ceil(pile / h)`.
- `h` much larger than needed: the smallest speed `k = 1` already satisfies the constraint, and the search correctly lands there.
- The `Math.ceil` on a cast-to-double division matters a lot here. Forgetting to round up is the classic bug in this exact problem.
