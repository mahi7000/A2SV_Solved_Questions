class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_count = Counter(ransomNote)
        mag_count = Counter(magazine)

        for key, val in ransom_count.items():
            if mag_count[key] < val:
                return False

        return True
