from time import sleep
from random import uniform, randint

def roll(dice, repeat):
    total = 0
    for i in range(repeat):
        total += randint(1, dice)
    
    return total

def typing(text):
    for letter in text:
        print(letter, end="", flush=True)
        sleep(uniform(0.05,0.070))

def wait_dot(seconds=0.3, cycle=1):
    for i in range(cycle):
        sleep(seconds)
        print(".")
    