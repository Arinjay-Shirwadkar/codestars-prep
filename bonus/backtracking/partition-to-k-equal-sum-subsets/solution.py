class Solution:
                  def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
                      #k buckets strategy
                      numsSum = sum(nums)
                      if numsSum%k!=0:
                          return False

                     nums.sort(reverse=True)
                     maxsum = numsSum//k
                     buckets = []
                     for i in range(0,k):
                         buckets.append([0])

                     bucketsums = [0]*k

                      def dfs(i,size):
                          if size==len(nums):
                              return True

                          for j in range(0,k):
                              if bucketsums[j]+nums[i]<=maxsum:
                                  flag=1
                                  bucketsums[j]=bucketsums[j]+nums[i]
                                  buckets[j].append(nums[i])
                                  check = dfs(i+1,size+1)
                                  if check:
                                      return True
                                  buckets[j].pop()
                                  bucketsums[j]-=nums[i]
                              if bucketsums[j]==0:
                                  break
                          return False

                      return dfs(0,0)
