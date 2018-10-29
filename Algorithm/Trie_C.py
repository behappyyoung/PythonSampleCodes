class Trie:

    def __init__(self):
        self.root = {}

    def make_trie(self, args):
        """
        Make a trie by given words.
        """

        for word in args:
            if type(word) != str:
                raise TypeError("Trie only works on str!")
            temp_trie = {}
            for letter in word:
                temp_trie = temp_trie.setdefault(letter, {})
            temp_trie = temp_trie.setdefault('_end_', '_end_')

        self.root = temp_trie

    def in_trie(self, word):
        '''
        Detect if word in trie.
        '''
        if type(word) != str:
            raise TypeError("Trie only works on str!")

        temp_trie = self.root
        for letter in word:
            if letter not in temp_trie:
                return False
            temp_trie = temp_trie[letter]
        return True

    def remove_from_trie(self, word, depth):
        """
        Remove certain word from trie.
        """
        if word and word[depth] not in self.root:
            return False

        if len(word) == depth + 1:
            del self.root[word[depth]]
            if not self.root:  # Node becomes a leaf, indicate its parent to delete it.
                return True
            return False
        else:
            temp_trie = self.root

            # Recursively climb up to delete.
            if self.remove_from_trie(temp_trie[word[depth]], word, depth + 1):
                if temp_trie:
                    del temp_trie[word[depth]]
                return not temp_trie
        return False

    def count_trie(self):
        sub_count = 0
        for m, v in self.root.items():
            print m, 'sub : ', v
            if v == '_end_':
                sub_count = sub_count + 1
            else:
                sub_count += self.count_trie(v)
        return sub_count