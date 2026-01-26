#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for index in range(list_length):
        try:
            #  divide elements of list1 and list2
            value = my_list_1[index] / my_list_2[index]
        #  error if list_length are not equal/ index doesnt exist
        except IndexError:
            print("out of range")
            value = 0
        #  error if lists have different types
        except TypeError:
            print("wrong type")
            value = 0
        #  error if divivsions cant be done
        except ZeroDivisionError:
            print("division by 0")
            value = 0
        #  add a value to result
        finally:
            result.append(value)
    return result
