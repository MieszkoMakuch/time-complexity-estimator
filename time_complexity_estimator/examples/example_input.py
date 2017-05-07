import random


def test_cleaner():
    print("Cleaning now..")


def first_element(l):
    if len(l) == 0:
        return None
    else:
        return l[0]


def first_element_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def find_max(x):
    max_ = 0
    for el in x:
        if el > max_:
            max_ = el
    return max_


def find_max_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def sorted_wrapper(lst):
    return sorted(lst)


def sorted_wrapper_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def insert_0(lst):
    lst.insert(0, 0)


def insert_0_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def bubble_sort(lst):
    l = lst[:]  # create a copy of lst
    n = len(l)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, n):
            if l[i - 1] > l[i]:
                l[i], l[i - 1] = l[i - 1:i + 1]
                swapped = True
    return l


def bubble_sort_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]


def cubic_function(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                # Operation with constant complexity.
                8282828 * 2322


def cubic_function_initializer(n):
    return n


def permute(lst):
    tot_list = []
    if len(lst) == 1:
        return [lst]
    for permutation in permute(lst[1:]):
        for i in range(len(lst)):
            tot_list.append(permutation[:i] + lst[0:1] + permutation[i:])
    return tot_list


def permute_initializer(n):
    return [random.randint(-10000, 10000) for _ in range(n)]
