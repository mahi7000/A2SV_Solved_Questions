class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False

        word1_count = Counter(word1)
        word2_count = Counter(word2)

        for key in word1_count:
            if key not in word2_count:
                return False
        
        word1_freq = sorted(word1_count.values())
        word2_freq = sorted(word2_count.values())

        if word1_freq == word2_freq:
            return True
        return False
