import os
import random
from time import sleep


def generate_sequence(difficulty):
    your_list = []
    for i in range(0, difficulty):
        your_list.append(random.randint(1, 101))

    return your_list


def get_list_from_user(difficulty):
    your_list = []
    for i in range(0, difficulty):
        num2 = input("Enter your choice:")
        your_list.append(int(num2))
    return your_list


def is_list_equal(array1, array2):
    if array1 == array2:
        return True
    else:
        return False


d = input("Please enter difficulty: ")
d = int(d)

a = generate_sequence(d)
print(a)
sleep(0.7)
os.system('clear')
b = get_list_from_user(d)

c = is_list_equal(a, b)

print(b)
print(c)
