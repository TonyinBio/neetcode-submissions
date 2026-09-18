def dfs(i, j, visited, grid, row_len, col_len):
    # print(visited)
    nexts = [
        (i + 1, j),
        (i - 1, j),
        (i, j + 1),
        (i, j - 1)
    ]

    for (i_n, j_n) in nexts:
        if not (0 <= i_n < col_len and 0 <= j_n < row_len):
            continue
        if (i_n, j_n) in visited:
            continue
        if grid[i_n][j_n] == "1":
            visited.add((i_n, j_n))
            dfs(i_n, j_n, visited, grid, row_len, col_len)

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_states = len(grid) * len(grid[0])
        row_len = len(grid[0])
        col_len = len(grid)
        visited = set()
        i, j = 0, 0
        result = 0
        while len(visited) < num_states:
            # print(i, j, len(visited), num_states)
            if ((i, j) in visited):
                i += (j + 1) // row_len
                j = (j + 1) % row_len
                continue
            
            visited.add((i, j))
            if grid[i][j] == "1":
                result += 1
                dfs(i, j, visited, grid, row_len, col_len)

            i += (j + 1) // row_len
            j = (j + 1) % row_len

        return result
            