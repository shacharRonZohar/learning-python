from util.basic import print_test, get_nums_from_user


# import os
# import sys
# sys.path.append(os.path.abspath("../util"))


def get_smallest(first_num, second_num, third_num):

    smallest = first_num

    if second_num < smallest and second_num < third_num:
        smallest = second_num
    elif third_num < smallest:
        smallest = third_num

    return smallest


# nums = get_nums_from_user(3)
# res = get_smallest(*nums)
# print(res)

# Tests


def run_tests():
    tests = [
        ["1,2,3", "1", get_smallest(1, 2, 3)],
        ["1,3,2", "1", get_smallest(1, 3, 2)],
        ["2,1,3", "1", get_smallest(2, 1, 3)],
        ["2,3,1", "1", get_smallest(2, 3, 1)],
        ["3,1,2", "1", get_smallest(3, 1, 2)],
        ["3,2,1", "1", get_smallest(3, 2, 1)],
        ["1,1,1", "1", get_smallest(1, 1, 1)],
        ["1,1,2", "1", get_smallest(1, 1, 2)],
        ["1,2,1", "1", get_smallest(1, 2, 1)],
        ["2,1,1", "1", get_smallest(2, 1, 1)],
        ["1,2,2", "1", get_smallest(1, 2, 2)],
        ["2,1,2", "1", get_smallest(2, 1, 2)],
        ["2,2,1", "1", get_smallest(2, 2, 1)],
        ["2,2,2", "2", get_smallest(2, 2, 2)]
    ]
    for test in tests:
        print_test(test[0], test[1], test[2])


run_tests()
