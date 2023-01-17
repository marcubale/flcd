from Lab5.grammar import Grammar

from string import ascii_uppercase as auc

grammar_filename = "/Users/marcubale/Downloads/Formal-Languages-and-Compiler-Design-/Lab5/grammar7.txt"
grammar = Grammar(grammar_filename)

"""
FIRST
1) If x is terminal, then FIRST(x)={x}

2) If X→ ε is production, then add ε to FIRST(X)

3) If X is a non-terminal and X → PQR then FIRST(X)=FIRST(P)

   If FIRST(P) contains ε, then  

        FIRST(X) = (FIRST(P) – {ε}) U FIRST(QR)
"""

"""
FOLLOW
1) For Start symbol, place $ in FOLLOW(S)

2) If A→ α B, then FOLLOW(B) = FOLLOW(A)

3) If A→ α B β, then

  If ε not in FIRST(β),

       FOLLOW(B) = FIRST(β)

  else do,

       FOLLOW(B) = (FIRST(β)-{ε}) U FOLLOW(A)
"""


def reunit(list1, list2):
    result = []
    for elem in list1:
        if elem not in result:
            result.append(elem)
    for elem in list2:
        if elem not in result:
            result.append(elem)
    return result


def first(grammar, symbol):
    result = []
    if symbol in grammar.terminals:
        return [symbol]
    if symbol == '#':
        return [symbol]
    for production in grammar.productions[symbol]:
        toateContinDiez = True
        for i in range(len(production)):
            aux = first(grammar, production[i])
            if '#' not in aux:
                toateContinDiez = False
                result = reunit(result, aux)
                break
            else:
                aux.remove('#')
                result = reunit(result, aux)
        if toateContinDiez:
            result.append('#')
    return result


def follow(grammar, symbol):
    result = []
    if symbol == grammar.starting_symbol:
        return ['$']
    for leftProd in grammar.productions:
        for rightProd in grammar.productions[leftProd]:
            if symbol in rightProd:
                # print(leftProd + " -> " + rightProd)
                symbolIndex = rightProd.find(symbol)
                toateContinDiez = True
                for i in range(symbolIndex + 1, len(rightProd)):
                    aux = first(grammar, rightProd[i])
                    if '#' not in aux:
                        result = reunit(result, aux)
                        toateContinDiez = False
                        break
                    else:
                        aux.remove('#')
                        result = reunit(result, aux)
                if toateContinDiez:
                    aux2 = follow(grammar, leftProd)
                    result = reunit(result, aux2)
    return result


def new_available_letter(grammar):
    for letter in auc:
        if letter not in grammar.non_terminals:
            return letter


def eliminate_left_recursion(grammar):
    changed = False
    for leftProd in grammar.productions:
        for rightProd in grammar.productions[leftProd]:
            if rightProd[0] == leftProd:
                for prod in grammar.productions[leftProd]:
                    if prod[0] != leftProd:
                        newSymbol = new_available_letter(grammar)
                        grammar.non_terminals.append(newSymbol)
                        auxList = grammar.productions[leftProd]
                        auxList.remove(rightProd)
                        auxList.remove(prod)
                        grammar.productions[leftProd] = reunit(auxList, [prod + newSymbol])
                        grammar.productions[newSymbol] = [rightProd[1:] + newSymbol, '#']
                        changed = True
                        break
            if changed:
                break
        if changed:
            break
    return changed


def eliminate_all_left_recursions(grammar):
    while eliminate_left_recursion(grammar):
        pass


def print_parse_table(grammar, parse_table):
    top_column = [' '] + grammar.terminals + ['$']
    last_pair = ('&', '&')
    for elem in top_column:
        print(elem, end='   ')
    for pair in parse_table:
        if pair[0] != last_pair[0]:
            print('\n' + pair[0] + ': ', end='')
        last_pair = pair
        print(parse_table[pair], end=' ')


def construct_parse_table(grammar):
    parse_table = {}
    # initialize table with None on all positions
    for non_terminal in grammar.non_terminals:
        for terminal in grammar.terminals:
            parse_table[(non_terminal, terminal)] = None
        parse_table[(non_terminal, '$')] = None
    for leftProd in grammar.productions:
        firstOfLeftProd = first(grammar, leftProd)
        counter = 0
        for rightProd in grammar.productions[leftProd]:
            if firstOfLeftProd[counter] in grammar.terminals:
                parse_table[(leftProd, firstOfLeftProd[counter])] = rightProd
            else:
                # followOfLeftProd = follow(grammar, leftProd)
                # for followSym in followOfLeftProd:
                parse_table[(leftProd, '$')] = rightProd
            counter += 1
    return parse_table

parse_tbl = construct_parse_table(grammar)
print_parse_table(grammar, parse_tbl)


"""
print(grammar.productions)
eliminate_left_recursion(grammar)
print(grammar.productions)
eliminate_left_recursion(grammar)
print(grammar.productions)
eliminate_left_recursion(grammar)
print(grammar.productions)
"""

"""
for symbol in grammar.non_terminals:
    print(symbol + ' : ', first(grammar, symbol))
print(" === ")
for symbol in grammar.non_terminals:
    print(symbol + ' : ', follow(grammar, symbol))
"""
