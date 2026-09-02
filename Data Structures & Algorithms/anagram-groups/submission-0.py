from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            pairs[key].append(s)
        return list(pairs.values())