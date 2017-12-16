class Util:
    @staticmethod
    def containsNonTerminal(nonTerminal, expression):
        for x in expression:
            if x.c == nonTerminal:
                return True
        return False

    @staticmethod
    def indexOfNonTerminal(nonTerminal, expression):
        for x in range(len(expression)):
            if expression[x].c == nonTerminal:
                return x
        return -1

    @staticmethod
    def indexOfItem(item, items):
        for i in range(len(items)):
            if items[i] == item:
                return i
        return -1