class Solution {
              public:

                   vector<int> findXSum(vector<int>& nums, int k, int x) {
                       int i=0,j=k-1,c=0,sum=0,p=0;
                       int n = nums.size();
                       int max=nums[0];
                       for(i=1;i<n;i++)
                       if(nums[i]>max)max=nums[i];

                           vector<int>freq(max+1,0);

                     vector<int> answer(n-k+1);
                    //11232134 x=2

                        while(p<n-k+1){
                          fill(freq.begin(), freq.end(), 0);
                       for(i=p;i<p+k&&i<n;i++){

                        freq[nums[i]]++;

                    }
                    answer[c]=findsum(freq,x);
                      c++; p++;

                       }

                       return answer;
                   }

                   int findsum(vector<int>&freq,int x){
                    int max=freq[0],maxpos=0,len=freq.size(),sum=0;
                    for(int j=0;j<x;j++){
                       for(int i=0;i<len;i++){
                    if(freq[i]>max){max=freq[i]; maxpos=i;}
                    else if(freq[i] == max) {
                   if(i>maxpos){maxpos=i;max=freq[i];}
              }
                       }
                    sum=sum+maxpos*freq[maxpos];freq[maxpos]=0;
                    max=0; maxpos=0;

                   }
                   return sum;
                   }
              };
