class Solution:
    def minWindow(self, s: str, t: str) -> str:
        p1,p2=0,0
        substring=[]
        tmap={}
        sol=""
        bestp1,bestp2=-1,-1
        distinct=0
        for char in t:
            if char not in tmap:
                distinct+=1
                tmap[char]=1
            else:
                tmap[char]=tmap[char]+1
        satisfied=0
        smap={}
        for p2 in range(0,len(s)):
            #consider the element at p2 now
            char = s[p2]
            if char in tmap:
                if char not in smap:
                    smap[char]=1
                else:
                    smap[char]=smap[char]+1
                if smap[char]==tmap[char]:
                    satisfied+=1
            while satisfied==distinct:
                #shrink the window
                #substring=s[p1:p2+1]
                if p2-p1+1<bestp2-bestp1+1 or bestp1==-1:
                    bestp1=p1
                    bestp2=p2
                if s[p1] in smap and s[p1] in tmap:
                    smap[s[p1]]-=1
                    if smap[s[p1]]<tmap[s[p1]]:
                        satisfied-=1
                    if smap[s[p1]]==0:
                        smap.pop(s[p1])
                    
                p1+=1
        sol = s[bestp1:bestp2+1]
        return "".join(sol)