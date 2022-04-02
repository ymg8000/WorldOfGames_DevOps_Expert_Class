import random


def generate_number(d1):
    d1 = random.randint(1, d1)
    print(d1)
    return d1


def get_guess_from_user(difficulty):
    num3 = input(f' Please input number between 1 and {difficulty}')
    return int(num3)


def compare_results(e, f):
    if e == f:
        return True
    else:
        return False


# def play():
a = input("Enter difficulty from 1-5 :")
a = int(a)
b = generate_number(a)
c = get_guess_from_user(a)
d = compare_results(b, c)
print(d)
