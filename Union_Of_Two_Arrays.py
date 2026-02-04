class Solution:    
    def findUnion(self, a, b):
        # code here
        a.extend(b)
        a = set(a)
        
        return list(a)
