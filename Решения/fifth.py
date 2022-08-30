with open('input.txt', 'r', encoding='utf-8-sig') as f:
    primer = f.read()

open_breakets = []
close_breakets = []



def get_deleting_breakets():
    count = 0
    for index, value in enumerate(primer):
        if '(' == value:
            open_breakets.append(index)
            count += 1
        if ')' == value:
            close_breakets.append(index)
            count -= 1
        if count == -2:
            return -1

    if count == 1 and primer[0] != ')' :
        return open_breakets[0] + 1
    if count == -1:
        return close_breakets[0] + 1

    return -1



print(get_deleting_breakets())
