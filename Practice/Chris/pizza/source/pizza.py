import sys


ingredients = 2


class Cell:
    def __init__(self, x, y, i):
        self.x = x
        self.y = y
        self.i = i


# Represents a slice of a pizza
class Slice:
    def __init__(self):
        self.cells = []
        self.ingredients = []

    def addCell(self, cell):
        self.cells.append(cell)
        self.ingredients.append(cell.i)

    def getUL(self):
        if len(self.cells) > 0:
            m = min(self.cells)
            return m.x, m.y
        else:
            return -1, -1

    def getLR(self):
        if len(self.cells) > 0:
            m = max(self.cells)
            return m.x, m.y
        else:
            return -1, -1

    def getDimension(self):
        ul = self.getUL()
        lr = self.getLR()
        return [ul[0], ul[1], lr[0], lr[1]]


# Creates all possible constellations of slices
class SliceOptions:
    def __init__(self, dataset, mi, mc, x, y):
        self.mc = mc
        self.mi = mi
        self.options = sliceOptions(mi, mc)
        self.slices = [] * len(self.options)
        self.optimal_slice = []
        max_height = len(dataset)
        max_length = len(dataset[0])

        for option in self.options:
            slice_option = Slice()
            for _y in range(y, min(option[1], max_height - y)):
                for _x in range(x, min(option[0], max_length - x)):
                    slice_option.addCell(Cell(_x, _y, dataset[_y][_x]))
            self.slices.append(slice_option)

        self.optimal_slice = self.calcOptimalSlice()
        ul = self.optimal_slice.getUL()
        lr = self.optimal_slice.getLR()

        # erase cells in dataset
        for _y in range(ul[1], lr[1]):
            for _x in range(ul[0], lr[0]):
                dataset[_y][_x] = 0

    # Calculates slices with maximum slices
    def calcOptimalSlice(self):
        max_size = 0
        opt_slice = Slice()
        for slice_option in self.slices:
            if slice_option.ingredients.count('M') > 0 and slice_option.ingredients.count('T') > 0:
                if len(slice_option.cells) > max_size:
                    max_size = len(slice_option.cells)
                    opt_slice = slice_option

        return opt_slice

    # Calculates slices with minimal size
    # def calcOptimalSlice(self):
    #     min_size = self.mc
    #     opt_slice = Slice()
    #     for slice_option in self.slices:
    #         if slice_option.ingredients.count('M') > 0 and slice_option.ingredients.count('T') > 0:
    #             if len(slice_option.cells) < min_size:
    #                 min_size = len(slice_option.cells)
    #                 opt_slice = slice_option
    #
    #     return opt_slice

    def getOptSlice(self):
        return self.optimal_slice


# Returns the optimal options of slice sizes
def sliceOptions(ing, mc):
    options = []
    for x in range(1, mc + 1):
        for y in range(1, mc + 1):
            if ing <= x * y <= mc:
                options.append((x, y))

    return options


# Returns the optimal cells as list
def solve(rows, cells, mi, mc, dataset):
    slices = []

    for y, _ in enumerate(dataset):
        for x, _ in enumerate(dataset[y]):
            print(x, y)
            if dataset[y][x] != 0:
                slice_options = SliceOptions(dataset, ingredients, int(mc), x, y)
                opt_slice = slice_options.getOptSlice()
                dimension = opt_slice.getDimension()
                if dimension != [-1, -1, -1, -1]:
                    slices.append(" ".join(map(str, dimension)))
                # lr = opt_slice.getLR()
                # x += lr[0]
                # y += lr[1]

    return slices


def write(result, out):
    with open(out, "w+") as handle:
        handle.write(str(len(result)) + "\n")
        handle.writelines("\n".join(result))


if __name__ == "__main__":

    file_contents = {}
    scenario = {}

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            file_contents = file.readlines()

        info = file_contents[0].split(' ')
        data = []
        for r in range(1, len(file_contents)):
            data.append(list(file_contents[r][:-1]))
        out_name = sys.argv[1].split('/')[-1].split(".")[0]
        write(solve(info[0], info[1], int(info[2]), int(info[3]), data), out_name + ".out")
