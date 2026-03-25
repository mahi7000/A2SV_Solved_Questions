class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        self.minn = inf
        def cookie(i, children):
            if i == len(cookies):
                self.minn = min(self.minn, max(children))
                return

            for j in range(k):
                if children[j] < self.minn:
                    children[j] += cookies[i]
                    cookie(i + 1, children)
                    children[j] -= cookies[i]


        cookie(0, [0] * k)
        return self.minn