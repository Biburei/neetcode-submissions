from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = list(s1)
        sliding = list(s2[:len(s1)])
        for i in range (len(s1), len(s2)):
            if Counter(window) == Counter(sliding):
                return True
            del sliding[0]
            sliding.append(s2[i])
        if Counter(window) == Counter(sliding):
            return True
        return False