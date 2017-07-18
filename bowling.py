def score(game):
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] != '/':
            result += get_value(game[i])
        if frame < 10:
            if game[i] == '/':
                result += 10 - last
                result += get_value(game[i+1])
            elif game[i] == 'X' or game[i] == 'x':
                result += if_is_X(game[i+1], game[i+2])
        last = get_value(game[i])
        if in_first_half:
            in_first_half = False
        else:
            frame += 1
            in_first_half = True
        if game[i] == 'X' or game[i] == 'x':
            in_first_half = True
            frame += 1
    return result


def get_value(char):
    return_value = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return_10 = ['x', 'X', '/']
    if char in return_value:
        return int(char)
    elif char in return_10:
        return 10
    elif char == '-':
        return 0
    else:
        raise ValueError()


def if_is_X(plus_one, plus_two):
    result = get_value(plus_one)
    if plus_two == '/':
        result += 10 - get_value(plus_one)
    else:
        result += get_value(plus_two)
    return result
