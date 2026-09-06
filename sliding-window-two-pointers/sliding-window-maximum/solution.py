import heapq

              class Solution:
                  def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
                      #heap + hashmap
                      heap=[]
                      consider={} #basically a frequency counter
                      #holds elements under consideration. Much easier than actually removing values from the heap. It

                      #building the initial heap for the window
                      for i in range(0,k-1):
                          if nums[i] in consider:
                              consider[nums[i]]+=1
                          else:
                              heapq.heappush(heap,-nums[i])
                              consider[nums[i]]=1

                      p1=0
                      sol=[]
                      for p2 in range(k-1,len(nums)):
                           #add p2
                           if nums[p2] in consider:
                               consider[nums[p2]]+=1
                           else:
                               heapq.heappush(heap,-nums[p2])
                               consider[nums[p2]]=1

                          greatest=-heap[0]
                          while greatest not in consider:
                              heapq.heappop(heap)
                              greatest=-heap[0]

                          sol.append(greatest)

                          #now remove p1
                          if consider[nums[p1]]>1:
                              consider[nums[p1]]-=1
                          else:
                              consider.pop(nums[p1])

                          p1+=1

                      return sol
