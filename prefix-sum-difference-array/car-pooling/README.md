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

I first solved this problem using a min-heap. I was able to remove the passengers who were to leave by doing this. However, this difference array and prefix sum approach is much superior as it runs faster. Since, at every position, passengers can either get on or get off, we can compute the net change in passengers at every position by simply subtracting those that get off and adding those that get on. Now we simply check each position to see if the number of passengers ever exceed capacity.

## Algorithm

Initialize an array or hash map spanning all potential stop locations to track net passenger changes, setting every location to zero. For each trip in the list, record passenger changes by adding the number of passengers to the start location and subtracting that exact amount from the end location. Next, iterate sequentially through every stop along the timeline while maintaining a running tally of onboard passengers. At each stop, add the location's net change to the running total and check if it exceeds the vehicle's maximum capacity. If the passenger count ever goes over capacity, immediately return false; otherwise, if you process all stops without exceeding the limit, return true.

## Time Complexity

O(N)

## Space Complexity

O(1)

## Edge Cases

Same location drop-offs and pick-ups: When one group gets off at the exact same stop where another group gets on, net passenger changes at that location consolidate correctly into a single net value, ensuring passengers step off before new ones step on.

Zero vehicle capacity: If capacity is set to zero and any trip contains one or more passengers, the running count immediately breaches the limit at the very first pickup point.

Capacity equal to total passengers on disjoint trips: Trips that do not overlap in time can safely reuse the full vehicle capacity across different legs of the journey without triggering a false positive.

Multiple trips starting at the exact same stop: Several trips boarding at the same location sum together in the difference array before the capacity check occurs, catching over-capacity scenarios at that specific stop right away.
