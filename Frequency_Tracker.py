class FrequencyTracker:

    def __init__(self):
        self.freq = []
        self.freq_counter = defaultdict(int)
        self.freq_freq = defaultdict(int)

    def add(self, number: int) -> None:
        self.freq.append(number)
        self.freq_counter[number] += 1
        if self.freq_counter[number] != 0:
            self.freq_freq[self.freq_counter[number] - 1] -= 1
        if self.freq_freq[self.freq_counter[number] - 1] == 0:
            del self.freq_freq[self.freq_counter[number] - 1] 
        self.freq_freq[self.freq_counter[number]] += 1


    def deleteOne(self, number: int) -> None:
        if number in self.freq:
            self.freq.remove(number)
            self.freq_freq[self.freq_counter[number]] -= 1
            if self.freq_freq[self.freq_counter[number]] == 0:
                del self.freq_freq[self.freq_counter[number]]

            self.freq_counter[number] -= 1
            if self.freq_counter[number] == 0:
                del self.freq_counter[number]

            self.freq_freq[self.freq_counter[number]] += 1

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.freq_freq


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
