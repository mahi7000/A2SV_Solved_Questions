#User function Template for python3
from collections import Counter 
class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        a_count = Counter(a)
        b_count = Counter(b)
        
        for num, count in b_count.items():
            if a_count[num] < count:
                return False
                
        return True
