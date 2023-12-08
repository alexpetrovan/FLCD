class Grammar:
    def __init__(self, N, E, P, S):
        self._N = N
        self._E = E
        self._P = P
        self._S = S

    @staticmethod
    def _validate(N, E, P, S):
        if S not in N:
            return False
        for key in P.keys():
            if key not in N:
                return False
            for move in P[key]:
                for char in move.split(' '):
                    if char not in N and char not in E and char != 'E':
                        print(f"Problem in {key} and in {P[key]}. Char {char} not recognized !")
                        return False
        return True

    @staticmethod
    def parseLine(line):
        return [value.strip() for value in line.strip().split('=')[1].strip()[1:-1].strip().split(',')]

    @staticmethod
    def fromFile(fileName):
        with open(fileName, 'r') as file:
            N = Grammar.parseLine(file.readline())
            E = Grammar.parseLine(file.readline())
            S = file.readline().split('=')[1].strip()
            P = Grammar.parseRules(Grammar.parseLine(''.join([line for line in file])))

            if not Grammar._validate(N, E, P, S):
                raise Exception("Validation returned false.")

            return Grammar(N, E, P, S)

    @staticmethod
    def parseRules(rules):
        result = {}

        for rule in rules:
            # print(rule)
            lhs, rhs = rule.split('->')
            lhs = lhs.strip()
            rhs = [prod.strip() for prod in rhs.split("|")]
            result[lhs] = rhs

        return result

    def __str__(self):
        return 'Non-terminals = { ' + ', '.join(self._N) + ' }\n' \
               + 'Terminals = { ' + ', '.join(self._E) + ' }\n' \
               + 'Productions = {\n' + '\n '.join(f"{key} -> {value}" for key, value in self._P.items()) + '\n}\n' \
               + 'Starting Word = ' + str(self._S) + '\n'

grammar = Grammar.fromFile("g1.txt")
print(grammar)

grammar = Grammar.fromFile("g2.txt")
print(grammar)