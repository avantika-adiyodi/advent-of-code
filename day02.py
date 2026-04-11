# --- Day 2: Gift Shop ---
# sum of all invalid IDs 

import os
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp2.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp2_example.txt") # path to example file

count = 0
invalid_sum_twice = 0
invalid_sum_any = 0
list_repeats = []

def repeat_any(num=int): # check if any repeating sequences
    global invalid_sum_twice
    
    num_str = str(num)
    check_str = (num_str + num_str)[1:-1]
    check = num_str in check_str

    if check and ((len (num_str) % 2) == 0): # check if number only contains twice repeated sequence
        half_len = int((len (num_str)) / 2)
        divide_by = pow (10, half_len)
        x1 = int (num / divide_by)
        x2 = int (num % divide_by)
        if x1 == x2: invalid_sum_twice += num

    return check


def parse_range(id_range): # takes one range as input
    global count
    global invalid_sum_any

    range_str = id_range.split("-")
    firstID = int(range_str[0])
    lastID = int(range_str[1])
    
    for num in range (firstID, lastID + 1): # each number in range (inclusive)
        if len(str(num)) <= 1: continue # min 2 digits needs to repeat
        
        else: 
            if repeat_any(num): 
                invalid_sum_any += num
    return

if __name__ == "__main__":
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    arr_str = split_data(load_input(input_file), ",")
    
    if not arr_str:
        print("Main: No ranges found! Exiting")
        exit ()
    
    print ("Main: got the splitted ranges\n")
    
    for id_range in arr_str: parse_range(id_range)
    print (f"Main: (part 1) total sum of twice repeating invalid IDs = {invalid_sum_twice}")
    print (f"Main: (part 2) total sum of any repeating invalid IDs = {invalid_sum_any}")

    
