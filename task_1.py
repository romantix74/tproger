#/usr/bin/env python3

"""
Выведите все элементы, которые меньше 5.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

# my solution
def sort_list(input_list: list) -> list:
    return [ i for i in input_list if i<5 ]

# tproger solution
print(list(filter(lambda elem: elem < 5, a)))
print([elem for elem in a if elem < 5])

if __name__ == "__main__":   
    print(sort_list(a))