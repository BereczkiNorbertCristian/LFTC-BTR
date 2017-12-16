class CanonicalExpression:
    def __init__(self, leftPart, rightPart, dotPosition, prediction):
        self.leftPart = leftPart
        self.rightPart = rightPart
        self.dotPosition = dotPosition
        self.prediction = prediction

    def getElementBeforeDot(self):
        return self.rightPart[self.dotPosition]

    def __eq__(self, other):
        return self.leftPart == other.leftPart \
               and self.rightPart == other.rightPart \
               and self.prediction == other.prediction \
               and self.dotPosition == other.dotPosition

    def __str__(self):
        res = ""
        res += self.leftPart + "->"
        for x in range(len(self.rightPart)):
            if self.dotPosition == x:
                res += "."
            res += self.rightPart[x].c
        if self.dotPosition == len(self.rightPart):
            res+="."
        res += ", " + self.prediction.c
        return res
