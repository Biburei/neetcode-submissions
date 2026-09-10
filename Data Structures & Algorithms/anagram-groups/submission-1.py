from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = defaultdict(list)
        for word in strs:
            key = "".join(sorted(word))
            pairs[key].append(word)
        return list(pairs.values())
            