class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1=sorted(s)
        if s1==sorted(t):
            return True
        else:
            return False
        