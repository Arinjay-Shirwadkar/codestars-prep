# 3676. Smallest Number With All Set Bits

[https://leetcode.com/problems/smallest-number-with-all-set-bits/](https://leetcode.com/problems/smallest-number-with-all-set-bits/)

**Language:** c · **Status:** Accepted

## Problem Statement

Description
         You are given a positive number n.

         Return the smallest number x greater than or equal to n, such that the binary representation of x
         contains only set bits

         Example 1:

         Input: n = 5

         Output: 7

         Explanation:

         The binary representation of 7 is "111".

         Example 2:

         Input: n = 10

         Output: 15

         Explanation:

         The binary representation of 15 is "1111".

         Example 3:

         Input: n = 3

         Output: 3

         Explanation:

         The binary representation of 3 is "11".

         Constraints:

                1 <= n <= 1000

## Approach / Intuition

_(fill in)_

## Algorithm

The answer is the smallest number `>= n` whose binary form is all 1s, meaning something of the form `2^c - 1`.

Starting at `c = 1`, I compute what a `c`-bit all-ones number equals by summing `2^0 + 2^1 + ... + 2^(c-1)` using `pow(2, d)`. If that total is `>= n`, I return it immediately, since it's the answer.

Otherwise I bump `c` up by one and try again.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- If `n` is already all 1s (e.g. `n = 7 = 0b111`), the loop finds `c = 3` gives exactly 7, which is `>= n`, so it returns `n` itself. The answer can be `n` when `n` already fits the pattern.
- `n = 1`: `c = 1` gives `2^0 = 1 >= 1`, returning immediately.
- I'm using `pow()`, which is floating point, to compute powers of 2. Works fine at this problem's scale, but a bit shift (`1 << d`) would've been the more natural fit for a bit-manipulation problem, worth mentioning if asked why I did it this way.
