class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        c,c1={},{}
        for i in range(len(s)):
            c[s[i]]=c.get(s[i],0)+1
            c1[t[i]]=c1.get(t[i],0)+1
        return c==c1
                    
        