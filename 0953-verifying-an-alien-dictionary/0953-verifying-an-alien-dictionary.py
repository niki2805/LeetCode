class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic={}
        for i in range(26):
            dic[order[i]] = i
        
        def check (str1, str2, dic):
            mn = min(len(str1),len(str2))
            for i in range(mn):
                if str1[i] != str2[i] :
                   return dic[str1[i]] > dic[str2[i]]
    
            return len(str1) > len(str2)
        

        for i in range(1,len(words)):
            if check(words[i-1],words[i],dic):
                return False
        return True
