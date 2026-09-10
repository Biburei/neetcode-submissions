from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        total = Counter(nums)
        final = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in total.items():
            bucket[freq].append(num)
        for i in range (len(bucket) - 1, 0, -1):
            for number in bucket[i]:
                final.append(number)
                if len(final) == k:
                    return final