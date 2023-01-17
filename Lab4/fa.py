import re

"""
p = "p"
q = "q"
r = "r"
a = "a"
b = "b"
states = [p, q, r]
alphabet = [a, b]
initial_state = p
final_states = [r]
transitions = [
    (p, q, a),
    (q, q, a),
    (q, r, b),
    (p, r, b)
]
"""


class FiniteAutomata:
    def __init__(self, inputFileName):
        self.states = []
        self.initial_state = None
        self.alphabet = []
        self.final_states = []
        self.transitions = []
        self.inputFileName = inputFileName
        self.readInput()

    def readInput(self):
        f = open(self.inputFileName)
        transitionsFlag = False
        for line in f.readlines():
            firstElem = re.split(" = ", line.strip())[0]
            if firstElem != "transitions =" and not transitionsFlag:
                secondElem = re.split(" = ", line.strip())[1]
                if firstElem == "states":
                    for state in re.split(" ", secondElem.strip()):
                        self.states.append(state)
                if firstElem == "alphabet":
                    for letter in re.split(" ", secondElem.strip()):
                        self.alphabet.append(letter)
                if firstElem == "initial_state":
                    self.initial_state = secondElem.strip()
                if firstElem == "final_states":
                    for state in re.split(" ", secondElem.strip()):
                        self.final_states.append(state)
            else:
                if firstElem == "transitions =":
                    transitionsFlag = True
                else:
                    t1 = re.split("\\(", firstElem.strip())[1]
                    t1 = re.split(",", t1.strip())[0]
                    t2 = re.split(", ", firstElem.strip())[1]
                    t2 = re.split("\\)", t2.strip())[0]
                    t3 = re.split("-> ", firstElem.strip())[1]
                    self.transitions.append((t1, t2, t3))
        """
        print(self.states)
        print(self.alphabet)
        print(self.initial_state)
        print(self.final_states)
        print(self.transitions)
        """

    def checkToken(self, token):
        currentState = self.initial_state
        for letter in token:
            if letter not in self.alphabet:
                return False
            foundTransition = False
            for transition in self.transitions:
                if transition[0] == currentState and transition[1] == letter:
                    currentState = transition[2]
                    foundTransition = True
            if foundTransition == False:
                return False
        if currentState in self.final_states:
            return True
        return False

    def menu(self):
        print("Finite Automata generated from file ", self.inputFileName)
        print("1. the set of states\n"
              "2. the alphabet\n"
              "3. all the transitions\n"
              "4. the initial state\n"
              "5. the set of final states\n"
              "6. verify if sequence accepted\n"
              "0. exit\n")
        command = int(input("command >> "))
        while command in range(1, 7):
            if command == 1:
                print(self.states)
            elif command == 2:
                print(self.alphabet)
            elif command == 3:
                print(self.transitions)
            elif command == 4:
                print(self.initial_state)
            elif command == 5:
                print(self.final_states)
            elif command == 6:
                sequence = input("insert sequence >> ")
                print(self.checkToken(sequence))
            command = int(input("command >> "))


# fa = FiniteAutomata(r"/Users/marcubale/Downloads/Formal-Languages-and-Compiler-Design-/Lab4/inputExample.txt")
# faNumbers = FiniteAutomata(r"/Users/marcubale/Downloads/Formal-Languages-and-Compiler-Design-/Lab4/constantFA.txt")
# faNumbers = FiniteAutomata(r"/Users/marcubale/Downloads/Formal-Languages-and-Compiler-Design-/Lab4/identifierFA.txt")
# fa.menu()
