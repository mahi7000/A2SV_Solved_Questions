class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_size = min(len(i) for i in strs)

        while min_size > 0:
            first_pref = strs[0][:min_size]
            done = True
            for s in strs[1:]:
                if s[:min_size] != first_pref:
                    done = False
                    break
            if done:
                return first_pref

            min_size -= 1

        return ""
