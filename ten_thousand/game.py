from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic


roll_dice = GameLogic.roll_dice
points_calculate = GameLogic.calculate_score
validate_keepers = GameLogic.validate_keepers
get_scorers = GameLogic.get_scorers


def play(roller=GameLogic.roll_dice, num_rounds=10):
    """
    Starts a game of Ten Thousand.
    Args:
    - roller (function): the function that rolls the dice. Defaults to GameLogic.roll_dice.
    - num_rounds (int): the number of rounds to play. Defaults to 10.
    Returns:
    - None
    This function initializes a game of Ten Thousand, a dice game where players aim to score 10,000 points
    before their opponents. It prompts the user to either start the game or decline, and then begins the game
    by calling the start_game() function. The roller argument allows the caller to provide a custom function for
    rolling the dice. The default function is GameLogic.roll_dice.
    """

    global roll_dice
    roll_dice = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_res = input('> ')

    if user_res == "n":
        quitter()

    if user_res == 'y':
        print(f'Starting round 1')
        start_game(num_rounds)


def quitter():
    """
    Prints a quitting message to the console.
    Args:
    - None
    Returns:
    - None
    This function is called when the user declines to play the game by typing 'n' at the beginning of the program.
    It prints a message to the console indicating that the user has declined to play, and the program exits.
    """
    return print('OK. Maybe another time')


def start_game(num_rounds, round_num=1, total=0, number_dices=6, points=0):
    """
    Starts a round of the Ten Thousand game and prompts the player to roll the dice.
    Args:
    - num_rounds (int): the total number of rounds to play.
    - round_num (int): the current round number. Defaults to 1.
    - total (int): the total score accumulated so far. Defaults to 0.
    - number_dices (int): the number of dice to roll. Defaults to 6.
    - points (int): the total number of unbanked points. Defaults to 0.
    Returns:
    - None
    This function starts a round of the Ten Thousand game by rolling a specified number of dice and prompting
    the player to choose which dice to keep. It performs various error checks, such as testing for "zilch"
    rounds (where no points are earned), and checking that the player does not cheat by keeping more dice than
    they actually rolled. It also allows the player to choose whether to continue rolling, bank their points,
    or quit the game. The function is called recursively until all rounds are completed or the player quits.
    """

    user_choice = ''
    first_roll = roll_dice(number_dices)
    unpacked_tuple = ''

    for i in first_roll:
        unpacked_tuple += str(i)+' '
    print(f'Rolling {number_dices} dice...')
    print("*** "+unpacked_tuple.strip()+' ***')

    # zilch test
    if points_calculate(first_roll) == 0:
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")
        print(f"You banked 0 points in round {round_num}")
        print(f"Total score is {total} points")

        if round_num == num_rounds:
            return end_game(total)

        round_num += 1
        points = 0
        print(f'Starting round {round_num}')

        return start_game(num_rounds, round_num, total, number_dices=6)

    print("Enter dice to keep, or (q)uit:")
    user_choice = input('> ').replace(' ', '')

    if user_choice == "q":
        end_game(total)
    else:
        dice_to_keep = tuple(int(x) for x in user_choice)
        cheat_test = validate_keepers(first_roll, dice_to_keep)
        check_hot_dice = get_scorers(dice_to_keep)

        if len(check_hot_dice) == 6:
            points += points_calculate(dice_to_keep)

        while not cheat_test:
            print("""Cheater!!! Or possibly made a typo...""")
            print("*** "+unpacked_tuple.strip()+' ***')
            print("Enter dice to keep, or (q)uit:")
            user_choice = input('> ').replace(' ', '')

            if user_choice == "q":
                return end_game(total)

            else:
                dice_to_keep = tuple(int(x) for x in user_choice)
                cheat_test = validate_keepers(first_roll, dice_to_keep)

        if len(dice_to_keep) != 6:
            number_dices = number_dices - len(dice_to_keep)
            points += points_calculate(dice_to_keep)

        print(
            f"You have {points} unbanked points and {number_dices} dice remaining")
        print("(r)oll again, (b)ank your points or (q)uit:")
        user_choice = input('> ')

        if user_choice == 'q':
            end_game(total)

        elif user_choice == 'r':

            if number_dices > 0:
                start_game(num_rounds, round_num, total, number_dices, points)
            else:
                print(
                    'you ran out of dices new round will start\n you didnt bank yor points so you lost them')
                round_num += 1
                start_game(num_rounds, round_num, total, number_dices=6)

        elif user_choice == "b":
            bank_points(num_rounds, points, round_num, total)


def bank_points(num_rounds, points, round_num, total):
    """
    Banks the points that the user has accumulated in a given round.
    Parameters:
    -----------
    num_rounds : int
        The total number of rounds to be played.
    points : int
        The number of points to be banked in the current round.
    round_num : int
        The current round number.
    total : int
        The total number of points accumulated so far.
    Returns:
    --------
    None
    """

    total = total + points
    print(f"You banked {points} points in round {round_num}")
    print(f"Total score is {total} points")

    if round_num == num_rounds:
        return end_game(total)

    round_num += 1
    print(f'Starting round {round_num}')
    start_game(num_rounds, round_num, total)


def end_game(total):
    """
    Prints a message to indicate the end of the game and the total points earned.
    Parameters:
    -----------
    total : int
        The total number of points earned during the game.
    Returns:
    --------
    None
    """
    print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    play()