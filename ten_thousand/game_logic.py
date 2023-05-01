import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    def calculate_score(tup):
        """
        this function recives a tuple and calculate the unbanked points for a roll of dice depands on the game rule  
        """

        unbancked_points = 0
        num_counter = Counter(tup)

        if 1 == num_counter[5] or num_counter[5] == 2:
            unbancked_points += 50 * num_counter[5]
        if 1 == num_counter[1] or num_counter[1] == 2:
            unbancked_points += 100 * num_counter[1]
        # 3 of a kind
        if num_counter[1] == 3:
            unbancked_points += 1000
        if num_counter[2] == 3:
            unbancked_points += 200
        if num_counter[3] == 3:
            unbancked_points += 300
        if num_counter[4] == 3:
            unbancked_points += 400
        if num_counter[5] == 3:
            unbancked_points += 500
        if num_counter[6] == 3:
            unbancked_points += 600
        # 4 of a kind
        if num_counter[1] == 4:
            unbancked_points += 2000
        if num_counter[2] == 4:
            unbancked_points += 400
        if num_counter[3] == 4:
            unbancked_points += 600
        if num_counter[4] == 4:
            unbancked_points += 800
        if num_counter[5] == 4:
            unbancked_points += 1000
        if num_counter[6] == 4:
            unbancked_points += 1200
        # 5 of a kind
        if num_counter[1] == 5:
            unbancked_points += 4000
        if num_counter[2] == 5:
            unbancked_points += 800
        if num_counter[3] == 5:
            unbancked_points += 1200
        if num_counter[4] == 5:
            unbancked_points += 1600
        if num_counter[5] == 5:
            unbancked_points += 2000
        if num_counter[6] == 5:
            unbancked_points += 2400
        # 6 of a kind
        if num_counter[1] == 6:
            unbancked_points += 8000
        if num_counter[2] == 6:
            unbancked_points += 1600
        if num_counter[3] == 6:
            unbancked_points += 2400
        if num_counter[4] == 6:
            unbancked_points += 3200
        if num_counter[5] == 6:
            unbancked_points += 4000
        if num_counter[6] == 6:
            unbancked_points += 4800

        if len(num_counter) == 3 and len(set(num_counter.values())) == 1 and list(set(num_counter.values()))[0] == 2:
            unbancked_points = 1500

        if len(num_counter) == 2 and list(set(num_counter.values()))[0] == 3:
            unbancked_points = unbancked_points*2

        # stright 1-6
        if len(num_counter) == 6:
            unbancked_points = 2000
        return unbancked_points

    def roll_dice(int):
        """
        this function recives an integar represents the number of dice we use to roll and gives back a random numbers between 1-6 depands on the int given  
        """
        list = []
        for i in range(int):
            x = random.randint(1, 6)
            list.append(x)
        return tuple(list)

    def validate_keepers(tup1, tup2):
        """this function will take two tuples and check if the first tuple contain the value from the scond tuple with the same itarrtion"""
        to_test_cheater = list(tup1)
        for i in tup2:
            if i not in to_test_cheater:
                return False

            index = to_test_cheater.index(i)
            to_test_cheater.pop(index)
        return True

    def get_scorers(dice):
        """ this function will take a tuple and return a tuple contain the values that give a score """

        all_dice_score = GameLogic.calculate_score(dice)

        if all_dice_score == 0:
            return tuple()

        dice_with_score = []

        for i, val in enumerate(dice):
            sub_roll = dice[:i] + dice[i + 1:]
            sub_score = GameLogic.calculate_score(sub_roll)

            if sub_score != all_dice_score:
                dice_with_score.append(val)

        return tuple(dice_with_score)

    

        
        

        

        

        

