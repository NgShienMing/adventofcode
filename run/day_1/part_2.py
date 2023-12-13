from app.utils.file import read_file_as_lines

puzzles = read_file_as_lines('run/day_1/input.txt')
valid_num_str = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

numbers = []
for text in puzzles:
    num = ''

    curr_num_list = []
    num_str = ''
    for i in range(len(text)):
        num_str = ''
        for j in range(i, len(text)):
            if j == i:
                try:
                    curr_num_list.append(text[j])
                    int(text[j])
                except Exception as e:
                    curr_num_list = curr_num_list[:-1]

                if len(curr_num_list) != 0:
                    num += text[j]
                    break

            num_str += text[j]
            if num_str in valid_num_str:
                num += str(valid_num_str.index(num_str) + 1)
                break

        if num_str in valid_num_str or len(curr_num_list) != 0:
            break


    curr_num_list = []
    num_str = ''
    for i in range(len(text)-1, -1, -1):
        num_str = ''
        for j in range(i, -1, -1):
            if j == i:
                try:
                    curr_num_list.append(text[j])
                    int(text[j])
                except Exception as e:
                    curr_num_list = curr_num_list[:-1]

                if len(curr_num_list) != 0:
                    num += curr_num_list[0]
                    break

            num_str = text[j] + num_str
            if num_str in valid_num_str:
                num += str(valid_num_str.index(num_str) + 1)
                break

        if num_str in valid_num_str or (len(curr_num_list) != 0 and len(num) == 2):
            break


    numbers.append(int(num))


print(sum(numbers))
