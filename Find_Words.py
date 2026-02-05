class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_counter = Counter(chars)

        sum_len = 0
        for word in words:
            is_good = True
            word_counter = Counter(word)

            for c in word:
                if c in chars_counter.keys():
                    if word_counter[c] > chars_counter[c]:
                        is_good = False
                        break
                else:
                    is_good = False
                    break
            if is_good:
                sum_len += len(word)

        return sum_len
