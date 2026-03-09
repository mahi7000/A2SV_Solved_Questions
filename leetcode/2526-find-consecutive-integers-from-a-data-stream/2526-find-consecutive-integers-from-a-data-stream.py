class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.queue = []

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if num != self.value:
            self.queue = []
        return len(self.queue) >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)