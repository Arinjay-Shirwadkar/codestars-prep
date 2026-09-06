class Solution {
                  public int trap(int[] height) {
                      /* Here is my explanation for the problem.
                      First, we start by analyzing how the water is collected. Clearly,
                      There are two requirements for water to accumulate - a left wall
                      and a right wall. Now, there are a few nuances we must understand.

                      The region can be split into 2 - one, let us say, is the main region
                      the second is the end region. Now, the end region is the part from
                      the end of the array to the last high 'right wall'. This is further
                      explained below
                      Let us consider each separately, and I shall soon illustrate why
                      we do so.

                      The main region
                      In this region, it is guaranteed that the right walls are always
                      higher than or equal to the left walls. Why? Because, if this region
                      does not include the end of the array (where water may be unbound
                      i.e, overflow without a right wall), there can never be a higher left
                      wall, as this would mean overflow, which is not possible in the main
                      region. So, we can use a two pointer method. 'limi' will hold the index
                      where the first left wall is found, whereas i will iterate over the
                      array until a wall higher than or equal to it is found. Then, the
                      water in between can be calculated, subtracting the little spaces
                      occupied by walls lower than the left wall, which act as impediments.
                      The process can be repeated by considering the current right wall as
                      the next left wall, until we find the end region, where the water
                      from the last left wall will overflow. This is done using a
                      'finish' variable
                      All this is dealt with in loop 1

                      End region
                      Now, critically, though the 'last' right wall will not be able to
                      hold water up to its height as there is no corresponding right wall,
                      the impediments which we subtracted before can now hold water in
                      the tiny crevices. So, we must iterate through the array again
                      from the right, till we reach the 'last' left wall, filling
                      these tinier holes too, doing the same
                      thing we were doing in the main loop, but from the right.
                      Hence, we cover every single space available for the water to fill.
                      */
                      int l =0; //left found flag
                      int maybe=0;
                      int water=0;
                      int lim=0;
                      int limi=0;

                      int finish=0;

                      for(int i=0;i<height.length;i++){
                          if(l==0&&height[i]!=0){
                          l=1;
                          maybe=0;
                          lim=height[i]; //limiting height
                          limi=i;
                          finish=0;
                          }
                          else if(l==1){
                            if(height[i]<lim)maybe-=height[i];
                            else{ //height>=lim
                            water+=maybe+(i-limi-1)*lim;
                            l=0;
                            if(i==height.length-1){
                               finish=1;
                            }
                            else{
                            i--; //start with i as left
                            }

                           }
                          }
                      }

                      int revlimi=limi;
                      l=0;
                      if(finish==0){
                      //run again from end to get the small holes
                          for(int i=height.length-1;i>=revlimi;i--){
                          if(l==0&&height[i]!=0){
                          l=1;
                          maybe=0;
                          lim=height[i]; //limiting height
                          limi=i;

                          }
                          else if(l==1){
                            if(height[i]<lim)maybe-=height[i];
                            else{ //height>=lim
                            water+=maybe+(limi-i-1)*lim;
                            l=0;

                           i++; //start with i as right

                           }
                          }
                      }

                      }
                      return water;
                  }
              }
