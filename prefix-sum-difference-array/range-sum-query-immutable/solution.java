class NumArray {
                  int num[];
                  int pre[];
                  public NumArray(int[] nums) {
                    num = nums;
                    int runSum=0;
                    pre = new int[num.length];
                    for(int i=0;i<num.length;i++){
                      runSum+=num[i];
                      pre[i]=runSum;
                    }
                  }

                  public int sumRange(int left, int right) {
                      return (pre[right]-pre[left]+num[left]);
                  }
              }

              /**
               * Your NumArray object will be instantiated and called as such:
               * NumArray obj = new NumArray(nums);
               * int param_1 = obj.sumRange(left,right);
               */
