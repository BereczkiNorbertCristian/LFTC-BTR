from model.Container import Container


def get_file_content(filename):
    container = Container()
    with open(filename) as f:
        for line in f:
            left, right = line.split("->");
            right = right.rstrip("\n")
            container.addTuple(left, right)
    return container
