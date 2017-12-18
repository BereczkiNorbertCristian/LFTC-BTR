from model.NonTerminal import NonTerminal
from model.Terminal import Terminal


class Container(object):

    def __init__(self):
        self.dict = {}
        self.lst = []
        self.FIRST_CHARACTER = 0

    def addTuple(self, left, right):
        rightLst = []
        for el in right:
            toAppend = None
            if el[self.FIRST_CHARACTER] == "'":
                toAppend = Terminal(el.strip("'"))
            else:
                toAppend = NonTerminal(el)
            rightLst.append(toAppend)
        if not left in self.dict.keys():
            self.dict[left] = []
        self.dict[left].append(rightLst)
        self.lst.append((left, rightLst))

    # expressionsForNonTerminal gives the list of expressions for a nonTermial
    # 	doesn't matter what you send as parameter either string or NonTermial
    def expressionsForNonTerminal(self, nonTerminal):
        key = None
        if isinstance(nonTerminal, str):
            key = nonTerminal
        if isinstance(nonTerminal, NonTerminal):
            key = nonTerminal.c
        return self.dict[key]

    # getDict returns a dict which has the following:
    # 	key (left non terminal) -> val (list of lists meaning a list of expressions)
    # 	for the given nonTerminal
    def getDict(self):
        return self.dict

    # getList returns a list of tuples of the form (nonTermial,expression)
    # 	expression if formed from terminals and non termials
    def getList(self):
        return self.lst

    def getNonTerminals(self):
        return list(set(self.getDict().keys()))

    def getAllElements(self):
        elements = []
        for x in self.getDict().keys():
            for exp in self.getDict()[x]:
                for el in exp:
                    if not el in elements:
                        elements.append(el)
        return elements

    def findRuleIdBy(self, leftPart, rightPart):
        for x in range(len(self.getList())):
            if self.getList()[x][0] == leftPart and self.getList()[x][1] == rightPart:
                return x

    def getRuleById(self, identifier):
        return self.getList()[identifier]

    @staticmethod
    def printList(lst):
        ret = "\nList:["
        for el in lst:
            tp = "None:"
            if el.isTerminal() :
                tp = "T:"
            else:
                tp = "NT:"
            ret += tp + el.c + ","
        ret += "]\n"
        return ret

    def __str__(self):
        ret = ""
        for k, lst in self.lst:
            ret += k + "->" + Container.printList(lst)
        ret += "Dict:{"
        for k in self.dict.keys():
            ret += "\n"
            ret += k + "->"
            val = self.dict[k]
            for lst in val:
                ret += Container.printList(lst)

        ret += "}\n"
        return ret
