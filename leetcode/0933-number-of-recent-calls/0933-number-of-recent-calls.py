class RecentCounter:

    def __init__(self):
        self.recent = []

    def ping(self, t: int) -> int:
        self.recent.append(t)
        while t - self.recent[0] > 3000:
            self.recent.pop(0)

        return len(self.recent)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)