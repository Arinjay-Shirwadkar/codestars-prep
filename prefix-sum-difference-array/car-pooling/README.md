# 1184. Car Pooling

[https://leetcode.com/problems/car-pooling/](https://leetcode.com/problems/car-pooling/)

**Language:** python3 · **Status:** Accepted

## Problem Statement

Description
         There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive
         west).

         You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi]
         indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them
         off are fromi and toi respectively. The locations are given as the number of kilometers due east from the
         car's initial location.

         Passengers are dropped off before new passengers are picked up at the same location. At every point
         along the route, the total number of passengers in the car must not exceed capacity.

         Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

         Example 1:

              Input: trips = [[2,1,5],[3,3,7]], capacity = 4
              Output: false
              Explanation:
              At kilometer 1, 2 passengers are picked up, so the car holds 2.
              At kilometer 3, 3 more are picked up, so the car holds 5.
              Since 5 > capacity = 4, the trips cannot all be completed.

         Example 2:

              Input: trips = [[2,1,5],[3,3,7]], capacity = 5
              Output: true
              Explanation:
              At kilometer 1, the car holds 2 passengers.
              At kilometer 3, the car holds 5 passengers.
              At kilometer 5, the first 2 are dropped off, so the car holds 3.
              At kilometer 7, the last 3 are dropped off, so the car holds 0.
              The maximum occupancy is 5, which never exceeds capacity = 5.

         Constraints:

                  1 <= trips.length <= 1000
                  trips[i].length == 3
                  1 <= numPassengersi <= 100
                  0 <= fromi < toi <= 1000
                  1 <= capacity <= 105

## Approach / Intuition

_(fill in)_

## Algorithm

Instead of a difference array, I ended up using a sorted approach with a min-heap for this one. I sort all the trips by their end location first.

Then I keep a min-heap of currently active trips, keyed by drop-off point, and a running `currentcap` that starts at full `capacity`. Going through trips in order of increasing end point: first I pop and process anyone in the heap whose drop-off is `<= this trip's start`, since those passengers have already left, and I add their seats back to `currentcap`. Then I check if `currentcap` can fit the new trip. If not, I return False right away. Otherwise I subtract the passengers and push this trip onto the heap, keyed by its own end point.

If I get through every trip without a capacity violation, I return True.

## Time Complexity

_(fill in)_

## Space Complexity

_(fill in)_

## Edge Cases

- Two trips sharing the same start or end still work fine, as long as the `drop off <= start` comparison holds. I use `<=` rather than `<`, so a passenger dropped off exactly where the next pickup happens still frees the seat in time.
- A trip starting exactly where another ends is handled correctly for the same reason.
- Capacity exactly matching the max simultaneous passengers should still return True, since the check only fails on strict overflow.
- An empty `trips` list just returns True immediately, since the loop body never runs.
- Worth flagging: the topic here is difference array, but what I actually wrote uses a sort-plus-heap simulation instead. I should have the classic difference-array version ready too (`diff[start] += passengers`, `diff[end] -= passengers`, then scan for any point exceeding capacity), in case that's specifically what's being asked about.
