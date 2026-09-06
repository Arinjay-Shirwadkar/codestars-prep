import heapq

              class Solution:
                  def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
                      heap=[]
                      dist=0
                      currentcap=capacity
                      trips.sort(key=lambda x: x[1])
                      for trip in trips:
                          dist=trip[1]
                          #now make sure that everyone who should've dropped off before now drops off
                          while heap and heap[0][0]<=dist:
                              drop=heapq.heappop(heap)
                              currentcap+=drop[1]

                             if trip[0]>currentcap:
                                 return False
                             else:
                                 currentcap-=trip[0]
                                 heapq.heappush(heap,[trip[2],trip[0]])

                      return True
