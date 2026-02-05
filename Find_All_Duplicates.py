class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums_counter = Counter(nums)

        duplicate = []
        for num, count in nums_counter.items():
            if count == 2:
                duplicate.append(num)

        return duplicate
