class Solution:
    def climbStairs(self, n: int) -> int:
        visited = {}
        def recurse(n):
            if n in visited:
                return visited[n]
            
            if n == 1:
                return 1
            elif n == 2:
                return 2
            else:
                visited[n] = recurse(n - 1) + recurse(n - 2)
                return visited[n]
        return recurse(n)