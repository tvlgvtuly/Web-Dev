class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit not in node.children:
                node.children[bit] = TrieNode()
            node = node.children[bit]

    def find_max_xor(self, num):
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            toggled_bit = 1 - bit
            if toggled_bit in node.children:
                max_xor += (1 << i)
                node = node.children[toggled_bit]
            else:
                node = node.children.get(bit, None)
                if node is None:
                    break
        return max_xor

def findMaximumXOR(nums):
    trie = Trie()
    for num in nums:
        trie.insert(num)
    max_xor = 0
    for num in nums:
        max_xor = max(max_xor, trie.find_max_xor(num))
    return max_xor

# Example Usage:
print(findMaximumXOR([3, 10, 5, 25, 2, 8]))  
print(findMaximumXOR([14, 70, 53, 83, 49]))  