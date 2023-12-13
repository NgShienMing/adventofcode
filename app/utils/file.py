def read_file_as_lines(filename):
    puzzle = []
    with open(filename) as f:
        puzzle = f.read().splitlines()

    return puzzle
