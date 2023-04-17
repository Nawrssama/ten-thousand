# what i asked :

Handle rolling dice
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.

# what i get :

import random

class GameLogic:
    
    @staticmethod
    def roll_dice(num_dice):
        return tuple(random.randint(1, 6) for _ in range(num_dice))

# what i changed :

 def roll_dice(num_dice):
        """
        Simulates the roll of one or more six-sided dice.

        Parameters:
        num_dice (int): the number of dice to roll

        Returns:
        tuple: a tuple of `num_dice` random integers between 1 and 6, inclusive
         """
        
        r = tuple(random.randint(1,6) for _ in range(num_dice))
        print(r)
        return r


