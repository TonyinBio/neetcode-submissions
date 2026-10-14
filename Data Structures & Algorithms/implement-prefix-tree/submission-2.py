class PrefixTreeNode:
    def __init__(self, is_word=False, childs=None):
        self.is_word = is_word
        if childs is None:
            childs = [None] * 26
        self.childs = childs

class PrefixTree:

    def __init__(self):
        self.head = PrefixTreeNode()

    def insert(self, word: str) -> None:
        node = self.head
        for c in word:
            childs = node.childs
            i = ord(c) - ord("a")
            if childs[i]:
                node = childs[i]
            else:
                node = PrefixTreeNode()
                childs[i] = node
        node.is_word = True

    def search(self, word: str) -> bool:
        node = self._traverse(word)
        return node is not None and node.is_word

    def startsWith(self, prefix: str) -> bool:
        node = self._traverse(prefix)
        return True if node else False

    def _traverse(self, word):
        '''traverse the trie, return the last node if successful
        else return none'''
        node = self.head
        for c in word:
            childs = node.childs
            i = ord(c) - ord("a")
            if childs[i]:
                node = childs[i]
            else:
                return None
        return node

        