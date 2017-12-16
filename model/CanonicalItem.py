from model.CanonicalExpression import CanonicalExpression
from model.Terminal import Terminal
from model.Transition import Transition


class CanonicalItem:
    def __init__(self, identifier, initialExpressions, container, firstFollow):
        self.id = identifier
        self.expressions = initialExpressions
        self.container = container
        self.firstFollow = firstFollow
        self.next = []

    def expand(self):
        for expression in self.expressions:
            if expression.dotPosition < len(expression.rightPart) and expression.getElementBeforeDot().isNonTerminal():
                predictions = self.getPredictions(expression)
                crtElement = expression.getElementBeforeDot()
                for exp in self.container.getDict()[crtElement.c]:
                    for p in predictions:
                        newCanonicalExpression = CanonicalExpression(crtElement.c, exp, 0, p)
                        if not newCanonicalExpression in self.expressions:
                            self.expressions.append(newCanonicalExpression)

    def getPredictions(self, expression):
        predictions = [expression.prediction]
        if expression.dotPosition < len(expression.rightPart) - 1:
            nextElement = expression.rightPart[expression.dotPosition + 1]
            if nextElement.isNonTerminal():
                predictions = self.firstFollow.first[nextElement.c]
            else:
                predictions = [nextElement]
        return predictions

    def addNext(self, start, through, end):
        self.next.append(Transition(start, through, end))

    def __str__(self):
        res = ""
        res += "I" + str(self.id) + "\n"
        for e in self.expressions:
            res += str(e) + "\n"
        res += "next: "
        for n in self.next:
            res += str(n) + ", "
        res = res[:len(res) - 2]
        res += "\n\n"
        return res

    def __eq__(self, other):
        return self.expressions == other.expressions
