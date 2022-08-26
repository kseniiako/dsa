# Design Trie (Prefix Tree)

# A lot of the ideas in my implementation belong to Neetcode:
# https://youtu.be/oobqoCJlHA0

class TrieNode:
    def __init__(self):
        # children nodes are stored in a dictionary-based hashmap
        self.children = {}
        # a node holds a set of children nodes
        # and a flag self.end = True showing that this 
        # is the end of word
        self.end = False

class Trie:

    def __init__(self):
        # initialize a trie
        self.root = TrieNode()
    
    def __insert__(self, word):
        # insert a word into the trie

        # start with the parent node
        cur = self.root

        for c in word:
            # if current character is not a key in the parent
            # node's children hashmap, we add it to the hashmap,
            # with its value being a new tree node. otherwise we
            # just access the TreeNode value corresponding to the
            # existing character key.
            if c not in cur.children:
                cur.children[c] = TrieNode()
            # we set current character's node to be the parent
            # node
            cur = cur.children[c]
        cur.end = True
    
    def search(self, word):
        # determine if a word exists in a trie or not
        # iterate starting with the root
        cur = self.root
        
        # iterate through all characters in the word,
        # returning false if the character we are looking for is
        # not present in the parent node's hashmap.
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        # check if the flag for end of word is set. if not, return
        # false, otherwise true.
        return cur.end
    
    def startsWith(self, prefix):
        # return true if there is a previously inserted string
        # that has given prefix, false otherwise.
        cur = self.root
        
        # for each character in prefix, check if
        # the relevant key is present in the parent node's
        # hashmap
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]

        return True



