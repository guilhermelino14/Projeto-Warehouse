class Pair:
    def __init__(self, cell1, cell2):
        self.cell1 = cell1
        self.cell2 = cell2
        self.value = 0
        self.cells = []
        self.steps = 0
        # abs(cell1.line - cell2.line) + abs(cell1.column - cell2.column)
        # TOD0

    def hash(self):
        return str(self.cell1.line) + "_" + str(self.cell1.column) + "_" + str(
            self.cell2.line) + "_" + str(self.cell2.column)

    def __eq__(self, o: object) -> bool:
        return  (self.cell1 == o.cell1 and self.cell2 == o.cell2) or (self.cell1 == o.cell2 and self.cell2 == o.cell1)


    def __str__(self):
        return str(self.cell1.line) + "-" + str(self.cell1.column) + " / " + str(self.cell2.line) + "-" + str(self.cell2.column) + ": " + str(self.value) + "\n"

