from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        final = []
        bucket = [[] for _ in range(len(nums) + 1)]
        for num, freq in count.items():
            bucket[freq].append(num)
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                final.append(num)
                if len(final) == k:
                    return final