from app.utils.file import read_file

puzzles = read_file('run/day_2/input.txt')

power = []
for puzzle in puzzles:
    id_and_cubes = puzzle.split(': ')
    game_id = id_and_cubes[0][5:]
    cubes = id_and_cubes[1].split('; ')
    min_cubes = {
        'red': 0,
        'green': 0,
        'blue': 0,
    }
    for cubes_revealed in cubes:
        cubes_revealed = cubes_revealed.split(', ')
        for cube in cubes_revealed:
            amount_and_color = cube.split(' ')
            amount = amount_and_color[0]
            color = amount_and_color[1]
            curr_color_min_amount = min_cubes[color]
            if int(amount) > curr_color_min_amount:
                min_cubes[color] = int(amount)
    power.append(min_cubes['red'] * min_cubes['green'] * min_cubes['blue'])

print(sum(power))
