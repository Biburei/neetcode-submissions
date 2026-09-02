class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        found = {}
        for i, j in enumerate(nums):
            difference = target - j
            if difference in found:
                return [found[difference], i]
            found[j] = i