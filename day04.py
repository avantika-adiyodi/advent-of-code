# --- Day 4: Printing Department ---

import os
import numpy as np
from scipy import ndimage as nd
from helpers import load_input, split_data

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp4.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp4_example.txt") # path to example file

def go_through_forklift (forklift):
    
    # Convert each string into a list of characters
    char_array = np.array([list(row) for row in forklift]) # each string in forklift is converted to a list of characters, and then the list of lists is converted to a numpy array
    
    forklift_int = (char_array == '@').astype(int)
    
    # convolve in Moore neighborhood of each cell in forklift
    kernel = np.array([[1, 1, 1],
                       [1, 0, 1],
                       [1, 1, 1]])
    moore_neighborhood = nd.convolve(forklift_int, kernel, mode='constant', cval=0)

    roll_count = np.sum((forklift_int == 1) & (moore_neighborhood < 4))
    
    # print (f"forklift as integers = \n{forklift_int}")
    # print (f"output after convolution = \n{out}")
    # print (f"neighbors = \n{neighbors}")

    # print (f"accessible rolls = \n{np.where(neighbors < 4)}")

    return roll_count 



if __name__ == "__main__":
    if example == True: 
        input_file = input_file_ex
        print ("Main: Running with example input.\n")
    
    arr_str = split_data(load_input(input_file), "\n")
    
    if arr_str:
        print ("Main: got the rolls of paper.\n")
    else: 
        print("Main: No battery banks found! Exiting")
        exit ()
        
    roll_count = go_through_forklift(arr_str)
    print(f"Main: (part 1) accessible rolls (total neighboring rolls < 4)= {roll_count}")
    print(f"Main: (part 2) = ")
