class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        substring = set()
        max_sequence = 0
        left = 0
        for right in range(len(s)):
            while s[right] in substring:
                substring.remove(s[left])
                left += 1
            substring.add(s[right])
            if len(substring) > max_sequence:
                max_sequence = len(substring)
        return max_sequence