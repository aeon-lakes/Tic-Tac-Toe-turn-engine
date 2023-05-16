# Tic-Tac-Toe game grid

player = 'X'

play_state = '         '

result = 'Game not finished'

# Draws grid state of play

def grid_state(s):
    print('---------')
    for i in range(0, len(s), 3):
        print('| ' + ' '.join(s[i:i+3]) + ' |')
    print('---------')

# Analyses grid state

def analyse(p):
    x_wins = False
    o_wins = False

    x = p.count('X')
    o = p.count('O')
    if abs(x - o) > 1:
        result = 'Impossible'
        return result

    grid = [p[i:i+3] for i in range(0, len(p), 3)] # rows
    grid += [p[i::3] for i in range(3)] # columns
    grid.append(''.join([p[i] for i in [0, 4, 8]])) # 1st diagonal
    grid.append(''.join([p[i] for i in [2, 4, 6]])) # 2nd diagonal

    x_wins = any('XXX' in s for s in grid)
    o_wins = any('OOO' in s for s in grid)

    if x_wins and o_wins == True:
        result = 'Impossible'
    elif not x_wins and o_wins:
        result = 'O wins'
    elif x_wins and not o_wins:
        result = 'X wins'
    elif not x_wins and not o_wins and 9 - (x + o) > 0:
        result = 'Game not finished'
    else:
        result = 'Draw'
    return result

#
def turn(ps, xo):

    x = ''
    y = ''

    print(xo)

    while True:

        pos = input(f'Input coordinates to place your token\nPlayer {xo}:')
        pos = pos.replace(" ", "")  # remove spaces if any

        try:
            x, y = map(int, list(pos))
        except ValueError:
            print('You should enter numbers!')
            continue

        if x not in (1, 2, 3) or y not in (1, 2, 3):
            print('Coordinates should be from 1 to 3!')
            continue

        index = (x - 1) * 3 + (y - 1)

        if (ps[index]) in ('O', 'X'):
            print('This cell is occupied!')
            continue

        break

    ps_list = list(ps)
    ps_list[index] = xo
    ps = ''.join(ps_list)

    if xo == 'X':
        xo = 'O'
    else:
        xo = 'X'
    print(xo)

    return ps, xo


grid_state(play_state)

while result == 'Game not finished':

    play_state, player = turn(play_state, player)  # separating ps and xy here
    grid_state(play_state)

    result = analyse(play_state)

    print(result)
