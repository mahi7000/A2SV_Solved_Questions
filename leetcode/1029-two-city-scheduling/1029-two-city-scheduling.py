class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        cities = []
        for i, cost in enumerate(costs):
            cities.append((abs(cost[0] - cost[1]), i))

        cities.sort(key=lambda x:x[0], reverse=True)
        print(cities)

        summ = 0
        a = 0
        b = 0
        for _, i in cities:
            cost = min(costs[i])
            if cost == costs[i][0] and a == len(cities) // 2:
                cost = costs[i][1]
            elif cost == costs[i][1] and b == len(cities) // 2:
                cost = costs[i][0]

            if cost == costs[i][0]:
                a += 1
            else:
                b += 1
            summ += cost

        return summ