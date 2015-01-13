class Node(object):
    def __init__(self, letter, end=False):
        self.letter = letter
        self.end = end
        self.children = {}

    def add_child(self, node):
        self.children[node.letter] = node

    def has_child(self, letter):
        return letter in self.children

    def get_child(self, letter):
        if self.has_child(letter):
            return self.children[letter]
        else:
            raise ValueError

    def __repr__(self):
        return "Letter: %s, End: %s, Children %s" % (
            self.letter, self.end, self.children.keys())


class Trie(object):
    def __init__(self):
        self.root = Node('', True)

    def add_word(self, word):
        ptr = self.root
        for letter in word:
            if ptr.has_child(letter):
                ptr = ptr.get_child(letter)
            else:
                child = Node(letter)
                ptr.add_child(child)
                ptr = child
        # mark this node to have a complete word
        ptr.end = True

    def exists(self, word):
        ptr = self.root
        for letter in word:
            if ptr.has_child(letter):
                ptr = ptr.get_child(letter)
            else:
                return False

        return ptr.end

    def __str__(self):
        ptr = self.root
        return "%s" % ptr.children


baby_names = ['gaga', 'goo', 'gag']
garbled_text = 'gagagoogoogag'


def find_baby_names(baby_names, garbled_text):
    trie = Trie()
    for word in baby_names:
        trie.add_word(word)
    found_words = []

    start, end = 0, len(garbled_text)
    while end > start:
        if trie.exists(garbled_text[start:end]):
            found_words.append(garbled_text[start:end])
            start, end = end, len(garbled_text)
        else:
            end -= 1
    print ' '.join(found_words)


find_baby_names(baby_names, garbled_text)
