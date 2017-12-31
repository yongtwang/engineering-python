# coin.py
# The class definition for a coin.
from random import randint
class Coin:
    def __init__(self):  # Initialization method
        self.side = 'Heads'  # Heads on top initially.

    def get_side(self):  # A function inside a class is called a method
        return self.side

    def toss(self):  # First parameter of any method is always self
        temp = randint(0, 1)  # Temporary variable
        if temp == 1:
            self.side = 'Heads'  # Instance variables remember the object state
                                 # Different from local function variables
        else:
            self.side = 'Tails'

    def set_side(self, side_str):
        self.side = side_str