class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_clean = re.sub(r'[^a-zA-Z0-9]','',s)
        left = 0
        right = len(s_clean) -1
        while left < right:
            if s_clean[left].lower() == s_clean[right].lower():
                left +=1
                right -=1
            else:
                return False
        return True
        