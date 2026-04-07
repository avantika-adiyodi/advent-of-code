# maximum output joltage

import os
from helpers import load_input, split_data

input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp3.txt")

def parse_bank (bank):
    """
    boundary condition to find battery: formed using the last 2 digits
    we accomodate this by parsing only until second last digit when looking for tens place digit
    """
    tens_idx = bank.index(max(bank[:-1]))

    battery_joltage = int(max(bank[:-1])) # look for largest digit from beginning till second last digit
    battery_joltage = battery_joltage*10 + int(max(bank[tens_idx + 1:])) # find the largest digit after the first largest digit
    return battery_joltage

def go_through_banks (arr_str):
    joltage = 0
    for bank in arr_str: joltage += parse_bank(bank)
    
    return joltage

if __name__ == "__main__":

    arr_str = split_data(load_input(input_file), "\n")
    if arr_str:
        print ("Main: got the battery bank.\n")
    else: 
        print("Main: No battery banks found! Exiting")
        exit ()

    joltage = go_through_banks(arr_str)
    print(f"Main: (part 1) final joltage is {joltage}")
