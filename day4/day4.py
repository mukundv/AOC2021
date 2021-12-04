import inspect


def get_lists(input_file_name):
    with open(input_file_name, 'r') as f:
        line = f.read().split('\n\n')
        draw_numbers = [int(x) for x in line[0].split(',')]
        boards = [[[int(n) for n in r.split()]
                   for r in line[i].strip('\n').split('\n')]
                  for i in range(1, len(line))]
        return draw_numbers, boards


# Part 1
def get_winning_number(draw_numbers, boards):
    function_name = inspect.getframeinfo(inspect.currentframe()).function  # get name of function. Useful in prints
    for number in draw_numbers:  # loop through the draws
        for board in boards:  # for all the boards
            for x, y in enumerate(board):  # first list
                for a, b in enumerate(y):
                    if b == number:
                        board[x][a] = 0  # Mark the co-ordinates in the board as 0
            for y in board:
                if all(i == 0 for i in y):
                    score_sum = sum(x for j in board for x in j if x > 0)  # Sum up all the numbers in the
                    # board (5X5) that are > 0
                    print(f'{function_name}: Score Sum is {score_sum}')
                    print(
                        f'{function_name}: Final Score = Score Sum ({score_sum}) * Number ({number}) = {score_sum * number}')
                    return score_sum * number  # Winning Number is score * number that completed the


# Part 2
def get_last_winning_board_score(draw_numbers, boards):
    function_name = inspect.getframeinfo(inspect.currentframe()).function
    winning_board = []
    win = None

    for number in draw_numbers:
        if sum(i not in winning_board for i in boards) == 1:
            win = next(j for j, i in enumerate(boards) if i not in winning_board)  # Return next item from iterator
        for x, board in enumerate(boards):
            for i, board_row in enumerate(board):
                for a, board_number in enumerate(board_row):
                    if board_number == number:
                        board[i][a] = 0
            for column in zip(*board):
                if all(k == 0 for k in column):
                    if x == win:
                        score_sum = sum(i for r in board for i in r if i > 0)
                        print(f'{function_name}:  Score Sum is {score_sum}')
                        print(
                            f'{function_name}:  Score Sum ({score_sum}) * Number ({number}) = {score_sum * number}')
                        return score_sum * number
                    winning_board.append(board)
            for board_row in board:
                if all(b == 0 for b in board_row):
                    if x == win:
                        score_sum = sum(i for j in board for i in j if i > 0)
                        print(f'{function_name}: Score Sum is {score_sum}')
                        print(
                            f'{function_name}: Score Sum ({score_sum}) * Number ({number}) = {score_sum * number}')
                        return score_sum * number
                    winning_board.append(board)


if __name__ == '__main__':
    print(f'Part 1: Winning Number: {get_winning_number(*get_lists("day4_input.txt"))}')
    print(f'Part 2: Winning Number: {get_last_winning_board_score(*get_lists("day4_input.txt"))}')
