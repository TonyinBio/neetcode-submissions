class TrieNode:
    def __init__(self, kids={}, is_word=False):
        self.kids = {}
        self.is_word = is_word
    
class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.head
        for c in word:
            if c in node.kids:
                next_node = node.kids[c]
            else:
                next_node = TrieNode()
                node.kids[c] = next_node
            node = next_node
        node.is_word = True

    def search(self, word: str) -> bool:
        return self._search_from_node(word, self.head)

    def _search_from_node(self, word, node):
        for i, c in enumerate(word):
            if c in node.kids:
                node = node.kids[c]
            elif c == ".":
                return any([
                    self._search_from_node(k + word[i + 1:], node) 
                    for k in node.kids.keys()
                ])
            else:
                return False

        return node.is_word