# maximum output joltage

import os
from helpers import load_input, split_data

input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp3.txt")
# input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp3_example.txt") # path to example file

def parse_bank_multiple (bank, battery_count):
    """
    boundary condition to find joltage (N batteries): last N batteries of the bank are ON
    we accomodate this by parsing only until the Nth battery from last when looking for batteries
    """
    joltage = 0
    i = battery_count
    curr_index = 0
    last_index = -1 * (battery_count - 1)
    bank_length = len(bank)

    while i > 0:
        max_digit = int(max(bank[:last_index])) # find the largest digit at lowest index
        curr_index = bank.index(max(bank [:last_index])) # store index of current largest number

        bank = bank [curr_index+1:]
        joltage = joltage * 10 + max_digit
        
        if last_index == -1: last_index = bank_length # handle when bank becomes bank [:0] ie empty string
        else: last_index += 1
        i -= 1

    return joltage

def go_through_banks (arr_str, battery_count):
    joltage = 0

    for bank in arr_str: 
        joltage += parse_bank_multiple(bank, battery_count)
    
    return joltage 

if __name__ == "__main__":

    arr_str = split_data(load_input(input_file), "\n")
    if arr_str:
        print ("Main: got the battery bank.\n")
    else: 
        print("Main: No battery banks found! Exiting")
        exit ()

    joltage_p1 = go_through_banks(arr_str, 2)
    joltage_p2 = go_through_banks(arr_str, 12)

    print(f"Main: (part 1) joltage when 2 batteries ON = {joltage_p1}")
    print(f"Main: (part 2) joltage when 12 batteries ON = {joltage_p2}")
