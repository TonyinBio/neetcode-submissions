class Solution:
    def myPow(self, x: float, n: int) -> float:
        # memo = {}
        def myPow1(x, n):
            # if (x, n) in memo: 
            #     print("a")
            #     return memo[(x, n)]
            if n == 0: return 1
            if n == 1: return x
            m = n // 2
            result = self.myPow(x * x, m)
            # result *= result
            if n % 2 == 1:
                result = result * x
            # memo[(x, n)] = result
            return result
        if n < 0: 
            x = 1 / x
            n = -n
        return myPow1(x, n)