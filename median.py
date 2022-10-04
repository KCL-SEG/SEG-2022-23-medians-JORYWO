"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""
import math

while True:
    try:
        print("Enter a list of numbers separated by commas: ")
        numbers = [float(value) for value in input().split(",")]
    except ValueError:
        print("Some input could not be converted to a number!")
    else:
        break

numbers.sort()
if len(numbers) % 2 == 1:
    print(numbers[math.ceil(len(numbers) / 2 - 1)])
else: #number is odd
    # print(int(len(numbers) / 2 - 1))
    # print(int(len(numbers) / 2))
    print((numbers[int(len(numbers) / 2 - 1)] + numbers[int(len(numbers) / 2)]) / 2)
