from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counted = Counter(nums)
        n = len(nums) / 2
        for value, appearances in counted.items():
            if appearances > n:
                return value
            
        