#!python3

"""
Write a python script display the values of the dictionary
  1. that are sorted by their keys (ascending values) 
  2. that are sorted by their values (ascending) 
  
(3 points)
"""
sortMe = {1: -2, 2: 6, 4: 0, 6: 1, 9: 2, 10: 3, 11: 0, 13: 3, 14: 4, 15: -2, 17: 0, 18: -1, 20: 3}

sort_key = dict(sorted(sortMe.items()))

sort_values = dict(sorted(sortMe.items(), key = lambda item: item[1]))

print("Sorted by keys (ascending values:)")
for key, value in sort_key.items():
    print(f"{key}: {value}")

print("\nSorted by values (ascending): ")
for key, value in sort_values.items():
    print(f"{key}: {value}")