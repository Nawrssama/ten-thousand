from ten_thousand.game_logic import GameLogic
# from game_logic import GameLogic

roll_dice = GameLogic.roll_dice
points_calculate = GameLogic.calculate_score
validate_keepers = GameLogic.validate_keepers
get_scorers = GameLogic.get_scorers


def play(roller=GameLogic.roll_dice):
    """this function starts the game when called"""
    global roll_dice
    roll_dice = roller
    print("Welcome to Ten Thousand")
    print("(y)es to play or (n)o to decline")
    user_res = input('> ')
    if user_res == "n":
        quitter()
    if user_res == 'y':
        print(f'Starting round 1')
        start_game()


def quitter():
    """this function return a string  when the user type n in the beganing of runing this code"""
    return print('OK. Maybe another time')


def start_game(round_num=1, total=0, number_dices=6, points=0):
    """this function starts the rounds when the user type y to start the game"""

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
        round_num += 1
        points = 0
        print(f'Starting round {round_num}')
        return start_game(round_num, total, number_dices=6)

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
                start_game(round_num, total, number_dices, points)
            else:
                print(
                    'you ran out of dices new round will start\n you didnt bank yor points so you lost them')
                round_num += 1
                start_game(round_num, total, number_dices=6)
        elif user_choice == "b":
            bank_points(points, round_num, total)


def bank_points(points, round_num, total):
    """this function bank points when the user type b to store his point"""
    total = total + points
    print(f"You banked {points} points in round {round_num}")
    print(f"Total score is {total} points")
    round_num += 1
    print(f'Starting round {round_num}')

    start_game(round_num, total)


def end_game(total):
    """this function print a string when the player type q"""
    print(f"Thanks for playing. You earned {total} points")


if __name__ == "__main__":
    play()