class Solution {
                  public int[] productExceptSelf(int[] nums) {
                      int prefix[] = new int[nums.length];
                      int suffix[] = new int[nums.length];
                      int pre=1,suf=1;
                      for(int i=0;i<nums.length;i++){
                      prefix[i]=pre;
                      pre*=nums[i];
                      }

                      for(int i=nums.length-1;i>=0;i--){
                      suffix[i]=suf;
                      suf*=nums[i];
                      }

                      int sol[] = new int[nums.length];
                      for(int i=0;i<nums.length;i++){
                          sol[i]=prefix[i]*suffix[i];
                      }
                      return sol;
                  }
              }
