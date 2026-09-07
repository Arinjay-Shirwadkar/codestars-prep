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

#Alternate solution

class Deque:
     
    def __init__(self):
        self.deque = []
        self.front=-1
        self.rear=-1
        
    def isEmpty(self):
        return self.front==-1

    def enqueueR(self,val):
        if self.isEmpty():
            self.front+=1
        self.rear+=1
        self.deque.append(val)

    def dequeueR(self):
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
            self.deque =[]
            return
        self.rear-=1
        self.deque.pop()
        
         

    def dequeueF(self):
        if self.front==self.rear:
            self.front=-1
            self.rear=-1
            self.deque=[]
            return
        self.front+=1
        
    def get_rear(self):
        return self.deque[self.rear]
    def get_front(self):
        return self.deque[self.front]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = Deque()
        p1=-1
        p2=0
        sol=[]
        for p2 in range(0,k-1):
            while not d.isEmpty() and nums[d.get_rear()]<nums[p2]:
                d.dequeueR()
            d.enqueueR(p2)
        
        p2=k-1
        while p2<len(nums):
            #add the p2th index
            while not d.isEmpty() and nums[d.get_rear()]<nums[p2]:
                d.dequeueR()
            d.enqueueR(p2)

            #expire the old p1
            p1+=1
            while not d.isEmpty() and d.get_front()<p1:
                d.dequeueF()
            
            sol.append(nums[d.get_front()])

            p2+=1

        return sol
        
            