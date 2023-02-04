class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        hmap=Counter(s1)
        chars=len(hmap)
        
        l=len(s1)
        
        i,j=0,0
        
        while(j<len(s2)):
            
            if s2[j] in hmap:
                hmap[s2[j]]-=1
                if hmap[s2[j]]==0:
                    chars-=1
                
            if j-i+1<l:
                j+=1
                
            else:
                if chars==0:
                    return True
                
                if s2[i] in hmap:
                    hmap[s2[i]]+=1
                    if hmap[s2[i]]==1:
                        chars+=1
                        
                i+=1
                j+=1
                        
        return False
                