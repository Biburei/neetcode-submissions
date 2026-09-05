class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        if len(s) == 1:
            return 1
        
        length = 0
        max_length = 0
        substr = {}
        start = 0
        for i in range (len(s)):
            if len(substr) == 0:
                start = i
            if s[i] not in substr:
                length += 1
                substr[s[i]] = length
            else:
                while start <= i:
                    length -= 1
                    if s[start] == s[i]:
                        substr.pop(s[start])
                        start += 1
                        break
                    substr.pop(s[start])
                    start += 1
                length = i - start + 1
                substr[s[i]] = length
            if substr.get(s[i]) > max_length:
                max_length = substr.get(s[i])
        return max_length
