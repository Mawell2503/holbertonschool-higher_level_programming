#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    #  the count of numbers
    count = 0
    #  print up to x numbers,one at a time and skips numbers of different type
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count = count + 1
        except (ValueError, TypeError):
            continue
    print()
    return count
