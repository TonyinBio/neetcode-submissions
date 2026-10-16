from itertools import product

class TrieNode:
    def __init__(self, word=None):
        self.kids = {}
        self.word = word

class Trie:
    def __init__(self):
        self.head = TrieNode()

    def add(self, word):
        node = self.head
        for c in word:
            if c in node.kids:
                new_node = node.kids[c]
            else:
                new_node = TrieNode()
                node.kids[c] = new_node
            node = new_node

        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.add(word)

        m = len(board)
        n = len(board[0])
        def neighbours(pos):
            r, c = pos
            neighs = []
            if r + 1 < m:
                neighs.append((r + 1, c))
            if r - 1 >= 0:
                neighs.append((r - 1, c))
            if c + 1 < n:
                neighs.append((r, c + 1))
            if c - 1 >= 0:
                neighs.append((r, c - 1))
            return neighs
        
        # dfs trie, condition to go to kid is exists in trie and board_neighbours
        result = set()
        def dfs(trie_node, pos, explored):
            # pre-order
            # root
            if trie_node.word:
                result.add(trie_node.word)
            explored.add(pos)
            # kids
            for kid_pos in neighbours(pos):
                if kid_pos in explored:
                    continue
                char = board[kid_pos[0]][kid_pos[1]]
                if char in trie_node.kids:
                    # print(char)
                    dfs(trie_node.kids[char], kid_pos, explored.copy())
        
        for pos in product(range(m), range(n)):
            # print(pos)
            char = board[pos[0]][pos[1]]
            if char in trie.head.kids:
                dfs(trie.head.kids[char], pos, set())

        return list(result)
