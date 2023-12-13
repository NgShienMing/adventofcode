from app.utils.file import read_file_as_lines

puzzles = read_file_as_lines('run/day_2/input.txt')
max_cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

valid_game_id = []
for puzzle in puzzles:
    valid_flag = True
    id_and_cubes = puzzle.split(': ')
    game_id = id_and_cubes[0][5:]
    cubes = id_and_cubes[1].split('; ')
    for cubes_revealed in cubes:
        cubes_revealed = cubes_revealed.split(', ')
        for cube in cubes_revealed:
            amount_and_color = cube.split(' ')
            amount = amount_and_color[0]
            color = amount_and_color[1]
            curr_color_max_amount = max_cubes[color]
            if int(amount) > curr_color_max_amount and valid_flag:
                valid_flag = False
    if valid_flag:
        valid_game_id.append(int(game_id))

print(sum(valid_game_id))
