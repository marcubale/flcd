import re
from hashTable import hashTable
from language_specification import *


class Scanner:
    def __init__(self, reservedWords, operators, hashTable):
        self.reservedWords = reservedWords
        self.operators = operators
        self.symTable = hashTable

    def scan(self):
        f = open('input.txt')
        for elem in re.split('\n|, | |\t', f.read().strip()):
            if elem not in self.operators:
                if elem not in self.reservedWords:
                    if elem != '':
                        if not self.symTable.contains(elem):
                            self.symTable.add(elem)
        print(self.symTable.printHashTable())


newHashTable = hashTable(10)
scanner = Scanner(reserved_words, operators, newHashTable)
scanner.scan()
