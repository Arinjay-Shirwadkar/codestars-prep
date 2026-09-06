class Solution {
                  public int shipWithinDays(int[] weights, int days) {
                      //here the logical condition to get target is different
                      //otherwise this is quite similar to koko eating bananas

                      //here, the examples are totally skewed

                      int validw=0, l,u,d=0,runW=0,sum=0;
                      //the range of possible weight will be from the maximum weight
                      //to what, though? No doubt the sum of all weights so all can be shipped
                      //at once in a day
                      //in the boxes, so we must find that
                      int max=0;
                      for(int i=0;i<weights.length;i++){
                          if(weights[i]>max)max = weights[i];
                          sum+=weights[i];
                      }
                      l=max;u=sum;
                      int w=0;

                      while(l<=u){
                          w = l+(u-l)/2;
                          //having selected a weight, we check its validity
                          d=0;
                          runW=0;
                          for(int i=0;i<weights.length;i++){
                               if(i==weights.length-1){
                                   d++;
                               }
                               if(runW+weights[i]>w){
                                   runW = weights[i];
                                   d++;
                               }

                              else if(runW+weights[i]<=w){runW+=weights[i]; continue;}
                          }

                          if(d>days){
                              //not a valid k then
                              l=w+1;
                          }
                          else{ //if d<=days
                          //good, but can we do better?
                          validw = w;
                          u = w-1;

                          }
                      }
                      return validw;
                  }
              }
