class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #nums = nums.sort()
        pair = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] + nums[j] == target:
                    pair.append(i)
                    pair.append(j)
                    return pair
        return pair