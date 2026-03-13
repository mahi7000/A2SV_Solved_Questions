class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register = {20: 0, 10:0, 5:0}

        for bill in bills:
            temp = bill
            bill -= 5

            for k, v in register.items():
                dec = min(bill // k, v)
                bill -= dec * k
                register[k] -= dec

            if bill:
                return False
            register[temp] += 1
        

        return True