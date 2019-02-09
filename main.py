def print_board(x, o):
    """
    build a bord of game that gets two lists x, o.
    :param x: list of numbers in range 0-8.
    :param o: another list of numbers in range 0-8.
    :return:
    """
    print_list = [' '] * 9
    for num in x:
        print_list[num] = 'x'
    for num in o:
        print_list[num] = 'o'

    print(print_list[0], '|', print_list[1], '|', print_list[2])
    print(print_list[3], '|', print_list[4], '|', print_list[5])
    print(print_list[6], '|', print_list[7], '|', print_list[8])


def check_input(user_in, x, o):
    """
    cheks if the input frome the user is a number or not. later the function chekes if the number is in range 0:8.
    Then if the number is not in one of the lists (x or o), the function adds the number into the list.
    :param user_in:
    :param x: a list of numbers.
    :param o: another list of numbers.
    :return: x.
    """
    try:
        num = int(user_in)
    except:
        print('wrong, must be a number')
        return x
    # checking if the input is a number between 0 and 8:
    if num not in range(0, 9):
        print('wrong: num must be between 0 and 8')
        return x
    # checking if the number is in x or o:
    if num not in x and num not in o:
        x.append(num)
    else:
        print('choose another place')
    return x


def check_winning(x):
    """
    Check if the input list won
    :param x: list which contains the positions of player x
    :return: 'yes' if the player won, 'tie' if game over and no one wins. 'no if game continue.
    """
    the_winer = 'no'

    for i in [0, 3, 6]:
        if i + 0 in x and i + 1 in x and i + 2 in x:
            the_winer = 'yes'
            return the_winer

    for i in [0, 1, 2]:
        if i + 0 in x and i + 3 in x and i + 6 in x:
            the_winer = 'yes'
            return the_winer
    if 0 in x and 4 in x and 8 in x or 2 in x and 4 in x and 6 in x:
        the_winer = 'yes'
        return the_winer
    if len(x) > 4:
        the_winer = 'tie'
        return the_winer

    return 'no'


def computer_move(x, o):
    """
    checks the move of the other player, the computer.
    :param x:  list which contains the positions of player x
    :param o:  list which contains the positions of player o, if the number is not in x the function
     adds this number io o list.
    :return: o, the computers move.
    """
    for j in range(0,8):
       if j not in x and j not in o:
           o.append(j)
           break
    return o

x = []
o = []

while True:

    # checking if the input is good.
    # if not the length is the same, so ask from the user for another input:
    input_user = input('enter a number')
    len_originle = len(x)
    x = check_input(input_user, x, o)
    if len_originle == len(x):
        continue
    print_board(x, o)
    result = check_winning(x)
    if result is 'yes':
        print('the winner is: x ')
        break
    elif result is 'tie':
        print('game over - tie')
        break

    #if x did not win, o is playing and checking if o win:
    o = computer_move(x,o)
    print('compuer move')
    print_board(x, o)
    result = check_winning(o)
    if result is 'yes':
        print('the winner is: o ')
        break
    elif result is 'tie':
        print('game over - tie')
        break


