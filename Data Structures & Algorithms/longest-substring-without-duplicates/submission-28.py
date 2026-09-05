class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        substr = {}
        start = 0
        sequence = 0
        max_sequence = 0
        for i in range (len(s)):
            if s[i] in substr and substr[s[i]] >= start:
                start = substr.get(s[i]) + 1
            sequence = i - start + 1
            substr[s[i]] = i
            if sequence > max_sequence:
                max_sequence = sequence
        return max_sequence