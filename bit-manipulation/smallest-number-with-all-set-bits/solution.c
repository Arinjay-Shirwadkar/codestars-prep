#include<math.h>
              int smallestNumber(int n) {
                  /*
                  1 = 1
                  11 = 1+2
                  111 = 1+2+4
                  1111 = 1+2+4+8
                  */
                  int d=0,num=0,c=1;
                  while(1==1){
                  for(d=0;d<c;d++){
                   num=num+pow(2,d);
                  }
                  if(num>=n)return num;
                  num=0; c++;
                  }
              }
