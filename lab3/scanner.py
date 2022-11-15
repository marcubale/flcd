import re
from hashTable import hashTable
from language_specification import *


class Scanner:
    def __init__(self, reservedWords, operators, hashTable, pif, tokenFile):
        self.reservedWords = reservedWords
        self.operators = operators
        self.symTable = hashTable
        self.pif = pif
        # self.symTable = hashTable
        self.counter = 1
        self.tokenFile = tokenFile
        self.tokenTable = []

    def generateTokenTable(self,):
        f = open(self.tokenFileName, 'r')
        counter = 2
        self.tokenTable.append(("CONST", 0))
        self.tokenTable.append(("IDENT", 1))
        for line in f.readlines():
            self.tokenTable.append((line.strip(), counter))
            counter += 1

    def scan(self):
        f = open('input.txt')
        lineCount = 0
        lexicalError = False
        lexicalErrorLine = -1
        lexicalErrorToken = -1

        # for elem in re.split('\n|, | |\t', f.read().strip()):
        #     if elem not in self.operators:
        #         if elem not in self.reservedWords:
        #             if elem != '':
        #                 if not self.symTable.contains(elem):
        #                     self.symTable.add(elem)
        # print(self.symTable.printHashTable())

        for line in f.readlines():
            lineCount += 1
            for elem in re.split('\n|, | |\t', line.strip()):
                if elem in reserved_words or elem in operators or elem in separators:
                    self.pif.append((elem, self.getTokenCode(elem), 0))
                # if lineCount == 6:
                elif elem == '':
                    pass
                elif bool(re.search("^[a-zA-Z_][a-zA-Z_0-9]*$", elem)):
                    self.symTable.add(elem)
                    self.pif.append((elem, 1, self.getSymTableCode(elem)))
                elif bool(re.search("^[0-9]+$", elem)):
                    self.symTable.add(elem)
                    self.pif.append((elem, 0, self.getSymTableCode(elem)))
                else:
                    lexicalError = True
                    lexicalErrorLine = lineCount
                    lexicalErrorToken = elem

        if lexicalError:
            print("Lexical Error at line ", lexicalErrorLine,
                  " token ", lexicalErrorToken)
        else:
            print("lexically correct")

        print("\nSymTable:")
        print(self.symTable.toString())
        print("\nPIF:")
        for pif_pair in self.pif:
            print(pif_pair)
        print("\nToken Table: ")
        print(scanner.tokenTable)

    def getTokenCode(self, elem):
        for tkn in self.tokenTable:
            if elem in tkn:
                return tkn[1]
        return False

    def getSymTableCode(self, elem):
        symTableItems = self.symTable.getItems()
        positionInHashTable, positionInInnerList = self.symTable.getPosition(
            elem)
        codePair = symTableItems[positionInHashTable][positionInInnerList]
        if codePair[1] == elem:
            return codePair[0]


pif = []
newHashTable = hashTable(10)
scanner = Scanner(reserved_words, operators, newHashTable, pif, "token.in.txt")
scanner.scan()
