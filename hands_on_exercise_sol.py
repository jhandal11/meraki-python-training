"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi
print(pi)
print(type(pi))


# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)
if i < 50 or i > 50:
    print("i: ", i)

# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])
if picked_fruit == 'orange':
    print('orange', picked_fruit)
elif picked_fruit == 'strawberry':
    print('red', picked_fruit)
elif picked_fruit == 'banana':
    print('yellow', picked_fruit)
else:
    print('unknown color')

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiply(a,b):
    return a*b

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =",multiply(12,96))

print("48 x 17 =",multiply(48,17))

print("196523 x 87323 =",multiply(196523,87323))
