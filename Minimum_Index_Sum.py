class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list1_index = {}
        list2_index = {}

        for i, item in enumerate(list1):
            list1_index[item] = i

        for i, item in enumerate(list2):
            list2_index[item] = i

        min_index = float('inf')
        l = []
        for item in list1_index:
            if item in list2_index.keys():
                if list2_index[item] + list1_index[item] < min_index:
                    l = []
                    l.append(item)
                    min_index = list2_index[item] + list1_index[item]
                elif list2_index[item] + list1_index[item] == min_index:
                    l.append(item)

        return l
