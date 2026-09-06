class Solution:
                  def subsetXORSum(self, nums: List[int]) -> int:
                      def dfs(i,run):
                          if i>=len(nums):
                              return run

                          return dfs(i+1,run^nums[i])+dfs(i+1,run)

                      return dfs(0,0)
