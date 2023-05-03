import random
from collections import Counter


class GameLogic:
    def __init__(self):
        pass

    def calculate_score(tup):
        """
        Calculate the unbanked points for a roll of dice based on the game rules of Yahtzee.
        Parameters:
        tup (tuple): A tuple of integers representing the values of rolled dice.
        Returns:
        int: The total unbanked points earned for the roll.
        Yahtzee is a game where players roll five dice to achieve certain combinations of values for points. 
        This function determines the unbanked points earned for a given roll based on the following rules:
        - If there are one or two 5's rolled, the player earns 50 points per 5.
        - If there are one or two 1's rolled, the player earns 100 points per 1.
        - If there are three or more of any number rolled, the player earns the point value of that number multiplied by 100.
        - If there are four or more of any number rolled, the player earns double the point value.
        - If there are five or more of any number rolled, the player earns quadruple the point value.
        - If there are six of any number rolled, the player earns eight times the point value.
        - If there are two pairs, the player earns 1500 points.
        - If there is a straight (1,2,3,4,5 or 2,3,4,5,6), the player earns 2000 points.
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
        This function simulates the rolling of a specified number of dice and returns a tuple containing the resulting values. The values are randomly generated integers between 1 and 6, inclusive.
        Args:
        - num_dice (int): The number of dice to roll.
        Returns:
        - tuple: A tuple containing the resulting values of the rolled dice.
        """

        list = []

        for i in range(int):
            x = random.randint(1, 6)
            list.append(x)
        return tuple(list)

    def validate_keepers(tup1, tup2):
        """
        Check if the first tuple contains all values from the second tuple with the same iteration.
        Args:
            tup1 (tuple): The first tuple to check.
            tup2 (tuple): The second tuple to check.
        Returns:
            bool: True if tup1 contains all values from tup2 with the same iteration, False otherwise.
        """

        to_test_cheater = list(tup1)

        for i in tup2:
            if i not in to_test_cheater:
                return False

            index = to_test_cheater.index(i)
            to_test_cheater.pop(index)

        return True

    def get_scorers(dice):
        """
        Given a tuple of dice values, returns a tuple containing the subset of dice
        that contribute to the score. If the roll has no score, an empty tuple is returned.
        """

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