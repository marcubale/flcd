
class hashTable:
    def __init__(self, size):
        self.size = size
        self.items = []
        for i in range(0, size):
            self.items.append([])
        self.counter = 1

    def size(self):
        return self.size

    def hash(self, key):
        s = 0
        for i in range(len(key)):
            s += ord(key[i])
        return s % self.size

    def add(self, key):
        hashVal = self.hash(key)
        if not self.contains(key):
            self.items[hashVal].append((self.counter, key))
            self.counter += 1
            return True
        return False

    def contains(self, key):
        hashVal = self.hash(key)
        for tpl in self.items[hashVal]:
            if key in tpl:
                return True
        if key in self.items[hashVal]:
            return True
        return False

    def getPosition(self, key):
        if self.contains(key):
            listPosition = self.hash(key)
            listIndex = 0
            for e in self.items[listPosition]:
                if e[1] != key:
                    listIndex += 1
                else:
                    break
            return listPosition, listIndex
        return -1, -1

    def remove(self, key):
        hashVal = self.hash(key)
        if key in self.items[hashVal]:
            self.items[hashVal].remove(key)
            return True
        return False

    def printHashTable(self):
        for i in range(self.size):
            print("position: ", i, " -> ", end='')
            if len(self.items[i]) == 0:
                print("empty")
            else:
                print(*self.items[i], sep="; ")

    def getItems(self):
        return self.items

    def toString(self):
        """
        prints a string that illustrates the hashtable
        :return:
        """
        for i in range(self.size):
            print(i, " : ", end='')
            if len(self.items[i]) == 0:
                print("empty")
            else:
                print(*self.items[i], sep="; ")
