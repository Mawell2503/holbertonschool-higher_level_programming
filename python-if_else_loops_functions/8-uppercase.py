#!/usr/bin/python3
def uppercase(str):
    outcome = ""  # creates an empty string called outcome
    for x in str:  # for loop
        if ord(x) >= 97 and ord(x) <= 122:  # if loop
            outcome = outcome + chr(ord(x) - 32)  # converts lower to upper(-)
            # & converts ASCII to char
        else:
            outcome = outcome + x  # just adds the letter if its uppercase
    print("{}".format(outcome))  # prints
