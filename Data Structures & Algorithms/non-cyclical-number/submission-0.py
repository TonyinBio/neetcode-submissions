class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        def isHappy1(n):
            if n in seen: return False
            if n == 1: return True
            seen.add(n)
            m = 0
            while n > 9:
                m += (n % 10) ** 2
                n //= 10
            m += n ** 2
            return isHappy1(m)

        return isHappy1(n)