import sys


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
        write([], out_name + ".out")
