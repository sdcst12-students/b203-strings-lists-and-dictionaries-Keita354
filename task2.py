#!python3

'''
use a for loop to iterate through all possible integers to find the factors of 24
'''
number = 24

print(f"Factors of {number}:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)