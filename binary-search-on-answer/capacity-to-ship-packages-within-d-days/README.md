# 1056. Capacity To Ship Packages Within D Days

[https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/](https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/)

**Language:** java · **Status:** Accepted

## Problem Statement

Description
         A conveyor belt has packages that must be shipped from one port to another within days days.

         The ith package on the conveyor belt has a weight of weights[i]. Each day, we load the ship with
         packages on the conveyor belt (in the order given by weights). We may not load more weight than the
         maximum weight capacity of the ship.

         Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being
         shipped within days days.

         Example 1:

              Input: weights = [1,2,3,4,5,6,7,8,9,10], days = 5
              Output: 15
              Explanation: A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
              1st day: 1, 2, 3, 4, 5
              2nd day: 6, 7
              3rd day: 8
              4th day: 9
              5th day: 10

              Note that the cargo must be shipped in the order given, so using a ship of capacity 14 and splitting the

         Example 2:

              Input: weights = [3,2,2,4,1,4], days = 3
              Output: 6
              Explanation: A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
              1st day: 3, 2
              2nd day: 2, 4
              3rd day: 1, 4

         Example 3:

              Input: weights = [1,2,3,1,1], days = 4
              Output: 3
              Explanation:
              1st day: 1
              2nd day: 2
              3rd day: 3
              4th day: 1, 1

         Constraints:

                  1 <= days <= weights.length <= 5 * 104
                  1 <= weights[i] <= 500

## Approach / Intuition

What one realizes at first, after looking at a few examples, is that the weight capacity of the ship must fall in a very particular range. Logically, this range must be between the weight of the heaviest box and the sum of all boxes. Any lower than the weight of the heaviest and box, and it will never be able to ship it. And, if the ship can bear the weight of all boxes, it can deliver the packets in a single day.

So, this problem naturally leads to a sorted search space and target condition, for which binary search will work quite well. 

## Algorithm

Binary search on the answer again, this time the ship capacity w. l starts at the heaviest single package (cant go below that) and u starts at the sum of everything (ship it all in one day).

For a candidate mid, I simulate loading days, greedily adding weights to the current days load (runW) as long as they fit, and once the next package would overflow I start a new day with it as the first item. Count how many days (d) that takes.

If d > days, mid is too small, search up (l = mid+1). If d <= days, mid works, save it as validw and try smaller (u = mid-1).

Return validw once done.

## Time Complexity

The time complexity is O(nlog(n)) 

## Space Complexity

O(1)

## Edge Cases

array of length 1, l and u are both just that one weight, converges right away
days exactly equal to weights.length forces the capacity to be at least the biggest single weight since basically every day carries exactly one package in that tightest case
days = 1 forces validw to be the sum of everything
the day counting bumps d one extra time right at the last index to close out the final day properly even if it wasnt overflowed into.