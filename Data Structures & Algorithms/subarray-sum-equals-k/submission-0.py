class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cnt = 0
        pairs = {0 : 1}
        current_sum = 0

        for num in nums:
            current_sum += num
            target = current_sum - k

            if target in pairs:
                cnt += pairs.get(target)
            pairs[current_sum] = pairs.get(current_sum, 0) + 1
        return cnt