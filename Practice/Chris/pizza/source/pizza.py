import sys


def searchIngredient(dataset, x, y, mi, mc):
    slice = []
    ingredients = (0, 0)
    for sx in range(x, x+mc):
        for sy in range(y, y+mc):
            if sx < x + sx and sy < y + sy and ingredients[0] >= mi and ingredients[1] >= mi and (1 <= len(slice) <= mc):
                slice.append((sx, sy))
    x1, y1 = min(slice)
    x2, y2 = max(slice)
    return [x1, y1, x2, y2]


def solve(rows, cells, mi, mc, dataset):
    slices = []
    for y, _ in enumerate(dataset):
        for x, _ in enumerate(dataset[y]):
            slices.append(" ".join(map(str, searchIngredient(dataset, x, y, int(mi), int(mc)))))
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
        write(solve(info[0], info[1], info[2], info[3], data), out_name + ".out")
