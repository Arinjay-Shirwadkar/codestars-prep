# 51. N-Queens

[https://leetcode.com/problems/n-queens/](https://leetcode.com/problems/n-queens/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens
         attack each other.

         Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any
         order.

         Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both
         indicate a queen and an empty space, respectively.

         Example 1:

              Input: n = 4
              Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
              Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

         Example 2:

              Input: n = 1
              Output: [["Q"]]

         Constraints:

                  1 <= n <= 9

## Approach / Intuition

Basically, I thought about how I could place a queen at a particular position and remember it was there in deeper levels of recursion. To do this, I utilize a placed list which records row and col of the placed queen. Later, I pop the queen from here and continue on.

## Algorithm

I keep the board as a 2D character grid, a `cols` set for which columns already have a queen, and a `placed` list of `(row, col)` for queens placed so far.

`dfs(i, j)` tries placing a queen at row `i`, column `j`. Base case: if `placed` has `n` queens in it, that's a full solution, so I snapshot the board into `sol`. To check validity, I skip if column `j` is taken, or if any placed queen shares a diagonal with `(i, j)`, checked with `abs(i-x) == abs(j-y)` against every placed queen (no separate row check is needed, since the recursion only ever tries one queen per row).

If it's valid, I place the queen (mark `cols`, add to `placed`, set the board cell), then recurse into the next row starting at column 0 (`dfs(i+1, 0)`), and once that call returns, I undo all three of those changes (backtrack).

Then, regardless of whether this cell worked, I also try the next column in the same row (`dfs(i, j+1)`), which is what actually walks through every column option per row.

I kick it off with `dfs(0, 0)` and return `sol`.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- `n = 1` trivially works: a single queen on a 1x1 board.
- `n = 2` or `n = 3` has no valid placement at all, so `sol` stays empty, since every branch gets eliminated by the column and diagonal checks before `placed` ever reaches size `n`.
- Queens sharing a diagonal that isn't directly adjacent are still caught correctly, since `abs(i-x) == abs(j-y)` works at any distance, not just neighboring cells.
- Backtracking correctness is the part I'd want to explain carefully: popping `cols`, popping `placed`, and resetting the board cell all have to happen together after `dfs(i+1, 0)` returns, no matter the outcome, otherwise leftover state leaks into the `dfs(i, j+1)` branch.
