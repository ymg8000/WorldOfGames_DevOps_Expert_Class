def welcome(name):
    a = """ and welcome to the World of Games (WoG).
Here you can find many cool games to play
    """
    b = 'Hello ' + name + a

    return b 


def load_game():
    print("Please choose a game to play:")
    print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back")
    print("2. Guess Game - guess a number and see if you chose like the computer")
    print("3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

    num1 = input("Enter your choice:")

    return num1
