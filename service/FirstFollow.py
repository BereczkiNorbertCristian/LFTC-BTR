from model.Terminal import Terminal
from util.Util import Util


class FirstFollow:
    def __init__(self, container, initial):
        self.first = {}
        self.follow = {}
        self.initial = initial
        self.container = container
        self.__remainingNonTerminals = []
        self.firstAndFollow()

    def firstAndFollow(self):
        self.__remainingNonTerminals = self.container.getNonTerminals()
        while len(self.__remainingNonTerminals) > 0:
            self.findFirstByNonTerminal(self.__remainingNonTerminals[0])
        self.__remainingNonTerminals = self.container.getNonTerminals()
        while len(self.__remainingNonTerminals) > 0:
            self.findFollowByNonTerminal(self.__remainingNonTerminals[0])

    def findFirstByNonTerminal(self, nonTerminal):
        self.first[nonTerminal] = []
        for expression in self.container.getDict()[nonTerminal]:
            if expression[0].isTerminal():
                self.first[nonTerminal].append(expression[0])
            else:
                if not expression[0].c in self.first.keys():
                    self.findFirstByNonTerminal(expression[0].c)
                self.first[nonTerminal] += self.first[expression[0].c]
        self.first[nonTerminal] = list(set(self.first[nonTerminal]))
        self.__remainingNonTerminals.remove(nonTerminal)

    def findFollowByNonTerminal(self, nonTerminal):
        self.follow[nonTerminal] = []
        if nonTerminal == self.initial:
            self.follow[self.initial] = [Terminal("$")]
        for leftPart in self.container.getDict().keys():
            for expression in self.container.getDict()[leftPart]:
                if Util.containsNonTerminal(nonTerminal, expression):
                    if Util.indexOfNonTerminal(nonTerminal, expression) == len(expression) - 1:
                        if leftPart != nonTerminal:
                            if leftPart in self.__remainingNonTerminals:
                                self.findFollowByNonTerminal(leftPart)
                            self.follow[nonTerminal] += self.follow[leftPart]
                    else:
                        if expression[Util.indexOfNonTerminal(nonTerminal, expression) + 1].isTerminal():
                            self.follow[nonTerminal].append(expression[Util.indexOfNonTerminal(nonTerminal, expression) + 1])
                        else:
                            self.follow[nonTerminal] += self.first[expression[Util.indexOfNonTerminal(nonTerminal, expression) + 1].c]
        self.follow[nonTerminal] = list(set(self.follow[nonTerminal]))
        self.__remainingNonTerminals.remove(nonTerminal)

    def __str__(self):
        res = '{:15} | {:15} | {:15}\n'.format('', 'First', "Follow")
        for x in self.container.getNonTerminals():
            tmpResFirst = ""
            for t in self.first[x]:
                tmpResFirst += t.c + ", "
            tmpResFirst = tmpResFirst[:len(res)-2]
            tmpResFollow = ""
            for t in self.follow[x]:
                tmpResFollow += t.c + ", "
            tmpResFollow = tmpResFollow[:len(res)-2]
            res += "-" * 51 + "\n"
            res += '{:15} | {:15} | {:15}\n'.format(x, tmpResFirst, tmpResFollow)
        return res
