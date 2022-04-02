import random


class Game1:

    def __init__(self, difficulty, secret_number):
        self.difficulty = difficulty
        self.secret_number = secret_number

    @staticmethod
    def generate_number:
        a = random.randint(0, Game1.difficulty)
        return a



Game1.difficulty = 5
Game1.secret_number = 3

print(Game1.generate_number())
