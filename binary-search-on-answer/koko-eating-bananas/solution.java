class Solution {
                  public int minEatingSpeed(int[] piles, int h) {
                     //I begin to see that binary search can be used to effectively find
                     //the solution, if we know what range it lies in and a logical
                     //condition about it. This can either be the value itself,
                     //as in finding a target, or it can be, for example, knowing that
                     //it must be the square root of some given number. It can even
                     //be used to minimize or maximize if one moves l and u wisely.

                      //find maximum in piles
                      int max = 0;
                      for(int i=0;i<piles.length;i++){
                            if(piles[i]>max)max=piles[i];
                      }
                      int l =1, u=max,k=0;
                      long hours=0;
                      //we are searching for minimum k in range 1 to max.
                      //we need n iterations each turn to check the validity of any k
                      //we will also minimize it by reducing u everytime a valid k is found
                      int validk=0;
                      while(l<=u){
                        k = l + (u-l)/2;

                       //check validity of found k
                       hours=0;
                       for(int i=0;i<piles.length;i++){
                           hours+=Math.ceil((double)piles[i]/k); //round up to count that extra 1 hour
                       }
                       if(hours>h){
                           l=k+1;
                       }
                       else if(hours<=h){
                           //can we do better?
                           validk = k;
                           u=k-1;
                       }

                      }
                      return validk;
                  }
              }
