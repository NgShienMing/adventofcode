def read_file(filename):
    puzzle = []
    with open(filename) as f:
        puzzle = f.read().splitlines()

    return puzzle
