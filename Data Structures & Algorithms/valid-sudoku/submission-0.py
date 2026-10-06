# import itertools
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        for r in range(n):
            seen = set()
            for i in range(n):
                if board[r][i] == ".": continue
                if board[r][i] in seen: 
                    # print(r, i, seen)
                    # print("A")
                    return False
                seen.add(board[r][i])
        for c in range(n):
            seen = set()
            for i in range(n):
                if board[i][c] == ".": continue
                if board[i][c] in seen: 
                    # print("B")
                    return False
                seen.add(board[i][c])
        
        for sub_r in range(3):
            for sub_c in range(3):
                seen = set()
                for i in range(3):
                    for j in range(3):
                        # print(r, c)
                        r = sub_r * 3 + i
                        c = sub_c * 3 + j
                        if board[r][c] == ".": continue
                        if board[r][c] in seen: 
                            # print("C")
                            return False
                        seen.add(board[r][c])
        
        return True