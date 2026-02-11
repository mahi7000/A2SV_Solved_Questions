class Solution:
    def findCommonResponse(self, responses: List[List[str]]) -> str:
        response_no_duplicate = []

        for response in responses:
            response_no_duplicate.extend(list(set(response)))

        response_count = Counter(response_no_duplicate)

        max_count = max(response_count.values())

        common = []
        for key, val in response_count.items():
            if val == max_count:
                common.append(key)

        common.sort()

        return common[0]
