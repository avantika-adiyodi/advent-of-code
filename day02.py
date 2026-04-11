# --- Day 2: Gift Shop ---
# sum of all invalid IDs 

import os
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp2.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp2_example.txt") # path to example file

# g_invalid_sum_twice = 0
# g_invalid_sum_any = 0

def repeating_sequence(num: int) -> bool:
    # return True if num appears as a sub-string in its own doubled string
    # i.e. it is a rotation of itself — meaning it contains a repeated sequence
    
    s = str(num)
    return s in (s + s)[1:-1]

def repeat_twice(num: int) -> bool: 
    # check if any sequences repeat twice only
    # global g_invalid_sum_twice
    
    num_str = str(num)

    # if repeating_sequence(num) and ((len (num_str) % 2) == 0): # check if number only contains twice repeated sequence
    if (len (num_str) % 2) == 0: # check if number only contains twice repeated sequence
        half_len = int((len (num_str)) / 2)
        divide_by = pow (10, half_len)
        x1 = int (num / divide_by)
        x2 = int (num % divide_by)
        if x1 == x2: 
            return True

    return False


def parse_range(id_range: str): 
    # takes one range as input
    # returns sum of invalid IDs in that range
    # global g_invalid_sum_any
    # global g_invalid_sum_twice

    invalid_sum_twice = 0
    invalid_sum_any = 0
    
    firstID, lastID = id_range.split("-")
    
    for num in range (int(firstID), int(lastID) + 1): # each number in range (inclusive)
        if len(str(num)) <= 1: # min 2 digits needs to repeat
            continue 
        
        if repeating_sequence(num):
            # g_invalid_sum_any += num
            invalid_sum_any += num
            if repeat_twice(num): # check if it also contains twice repeated sequence
                # g_invalid_sum_twice += num
                invalid_sum_twice += num

    return invalid_sum_twice, invalid_sum_any

if __name__ == "__main__":
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    arr_str = split_data(load_input(input_file), ",")
    
    if not arr_str:
        print("Main: No ranges found! Exiting")
        exit ()
    
    print ("Main: got the split ranges\n")
    
    total_twice = 0
    total_any = 0
    
    for id_range in arr_str: 
        invalid_sum_twice, invalid_sum_any = parse_range(id_range)
        total_twice += invalid_sum_twice
        total_any += invalid_sum_any
    print (f"Main: (part 1) total sum of twice repeating invalid IDs = {total_twice}")
    print (f"Main: (part 2) total sum of any repeating invalid IDs = {total_any}")

    
