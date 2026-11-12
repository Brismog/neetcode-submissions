class Solution:
    def isAnagram(self, s: str(str), t: str(str)):
        
        if len(s) != len(t):
            return False 

        countS, countT = {}, {}

        for item in range(len(s)):
            countS[s[item]] = 1+countS.get(s[item], 0)
            countT[t[item]] = 1+countT.get(t[item], 0)
            
        for charectar in countS:
            if countS[charectar] != countT.get(charectar, 0):
                return False 
        
        return True