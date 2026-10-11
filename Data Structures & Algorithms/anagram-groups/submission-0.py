from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for i in strs:
            seen["".join(sorted(i))].append(i)

        return list(seen.values())