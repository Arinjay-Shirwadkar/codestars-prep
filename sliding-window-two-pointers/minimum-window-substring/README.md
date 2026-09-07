# 76. Minimum Window Substring

[https://leetcode.com/problems/minimum-window-substring/](https://leetcode.com/problems/minimum-window-substring/)

**Language:** python · **Status:** Accepted

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

This can be recognized as a dynamic sliding window problem by analyzing what we actually want - the subarray with the minimum length which has all the characters from another string (simply translated to a hashmap). Instead of processing all subarrays, we can maintain a dyanmic sliding window. It grows continually, and shrinks whenever all characters from the string t are found in the subarray, in order to find the minimum.

## Algorithm

Algorithm

First, count the frequency of each character in target string `t` using a hash map, and track the total number of distinct characters required. Initialize two pointers, `p1` and `p2`, at the start of string s to define a flexible sliding window. Keep a second hash map for characters inside the current window, along with a match counter that tracks how many distinct characters have met their target frequency requirement.

Iterate through s by expanding `p2` one character at a time. If the current character exists in t, update its count in the window hash map. Whenever a character's window count reaches its required count in t, increment the match counter by one.

When the match counter equals the number of distinct characters in t, the window is valid. At this point, compare the current window length against the shortest valid window recorded so far, updating the best start and end indices if it is smaller. Then, shrink the window from the left by advancing p1. Before moving p1, decrement the window count of the character at p1; if its count falls below what t requires, decrement the match counter. Repeat this contraction process as long as the window remains valid. Once it becomes invalid, continue expanding p2.

After p2 reaches the end of s, slice and return the substring defined by the best recorded start and end indices. If no valid window was ever formed, return an empty string.

## Time Complexity

O(N+M)

## Space Complexity

O(1) (as we will only need to consider the lower + upper case english alphabets)

## Edge Cases

- s is shorter than t: The right pointer iterates through s without ever reaching the required distinct match count, cleanly returning an empty string.

- No valid window exists: If s is missing required characters, bestp1 stays initialized to -1, which results in an empty substring return.

- s and t are identical: The right pointer expands to the full length of s, satisfies all requirements, records the full string as the best bounds, and returns s.

- Duplicates in t: Because the algorithm checks exact frequency matches rather than simple character presence, words with duplicate characters (like "AABC") require s to contain at least two 'A's before considering that character satisfied.

- Single-character strings: If both s and t are single matching characters, the window immediately validates at length 1, records the bounds, and returns that single character.