class NonTerminal(object):
    def __init__(self, character):
        self.c = character

    def __str__(self):
        return self.c

    def isTerminal(self):
        return False

    def isNonTerminal(self):
        return True
