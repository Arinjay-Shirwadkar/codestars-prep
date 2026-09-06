class Solution {
                  public int maxSubArray(int[] nums) {
                      //the not contributing logic is truly brilliant
                      int i=0,max=nums[0],sum=0;
                      for(i=0;i<nums.length;i++){
                      sum = sum + nums[i];
                      if(sum>max)max=sum;
                      if(sum<0)sum=0;
                      }
                      return max;
                  }
              }
