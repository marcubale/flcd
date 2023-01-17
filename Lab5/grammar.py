class Grammar:
    def __init__(self, input_filename):
        self.input_filename = input_filename
        self.terminals = []
        self.non_terminals = []
        self.starting_symbol = ''
        self.productions = {}
        self.read_grammar()

    def read_grammar(self):
        f = open(self.input_filename)
        self.non_terminals = f.readline().strip().split()
        self.terminals = f.readline().strip().split()
        self.starting_symbol = f.readline().strip()
        for line in f.readlines():
            line = line.strip().split('->')
            left_hand_side = line[0].strip()
            right_hand_side = line[1].strip().split('|')
            self.productions[left_hand_side] = list()
            for production in right_hand_side:
                self.productions[left_hand_side].append(production.strip())

    def print_grammar(self):
        print("Grammar")
        print("Nonterminals: ")
        for elem in self.non_terminals:
            print(elem, end=' ')
        print("\nTerminals: ")
        for elem in self.terminals:
            print(elem, end=' ')
        print("\nStarting symbol: ", self.starting_symbol)
        print("Productions: ")
        for key, values in self.productions.items():
            print(key, " -> ", end='')
            for value in values:
                print(value, end=' ')
            print('\n')


grammar_filename = "/Users/marcubale/Downloads/Formal-Languages-and-Compiler-Design-/Lab5/grammar1.txt"
grammar = Grammar(grammar_filename)
# for key in grammar.productions.keys():
#    print(key)
