import random
from collections import Counter

class GameLogic() :
    def __init__(self):
        pass

    

    def roll_dice(num_dice):
        """
        Simulates the roll of one or more six-sided dice.

        Parameters:
        num_dice (int): the number of dice to roll

        Returns:
        tuple: a tuple of `num_dice` random integers between 1 and 6, inclusive
         """
        
        r = tuple(random.randint(1,6) for _ in range(num_dice))
        # print(r)
        return r

    def calculate_score(tup):
        '''
        The calculate_score function takes in a tuple of integers representing the outcome of rolling several dice. It returns an integer representing the unbanked points that can be scored based on the outcome of the roll.
        
        '''
        unbanked_points = 0
        count_result = Counter(tup)
        # print(count_result.most_common())

        ###################### if dice roll was three pairs ######################


        # if len(count_result.most_common()) == 3 and count_result[2]==2 and count_result[3]==2 and count_result[6]==2 :
        #     unbanked_points = 1500
        
        #     return unbanked_points

        if len(count_result.most_common()) == 3 and all(count == 2 for _, count in count_result.most_common()):
            unbanked_points = 1500

            return unbanked_points


        ###################### if dice roll was Straight 1- 6 ######################

        if count_result[1]==1 and count_result[2]==1 and count_result[3]==1 and count_result[4]==1 and count_result [5]==1 and count_result[6]==1:
            unbanked_points = 2000
            return unbanked_points

        ###################### if dice roll was two of a pairs ######################

        # if len(count_result)==2 and len(set(count_result.values()))==1 and list(set(count_result.values()))[0]==3:
        #     unbanked_points = unbanked_points*2  

        

        ########################### ones ############################

        if count_result[1]==3:
            unbanked_points += 1000

        if count_result[1]==4:
            unbanked_points += 2000

        if count_result[1]==5:
            unbanked_points += 4000

        if count_result[1]==6:
            unbanked_points += 8000

        ######### if ones was 1 or 2
        if count_result[1] >=1 and count_result[1]<3:
            unbanked_points += 100*count_result[1]

        ########################### fives ############################

        if count_result[5]==3:
            unbanked_points += 500

        if count_result[5]==4:
            unbanked_points += 1000

        if count_result[5]==5:
            unbanked_points += 2000

        if count_result[5]==6:
            unbanked_points += 4000

        ######### if fives was 1 or 2
        if count_result[5] >=1 and count_result[5]<3:
            unbanked_points += 50*count_result[5]

        ########################### three of a kind ############################

        if count_result[2]==3:
            unbanked_points += 200

        if count_result[3]==3:
            unbanked_points += 300

        if count_result[4]==3:
            unbanked_points += 400

        if count_result[6]==3:
            unbanked_points += 600

        ########################### four of a kind ############################

        if count_result[2]==4:
            unbanked_points += 400

        if count_result[3]==4:
            unbanked_points += 600

        if count_result[4]==4:
            unbanked_points += 800

        if count_result[6]==4:
            unbanked_points += 1200

        ########################### five of a kind ############################

        if count_result[2]==5:
            unbanked_points += 800

        if count_result[3]==5:
            unbanked_points += 1200

        if count_result[4]==5:
            unbanked_points += 1600

        if count_result[6]==5:
            unbanked_points += 2400

        ########################### six of a kind ############################

        if count_result[2]==6:
            unbanked_points += 1600

        if count_result[3]==6:
            unbanked_points += 2400

        if count_result[4]==6:
            unbanked_points += 3200

        if count_result[6]==6:
            unbanked_points += 4800

        return unbanked_points

        
        

        

        

        

