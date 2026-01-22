 #!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    #  check and sort a_dictionary then place it in sorted_keys
    sorted_keys = sorted(a_dictionary.keys())
    #  loop through sorted_keys
    for key in sorted_keys:
        #  print the sorted items
        print(f"{key}: {a_dictionary[key]}")
