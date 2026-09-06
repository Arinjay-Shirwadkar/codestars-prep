class Solution:
                  def splitArray(self, nums: List[int], k: int) -> int:
                      max=0
                      sum=0
                      for i in nums:
                          max = i if i>max else max
                          sum+=i
                      #the minimum subarray sum lies within these 2 paramters, k=1 and k=len
                      l,u=max,sum

                      while l<=u:
                          mid=l+(u-l)//2
                          #check if this value of the minimum subarray sum is valid
                          t=1
                          sum=0
                          for i in nums:
                              if sum+i<=mid:
                                  sum+=i
                              else:
                                  sum=i
                                  t+=1
                          if t<=k:
                              validm=mid
                              #can we do better though
                              u=mid-1
                          else:
                              l=mid+1

                      return validm
