# --- Day 1: Secret Entrance ---
# find number of times dial crosses zero or points at zero

import os
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp1.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp1_example.txt") # path to example file

def change_per_rot (direction: str, rot: int, dial: int) -> tuple[int, int, int]:
    # to calculate change per rotation
    # returns the new dial position after rotation, points to zero for this step, and zero crosses for this step

    zero_points = 0
    zero_crosses = rot // 100
    rot = rot % 100
  
    if direction == "L":
        change = dial - rot
        if dial != 0 and change < 0:
            zero_crosses += 1

    else: # direction == "R"
        change = dial + rot
        if dial != 0 and change > 100:
            zero_crosses += 1

    new_dial = change % 100

    if new_dial == 0:
        zero_points += 1

    return new_dial, zero_points, zero_crosses

def get_step (commands: list[str], dial: int) -> tuple[int, int, int]:
    # to get each rotation and count
    # returns the position of dial per command
    total_zero_points = 0
    total_zero_crosses = 0
    for cmd in commands:
        direction = cmd[0]
        rot = int(cmd[1:])
        dial, points, crosses = change_per_rot(direction, rot, dial)
        total_zero_points += points
        total_zero_crosses += crosses

    return dial, total_zero_points, total_zero_crosses

if __name__ == "__main__":
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    arr_str = split_data(load_input(input_file), "\n")
    if not arr_str:
        print("Main: No rotations found! Exiting")
        exit ()
    
    print ("Main: got the splitted commands\n")
    
    dial = 50
    print (f"Main: initial dial positon = {dial}")

    dial, count_zero, count_zero_cross = get_step(arr_str, dial)
    print (f"Main: final dial positon = {dial}")
    print (f"Main: (part 1) total number of times the dial pointed to 0 = {count_zero}")
    print (f"Main: (part 2) total number of times the dial crossed/pointed to 0 = {count_zero + count_zero_cross}")

