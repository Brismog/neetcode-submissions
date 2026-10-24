from collections import Counter

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        s1 = s.replace(" ", "").lower()
        s2 = t.replace(" ", "").lower()

        return Counter(s1) == Counter(s2)

instance = Solution()
result = instance.isAnagram("racecar","carrace")

print(result)