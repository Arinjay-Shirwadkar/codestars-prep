# 1236. N-th Tribonacci Number

[https://leetcode.com/problems/n-th-tribonacci-number/](https://leetcode.com/problems/n-th-tribonacci-number/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         The Tribonacci sequence Tn is defined as follows:

         T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

         Given n, return the value of Tn.

         Example 1:

              Input: n = 4
              Output: 4
              Explanation:
              T_3 = 0 + 1 + 1 = 2
              T_4 = 1 + 1 + 2 = 4

         Example 2:

              Input: n = 25
              Output: 1389537

         Constraints:

                  0 <= n <= 37
                  The answer is guaranteed to fit within a 32-bit integer, ie. answer <= 2^31 - 1.

## Approach / Intuition

_(fill in)_

## Algorithm

I handle `T(0) = 0` and `T(1) = T(2) = 1` directly as base cases first.

For `n >= 3`, I loop from 3 up to `n`, keeping only the last three values (`a`, `b`, `c`) instead of a full DP array. This is basically the space-optimized version of the recurrence `T(i) = T(i-1) + T(i-2) + T(i-3)`. Each step I compute `d = a + b + c`, then shift everything forward: `a = b`, `b = c`, `c = d`.

I return `d` at the end.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- `n = 0` returns immediately through the base case, so the loop never runs.
- `n = 1` or `n = 2` are also handled directly by the base case.
- `n = 3`: the loop runs exactly once and correctly gives `T(3) = 1 + 1 + 0 = 2`.
- For larger `n` near the constraint limit, the values grow fairly fast, so I'd want to double-check that `int` doesn't overflow if the constraints were ever pushed higher.
