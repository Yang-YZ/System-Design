# Python 3

class BloomFilter:
    def __init__(self, k):
        """
        @param: k: An integer
        """
        self.list = []
        self.count = k

    def add(self, word):
        """
        @param: word: A string
        @return: nothing
        """
        if len(self.list) < self.count:
            self.list.append(word)
            self.count += 1
        else:
            print("No space to add new entry."

    def remove(self, word):
        """
        @param: word: A string
        @return: nothing
        """
        if self.contains(word):
            self.list.remove(word)
        else:
            print(word, " is not in this file.")

    def contains(self, word):
        """
        @param: word: A string
        @return: True if contains word
        """
        if word in self.list:
            return True
        else:
            return False
