class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        s1 = ""
        s2 = ""
        if len(str1)>=len(str2):
            s1 = str2
            s2 = str1
        else:
            s1 = str1
            s2 = str2
        # len of s1 is less or equal to s2
        ans = ""
        for i in range(len(s1)) :
            str = s1[:i+1]
            if len(s1)%len(str)==0 and len(s2)%len(str)==0:
                n = int(len(s1)/len(str))
                m = int(len(s2)/len(str))
                if s1==n*str and s2==m*str:
                    ans = str

        return ans