from model.Terminal import Terminal


class CheckingService:
    def __init__(self, canonicalItems, container):
        self.canonicalItems = canonicalItems
        self.container = container
        self.table = [[None for _ in range(len(self.container.getAllElements()) + 2)] for _ in
                      range(len(self.canonicalItems.items) + 1)]
        self.initTable()

    def initTable(self):
        el = self.container.getAllElements()
        el.append(Terminal("$"))
        for i in range(len(self.canonicalItems.items)):
            self.table[i + 1][0] = "I" + str(i)
        for i in range(len(el)):
            self.table[0][i + 1] = el[i]
        for i in range(1, len(self.canonicalItems.items) + 1):
            next = self.canonicalItems.items[i-1].next
            finalExps = self.canonicalItems.items[i-1].getAllFinalExpressions()
            for j in range(1, len(el) + 1):
                for n in next:
                    if el[j-1] == n.through:
                        self.table[i][j] = "s" + str(n.end)
                for e in finalExps:
                    if e.prediction == el[j-1]:
                        self.table[i][j] = "r" + str(self.container.findRuleIdBy(e.leftPart, e.rightPart))
        for i in range(len(self.canonicalItems.items) + 1):
            print()
            for j in range(len(el) + 1):
                print("{:7}".format(str(self.table[i][j])), end="")
