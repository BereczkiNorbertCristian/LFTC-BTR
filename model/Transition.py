class Transition:
    def __init__(self, start, through, end):
        self.start = start
        self.through = through
        self.end = end

    def __str__(self):
        return "(" + str(self.through) + ", I" + str(self.end) + ")"
