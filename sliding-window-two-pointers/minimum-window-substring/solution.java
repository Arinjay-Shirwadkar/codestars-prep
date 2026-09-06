class Solution {
                  public String minWindow(String s, String t) {
                      HashMap<Character,Integer> com = new HashMap<>();
                      HashMap<Character,Integer> win = new HashMap<>();
                      int p1=0,p2=t.length()-1;
                      if (p2>=s.length())return "";

                      for(int i=0;i<t.length();i++){
                          com.put(t.charAt(i),com.getOrDefault(t.charAt(i),0)+1);
                          win.put(t.charAt(i),0);
                      }
                      //win will have 0 for all the characters of t

                      for(int i=0;i<t.length()-1;i++){
                          if(win.containsKey(s.charAt(i)))win.put(s.charAt(i),win.get(s.charAt(i))+1);
                      }
                      //the last character will not be put,on purpose
                      //we count the frequencies of the characters in t and of the
                      //first t.length() characters in s too
                      int valid=1; //1 by default. 0 if invalid
                      int min=s.length()+1;
                      String minS="";
                      int movep2=1;
                      while(p2<s.length()){
                          if(movep2==1){
                              if(win.containsKey(s.charAt(p2))){
                                  win.put(s.charAt(p2),win.get(s.charAt(p2))+1);
                              }
                          }
                          movep2=0;
                          //check the validity of a substring
                          valid=1;
                          for(char c: com.keySet()){ //o(26n) worst case
                              if(win.get(c)>=com.get(c))continue;
                              else{valid =0; break;}
                          }
                          if(valid==1){
                              if(p2-p1+1<min){
                                  min=p2-p1+1;
                                  minS=s.substring(p1,p2+1);
                              }
                              if(win.containsKey(s.charAt(p1))){
                              win.put(s.charAt(p1),win.get(s.charAt(p1))-1);
                          }
                              p1++;

                          }
                          else{
                              p2++;
                              movep2=1;
                          }

                      }
                      return minS;
                  }
              }
