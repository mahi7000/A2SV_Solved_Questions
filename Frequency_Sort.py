class Solution:
    def frequencySort(self, s: str) -> str:
        freq_count = Counter(s)

        freq_count = {key: val for key, val in sorted(freq_count.items(), key=lambda item: item[1], reverse=True)}

        new_s = ""
        for key, val in freq_count.items():
            new_s += key * val

        return new_s
