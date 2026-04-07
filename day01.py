# find number of times dial crosses zero or points at zero

import os
from helpers import load_input, split_data

input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp1.txt")

count_zero = 0
count_zero_cross = 0

# to calculate change per rotation
# returns the current dial postion after rotation
def change_per_rot (direction, rot, dial):
    global count_zero_cross, count_zero
    count_zero_cross += rot // 100
    rot = rot % 100
    
    match direction:
        case "L":

            if dial != 0:
                dial = dial - rot 
                if dial < 0: count_zero_cross += 1
                dial = dial % 100
            else: 
                dial = (dial - rot) % 100

        case "R":

            if dial != 0:
                dial = dial + rot
                if dial > 100: count_zero_cross += 1
                dial = dial % 100
            else: 
                dial = (dial + rot) % 100
    
    if dial == 0:
        count_zero += 1

    return dial

# to get each rotation and count
# returns the position of dial per command
def get_step (arr_exp, dial):
    for i in arr_exp:
        direction = i[0]
        rot = int(i[1:])
        dial = change_per_rot(direction, rot, dial)
    return dial

if __name__ == "__main__":
    dial = 50

    print (f"Main: initial dial positon = {dial}")

    arr_str = split_data(load_input(input_file), "\n")
    if arr_str:
        print ("Main: got the splitted commands\n")
    else: 
        print("Main: No rotations found! Exiting")
        exit ()
        
    dial = get_step(arr_str, dial)
    print (f"Main: final dial positon = {dial}")
    print (f"Main: total number of times the dial pointed to 0 = {count_zero}")
    print (f"Main: total number of times the dial crossed/pointed to 0 = {count_zero + count_zero_cross}")

