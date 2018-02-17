import sys


def solve(rows, cells, mi, mc, dataset):
    for i, _ in enumerate(dataset):
        print(dataset[i])


if __name__ == "__main__":

    file_contents = {}
    scenario = {}

    if len(sys.argv) > 1:
        with open(sys.argv[1]) as file:
            file_contents = file.readlines()

        info = file_contents[0].split(' ')
        data = []
        for r in range(1, len(file_contents)):
            data.append(list(file_contents[r]))
        solve(info[0], info[1], info[2], info[3], data)
