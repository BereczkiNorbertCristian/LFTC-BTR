class Expression:
    @staticmethod
    def containsNonTerminal(nonTerminal, expression):
        for x in expression:
            if x.c == nonTerminal:
                return True
        return False

    @staticmethod
    def indexOf(nonTerminal, expression):
        for x in range(len(expression)):
            if expression[x].c == nonTerminal:
                return x
        return -1