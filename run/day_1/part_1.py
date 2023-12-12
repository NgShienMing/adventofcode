puzzle = []
with open('run/day_1/part_1.txt') as f:
    puzzle = f.read().splitlines()

numbers = []
for text in puzzle:
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
