# --- Day 3: Lobby ---
# maximum output joltage

import os
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp3.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp3_example.txt") # path to example file

def parse_bank (bank: str, battery_count: int) -> int:
    # Extract joltage from a single bank string

    """
    to find joltage with N batteries ON: 
    Boundary condition: last N batteries of the bank are ON
    we accomodate this by parsing only until the Nth battery from last when looking for batteries
    so we only search within bank[:-battery_count+1] for each digit we pick
    """
    joltage = 0
    remaining = battery_count
    # we search until the index: -(battery_count - 1) to accomodate the boundary condition
    curr_index = 0
    last_index = -(battery_count - 1)

    while remaining > 0:
        max_digit = max(bank[:last_index]) # find the largest digit at lowest index
        curr_index = bank.index(max_digit) # store index of current largest number

        bank = bank [curr_index + 1:]
        joltage = joltage * 10 + int(max_digit)
        
        if last_index == -1: 
            last_index = len(bank) # handle when bank becomes bank [:0] ie empty string
        else: 
            last_index += 1

        remaining -= 1

    return joltage

def go_through_banks (arr_str: list[str], battery_count: int) -> int:
    # sums the joltage across all banks
    # battery count: number of batteries that are ON in each bank
    joltage = 0

    for bank in arr_str: 
        joltage += parse_bank (bank, battery_count)
    
    return joltage 

if __name__ == "__main__":
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    arr_str = split_data(load_input(input_file), "\n")
    if not arr_str:
        print("Main: No battery banks found! Exiting")
        exit()

    print("Main: got the battery banks.\n")

    joltage_p1 = go_through_banks(arr_str, 2)
    joltage_p2 = go_through_banks(arr_str, 12)

    print(f"Main: (part 1) joltage when 2 batteries ON  = {joltage_p1}")
    print(f"Main: (part 2) joltage when 12 batteries ON = {joltage_p2}")
