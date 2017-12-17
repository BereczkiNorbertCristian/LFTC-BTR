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
            self.table[0][i + 1] = el[i].c
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

    def checkSequence(self, sequence):
        crtTransition = ""
        sequence.append("$")
        crtItem = 0
        stack = [["$", "0"], sequence, []]
        while crtTransition != None:
            try:
                elIndex = self.table[0].index(sequence[0])
            except:
                return False
            crtTransition = self.table[crtItem+1][elIndex]
            if crtTransition == "r0":
                return True
            if crtTransition[0] == "s":
                stack[0].append(sequence[0])
                stack[0].append(crtTransition[1:])
                sequence.pop(0)
                crtItem = int(crtTransition[1:])
            else:
                prodRule = int(crtTransition[1:])
                exp = self.container.getRuleById(prodRule)
                stack[0] = stack[0][:len(stack[0]) - 2*len(exp[1])]

                elIndex = self.table[0].index(exp[0])
                newItem = int(stack[0][len(stack[0]) - 1])
                nextAction = self.table[newItem + 1][elIndex]

                stack[0].append(exp[0])
                stack[0].append(str(nextAction[1:]))
                stack[2].append(prodRule)

                crtItem = int(nextAction[1:])
            print(stack)
        return False