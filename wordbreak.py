""" Given a string without spaces and a dictionary return or print all
possible ways that the string can be broken so that only valid words are
formed.

Eg. "programmerit", dict = { "pro", "gram", "merit", "program", "programmer",
"it" }

{"pro", "gram", "merit"}, {"program", "merit"}, {"programmer", "it"}
"""


class TrieNode(object):
    def __init__(self, data, end=False):
        self.data = data
        self.end = end
        self.children = {}

    def has_child(self, child):
        return child in self.children

    def get_child(self, child):
        return self.children[child]

    def get_children(self):
        return self.children.values()

    def add_child(self, child):
        if child in self.children:
            raise ValueError("Child already present.")
        self.children[child] = TrieNode(child)
        return self.children[child]

    def __str__(self):
        return '<{} (end: {}, children: {})>'.format(self.data,
                                                     self.end,
                                                     self.children.keys())


class Trie(object):
    def __init__(self):
        self.root = TrieNode('.')

    def add_word(self, word):
        node = self.root
        for char in word:
            if node.has_child(char):
                node = node.get_child(char)
            else:
                node = node.add_child(char)
        node.end = True

    def add_words(self, words):
        for word in words:
            self.add_word(word)

    def has_word(self, word):
        node = self.root
        for char in word:
            if node.has_child(char):
                node = node.get_child(char)
            else:
                return False
        return node.end

    def __str__(self):
        queue = [self.root]
        str_ = ""
        while len(queue) > 0:
            node = queue.pop()
            queue.extend(node.get_children())
            str_ += str(node) + str(node.get_children()) + "\n"
        return str_


# def is_word_in_trie(word, trie):
#     answer = []
#     word_added = False
#     for idx, _ in enumerate(word):
#         if trie.has_word(word[:idx+1]):
#             answer.append(word[:idx+1])
#             result = is_word_in_trie(word[idx+1:], trie)
#             if result:
#                 answer.extend(result)
#         if word_added:
#     return answer


def word_break(word, trie):
    answer = []

    for idx, char in enumerate(word):
        word_added = False
        current = []
        if trie.has_word(word[:idx+1]):
            word_added = True
            current.append(word[:idx+1])
            result = word_break(word[idx+1:], trie)

            if result:
                current.extend(result)

        if word_added:
            answer.append(current)

    # print word, current
    if len(answer) == 1:
        return answer[0]
    else:
        return answer


if __name__ == '__main__':
    trie = Trie()
    words = ["pro", "gram", "merit", "program", "programmer", "it"]
    trie.add_words(words)
    for word in words:
        print word, trie.has_word(word)
    # print trie
    print "&" * 80
    print word_break('programmerits', trie)
