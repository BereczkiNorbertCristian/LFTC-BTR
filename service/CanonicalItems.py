from model.CanonicalExpression import CanonicalExpression
from model.CanonicalItem import CanonicalItem
from model.Terminal import Terminal
from util.Util import Util


class CanonicalItems:
    def __init__(self, container, firstFollow):
        initialRule = container.getList()[0]
        self.container = container
        self.firstFollow = firstFollow
        self.items = [
            CanonicalItem(0, [CanonicalExpression(initialRule[0], initialRule[1], 0, Terminal('$'))], self.container,
                          self.firstFollow)]
        self.crtIdentifier = 0
        self.lastUsedIdentifier = 0
        self.start()

    def start(self):
        for item in self.items:
            item.expand()
            self.createNewItems(item)

    def createNewItems(self, item):
        expressionGroups = self.groupExpressions(item.expressions)
        for key in expressionGroups:
            newCanonicalExpressions = []
            for i in range(len(expressionGroups[key])):
                if expressionGroups[key][i].dotPosition < len(expressionGroups[key][i].rightPart):
                    newCanonicalExpressions.append(CanonicalExpression(expressionGroups[key][i].leftPart,
                                                                       expressionGroups[key][i].rightPart,
                                                                       expressionGroups[key][i].dotPosition + 1,
                                                                       expressionGroups[key][i].prediction))
            newCanonicalItem = CanonicalItem(self.lastUsedIdentifier + 1,
                                             newCanonicalExpressions,
                                             self.container,
                                             self.firstFollow)
            newCanonicalItem.expand()
            indexOfItem = Util.indexOfItem(newCanonicalItem, self.items)
            if indexOfItem == -1:
                self.lastUsedIdentifier += 1
                self.items.append(newCanonicalItem)
                item.addNext(item.id, expressionGroups[key][0].getElementBeforeDot(), self.lastUsedIdentifier)
            else:
                item.addNext(item.id, expressionGroups[key][0].getElementBeforeDot(),
                             self.items[self.items.index(newCanonicalItem)].id)

    def groupExpressions(self, expressions):
        groupedExpressions = {}
        for e in expressions:
            if e.dotPosition < len(e.rightPart):
                crtElement = e.getElementBeforeDot()
                if not crtElement.c in groupedExpressions.keys():
                    groupedExpressions[crtElement.c] = [e]
                else:
                    groupedExpressions[crtElement.c].append(e)
        return groupedExpressions


    def __str__(self):
        res = ""
        for i in self.items:
            res += str(i)
        return res
