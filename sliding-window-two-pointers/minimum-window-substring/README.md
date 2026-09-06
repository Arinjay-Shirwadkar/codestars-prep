# 76. Minimum Window Substring

[https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         Given two strings s and t of lengths m and n respectively, return the minimum window substring of s
         such that every character in t (including duplicates) is included in the window. If there is no such
         substring, return the empty string "".

         The testcases will be generated such that the answer is unique.

         Example 1:

              Input: s = "ADOBECODEBANC", t = "ABC"
              Output: "BANC"
              Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

         Example 2:

              Input: s = "a", t = "a"
              Output: "a"
              Explanation: The entire string s is the minimum window.

         Example 3:

              Input: s = "a", t = "aa"
              Output: ""
              Explanation: Both 'a's from t must be included in the window.
              Since the largest window of s only has one 'a', return empty string.

         Constraints:

                  m == s.length
                  n == t.length
                  1 <= m, n <= 105
                  s and t consist of uppercase and lowercase English letters.

         Follow up: Could you find an algorithm that runs in O(m + n) time?

## Approach / Intuition

_(fill in)_

## Algorithm

First I build a frequency map `com` of every character in `t`. Then a second map `win`, initialized to 0 for each character that appears in `t`, which tracks how many of those characters are currently sitting inside my window.

Before the main loop starts, I pre-fill `win` using the first `t.length() - 1` characters of `s` (I leave out the very last one on purpose, it gets picked up in the main loop instead).

`p1` is my left pointer and `p2` is the right one, starting at `t.length() - 1`. I use a flag `movep2` to know whether I still need to add `s[p2]` into `win` this round.

While `p2` is within bounds: if `movep2` is set, I add `s[p2]` to `win`. Then I check if the window is currently valid, looping over every key in `com` and checking if `win` has at least that many of each character. If it's valid, I've found a candidate window, so I compare it to my current best and update `min`/`minS` if it's smaller, then shrink from the left (remove `s[p1]` from `win`, `p1++`). If it's not valid, I expand right instead (`p2++`, `movep2 = 1` so it gets counted next round).

At the end, `minS` is the answer, or an empty string if nothing worked.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- If `t` is longer than `s`, no window can possibly fit, so I check this at the very top and return an empty string right away.
- `t` can have repeated characters (e.g. `t = "aab"`), which works fine since `com` stores counts, not just presence.
- If no valid window exists, `minS` just stays empty, which gets returned.
- If `s` and `t` are the same string, the whole string is the only valid window.
- Characters in `s` that never appear in `t` get ignored automatically, since `win` only tracks keys that exist in `com`.
