#!/usr/bin/python3
def safe_print_list(my_list=[], x = 0):
    #  initializing the number of elements that needs to be returned
    count = 0
    #  the equivalent in C is for (int i = 0; i < x; i++)
    for i in range(x):
        #  try this code
        try:
            print(my_list[i], end="")
            count += 1
        # if the try blok has an error jump to this blok
        except Exception:
            break
    print()
    return count