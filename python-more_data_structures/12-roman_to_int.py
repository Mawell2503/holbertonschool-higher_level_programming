#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    if roman_string is None:
        return 0
    #  create a dictionanry
    values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    #  create result
    total = 0
    # loop through elements of roman_string
    for i in range(len(roman_string)):
        #  change element to its value
        current_value = values[roman_string[i]]
        #  check if current element isnt last
        if i + 1 < len(roman_string):
            #  check if current element isnt smaller than the next
            if current_value < values[roman_string[i + 1]]:
                #  if yes; subtract
                total -= current_value
            else:
                #  add
                total += current_value
        
        else:
            #  add
            total += current_value

    return total
