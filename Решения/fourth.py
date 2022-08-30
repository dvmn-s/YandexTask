coordinate = [int(i) for i in input().split()]
map = []
start = None


for i in range(coordinate[0]):
    new_row = list(input())
    map.append(new_row)
    if "S" in new_row:
        start = [i, new_row.index('S')]


def check_neighbours(dot):
    if map[dot[0]+1][dot[1]] == '.':
        map[dot[0] + 1][dot[1]] = 'D'
        check_neighbours([dot[0]+1, dot[1]])
    if map[dot[0] - 1][dot[1]] == '.':
        map[dot[0] - 1][dot[1]] = 'U'
        check_neighbours([dot[0] - 1, dot[1]])
    if map[dot[0]][dot[1] + 1] == '.':
        map[dot[0]][dot[1] + 1] = 'R'
        check_neighbours([dot[0], dot[1] + 1])
    if map[dot[0]][dot[1] - 1] == '.':
        map[dot[0]][dot[1] - 1] = 'L'
        check_neighbours([dot[0], dot[1] - 1])

check_neighbours(start)
for row in map:
    print(''.join(row))

