class Solution {
                  public int[] topKFrequent(int[] nums, int k) {
                      HashMap<Integer,Integer>mp = new HashMap<>();
                      for(int i =0;i<nums.length;i++){
                          mp.put(nums[i],mp.getOrDefault(nums[i],0)+1);
                      }
                      int arr[][] = new int[mp.size()][2];
                      //you could say that I am extracting the key-value pairs into a multidimensional array to sort t
                      int i=0;
                      for(int e : mp.keySet()){
                          arr[i][0]=e;
                          arr[i][1]=mp.get(e);
                          i++;
                      }
                      //now to sort the array on the basis of value (arr[1])
                      int temp[] = new int[2];

                        for(i=0;i<mp.size()-1;i++){
                            for(int j=0;j<mp.size()-i-1;j++){
                                if(arr[j][1]<arr[j+1][1]){
                                    temp = arr[j];
                                    arr[j]=arr[j+1];
                                    arr[j+1]=temp;
                                }
                            }
                        }
                      int res[] = new int[k];
                      for(i=0;i<k;i++){
                      res[i]=arr[i][0];
                      }
                      return res;
                  }
              }
