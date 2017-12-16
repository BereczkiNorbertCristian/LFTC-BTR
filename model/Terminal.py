class Terminal(object):
    def __init__(self, character):
        self.c = character

    def __str__(self):
        return self.c

    def __eq__(self, other):
        return self.c == other.c

    def isTerminal(self):
        return True

    def isNonTerminal(self):
        return False

    def __hash__(self) -> int:
        return hash(self.c)
