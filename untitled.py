class TrieNode:
    def __init__(self):
        self.children = {}
        self.indices = []

class WordFilter:
    def __init__(self, words):
        self.prefix_trie = TrieNode()
        self.suffix_trie = TrieNode()
        for idx, word in enumerate(words):
            self._insert_prefix(word, idx)
            self._insert_suffix(word, idx)

    def _insert_prefix(self, word, idx):
        node = self.prefix_trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.indices.append(idx)

    def _insert_suffix(self, word, idx):
        node = self.suffix_trie
        for char in reversed(word):
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.indices.append(idx)

    def f(self, pref, suff):
        prefix_indices = self._search_prefix(pref)
        suffix_indices = self._search_suffix(suff)
        i, j = len(prefix_indices) - 1, len(suffix_indices) - 1
        while i >= 0 and j >= 0:
            if prefix_indices[i] == suffix_indices[j]:
                return prefix_indices[i]
            elif prefix_indices[i] > suffix_indices[j]:
                i -= 1
            else:
                j -= 1
        return -1

    def _search_prefix(self, pref):
        node = self.prefix_trie
        for char in pref:
            if char not in node.children:
                return []
            node = node.children[char]
        return node.indices

    def _search_suffix(self, suff):
        node = self.suffix_trie
        for char in reversed(suff):
            if char not in node.children:
                return []
            node = node.children[char]
        return node.indices


wordFilter = WordFilter(["apple", "banana"])
print(wordFilter.f("a", "b"))  

wordFilter = WordFilter(["apple", "apricot", "avocado"])
print(wordFilter.f("a", "e"))  

wordFilter = WordFilter(["apple", "applet", "apples"])
print(wordFilter.f("app", "e")) 

words = ["a" * 1000] * 1000
wordFilter = WordFilter(words)
print(wordFilter.f("a", "a"))  

wordFilter = WordFilter(["", "a", "aa"])
print(wordFilter.f("", ""))  