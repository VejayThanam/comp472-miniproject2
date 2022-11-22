# Define Car class
class Car:
    def __init__(self, i, j, L, horiz, letter, fuel):
        self.row = i  # parameter i (int) = row of car
        self.col = j  # parameter j (int) = column of car
        self.length = L  # parameter L (int) = length of car
        self.horiz = horiz # parameter horiz (boolean) -> True if car is moving honizontal
        self.letter = letter # paramater letter for letter of the car
        self.fuel = fuel

    def print_car(self):
        print('row:', self.row)
        print('col:', self.col)
        print('length:', self.length)
        print('horizontal:', self.horiz)
        print('letter:', self.letter)
        print('fuel:', self.fuel)