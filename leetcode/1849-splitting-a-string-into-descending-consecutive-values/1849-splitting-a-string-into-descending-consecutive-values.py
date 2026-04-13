class Solution:
    def splitString(self, s: str) -> bool:
        def backtrack(path, options):
            if not options and len(path) > 1:
                return True

            for i in range(len(options)):
                curr = options[:i + 1]
                if not path or int(path[-1]) == int(curr) + 1:
                    if backtrack(path + [curr], options[i + 1:]):
                        return True
            
            return False
                

            # if len(arr) > 1 and int(arr[-1]) + 1 == int(arr[-2]): return True
            # elif i == len(s) - 1: return False

            # return backtrack(i + 1, arr[:-1] + [arr[-1][:i]] + [arr[-1][i + 1:]]) or backtrack(i + 1, arr[:])
          
        return backtrack([], s)