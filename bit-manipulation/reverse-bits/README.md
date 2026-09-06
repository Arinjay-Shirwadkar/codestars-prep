# 190. Reverse Bits

[https://leetcode.com/problems/reverse-bits/](https://leetcode.com/problems/reverse-bits/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Reverse bits of a given 32 bits signed integer.

         Example 1:

         Input: n = 43261596

         Output: 964176192

         Explanation:

           Integer               Binary
         43261596 00000010100101000001111010011100
         964176192 00111001011110000010100101000000

         Example 2:

         Input: n = 2147483644

         Output: 1073741822

         Explanation:

           Integer               Binary
         2147483644 01111111111111111111111111111100
         1073741822 00111111111111111111111111111110

         Constraints:

                0 <= n <= 231 - 2
                n is even.

         Follow up: If this function is called many times, how would you optimize it?

## Approach / Intuition

_(fill in)_

## Algorithm

I start with a result `m = 0` and loop 32 times, since it's a 32-bit integer. Each round: shift `m` left by 1 to make room for the next bit, grab the current lowest bit of `n` with `n & 1` and add it into `m`, then shift `n` right by 1 to move to its next bit.

After 32 rounds, `m` holds `n`'s bits reversed, and I return it.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- `n = 0` means every extracted bit is 0, so the result stays 0.
- `n` with all 32 bits set stays unchanged, since all 1s reversed is still all 1s.
- Shifting into the sign bit is fine in Java, since it's operating on the raw bit pattern with two's complement, so no special-casing is needed.
- Leading zeros in `n` turn into trailing zeros in the output and vice versa. Easy to describe incorrectly out loud, so worth practicing the explanation.
