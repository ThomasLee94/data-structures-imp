# Building a Trie is O(m * n), m being the longest word and n being the num or words
# Searching from a Trie is O(m), m being len of word
# Searching for all words matching with prefix is O(m), m being the longest path in the subtrees of the child after the end of the prefix

class Node:
    def __init__(self, val=None):
        self.val = val
        self.terminal = False
        self.children = {} # {child_key: Node(child_key)}
    
    def add_child(self, char):
        if char not in self.children:
            self.children[char] = Node(char)
    
    def has_child(self, val):
        return val in self.children
    
class Trie:
    def __init__(self, iterable=None):
        self.root = Node("^")

        if iterable:
            self.add_words(iterable)

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def add_word(self, word):
        """
        Iterative
        """

        node = self.root

        for i in range(len(word)):
            if not node.has_child(word[i]):
                node.add_child(word[i])

            node = node.children[word[i]]
        
        node.terminal = True

    def all_words(self):
        node = self.root
        words = []

        for node_obj in node.children.values():
            for word in self.dfs(node_obj, []):
                temp_str = ""
                for char in word:
                    temp_str += char
                words.append(temp_str)
        
        return words
    
    def words_with_prefix(self, prefix):
        node = self.root
        path = []
        words = []

        for char in prefix:
            path.append(char)

        for char in prefix:
            node = node.children[char]

        for word in self.dfs(node, path):
            words.append(word)
        
        return words

    def dfs(self, node, path):
        if node.terminal:
            yield path + [node.val]
        
        for child_node_obj in node.children.values():
            yield from self.dfs(child_node_obj, path + [node.val])

def solve(words):
    # words = ["jason", "jaymo", "justin", "ted"]
    t = Trie(words)
    res1 = t.all_words()
    res2 = t.words_with_prefix("j")
    print(res1)
    print(res2)

solve(["jason", "jaymo", "justin", "ted"])



