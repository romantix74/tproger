#/usr/bin/env python3

"""
Нужно вернуть список, который состоит из элементов, общих для этих двух списков.
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# my solution
def sort_shared_values(list_a: list, list_b: list) -> list:
    return [i for i in a if i in b]

# tproger solution
print([elem for elem in a if elem in b])
print(list(filter(lambda elem: elem in b, a)))
print(list(set(a) & set(b)))

if __name__ == "__main__":   
    print(sort_shared_values(a,b))