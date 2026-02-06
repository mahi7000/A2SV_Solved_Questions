class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            old_s = s
            s = "".join(sorted(s))
            anagrams[s].append(old_s)

        result = []
        for value in anagrams.values():
            result.append(value)

        return result
