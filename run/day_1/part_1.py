from app.utils.file import read_file
puzzles = read_file('run/day_1/input.txt')


numbers = []
for text in puzzles:
    curr_num_list = []
    num = ''
    for char in text:
        try:
            curr_num_list.append(char)
            int(char)
        except Exception as e:
            curr_num_list = curr_num_list[:-1]
            continue
    num += curr_num_list[0] + curr_num_list[-1]
    numbers.append(int(num))

print(sum(numbers))
