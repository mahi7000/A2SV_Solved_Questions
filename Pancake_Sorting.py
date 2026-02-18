class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if arr == sorted(arr):
            return []

        pancake = []
        for i in range(len(arr), 1, -1):
            print(arr[:i])
            max_ind = arr.index(max(arr[:i]))
            k = max_ind + 1
            if k > 1:
                pancake.append(k)

            p = 0
            q = max_ind
            while p < q:
                arr[p], arr[q] = arr[q], arr[p]
                p += 1
                q -= 1

            pancake.append(i)

            p = 0
            q = i - 1
            while p < q:
                arr[p], arr[q] = arr[q], arr[p]
                p += 1
                q -= 1
        print(arr)

        return pancake 
