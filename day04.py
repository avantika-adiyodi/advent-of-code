# --- Day 4: Printing Department ---

import os
import numpy as np
from scipy import ndimage as nd
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp4.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp4_example.txt") # path to example file

MOORE_KERNEL = np.array([[1, 1, 1],
                          [1, 0, 1],
                          [1, 1, 1]])

def go_through_forklift (forklift, loop = False):
    
    # Convert each string into a list of characters
    char_array = np.array([list(row) for row in forklift]) # each string in forklift is converted to a list of characters, and then the list of lists is converted to a numpy array
    forklift_int = (char_array == '@').astype(int)

    # convolve in Moore neighborhood of each cell in forklift
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    moore_neighborhood = nd.convolve(forklift_int, kernel, mode='constant', cval=0)

    rolls_row, rolls_column = np.where((forklift_int == 1) & (moore_neighborhood < 4)) # returns row numbers and column numbers of wherever there is an accessible roll in the forklift
    accessible_rolls = np.sum((forklift_int == 1) & (moore_neighborhood < 4))

    
    roll_count = accessible_rolls
    if loop:
        # update forklift to remove the current accessible rolls and repeat till count of accessible rolls = 0
        
        while accessible_rolls > 0:
            if rolls_row is not None and rolls_column is not None:
                forklift_int [rolls_row, rolls_column] -= 1
            
            moore_neighborhood = nd.convolve(forklift_int, kernel, mode='constant', cval=0)
            
            rolls_row, rolls_column = np.where((forklift_int == 1) & (moore_neighborhood < 4))
            accessible_rolls = np.sum((forklift_int == 1) & (moore_neighborhood < 4))
            roll_count += accessible_rolls

    return roll_count


if __name__ == "__main__":
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    arr_str = split_data(load_input(input_file), "\n")
    if not arr_str:
        print("Main: No rolls found! Exiting")
        exit()

    print("Main: got the rolls of paper.\n")

    roll_count_once = go_through_forklift(arr_str, loop=False)
    roll_count_loop = go_through_forklift(arr_str, loop=True)

    print(f"Main: (part 1) accessible rolls without looping = {roll_count_once}")
    print(f"Main: (part 2) accessible rolls until all are processed = {roll_count_loop}")
