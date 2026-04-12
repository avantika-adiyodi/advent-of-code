# --- Day 5: Cafeteria ---
# fresh ingredients in the cafeteria

import os
from helpers import load_input
import bisect

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp5.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp5_example.txt") # path to example file


def split_database_inputs(content: str, separator: str) -> list[str, str]:
    # function to split the input file into list of ranges and list of IDs according to separator
    # returns list of ranges and IDs
    if not content:
        return [], []
    
    # to separate range and IDs
    seperation_idx = content.index(separator)
    ranges = content[:seperation_idx].split("\n")
    ids = content[seperation_idx + 2:].split("\n")
    return ranges, ids


def merge_ranges(ranges: list[tuple]) -> list:
    # function to merge overlapping ranges
    # parameter ranges: list of ranges to merge
    # returns list of all the ranges merged
    ranges.sort()
    merged_range = []

    for start, end in ranges:
        if not merged_range or merged_range[-1][1] < start:
            merged_range.append([start, end])
        else:
            merged_range[-1][1] = max(merged_range[-1][1], end)
    return merged_range


def range_contains_ID (range_IDs: list, check_id: int) -> bool:
    # function to check if the given ID is in any of the given ranges
    # find the index of the range that could contain the check_id and check if the check_id is within the range
    range_index = bisect.bisect_right(range_IDs, [check_id, float('inf')]) - 1 
    
    if range_index >= 0:
        start, end = range_IDs[range_index] 
        return start <= check_id <= end 
    
    return False


def find_fresh_ingredients (ranges_str: list[str], ingredient_ids: list[str]):
    # function to find the total number of fresh ingredients and the number of available fresh ingredients
    fresh_ranges = []
    available_fresh_ingredients = 0
    total_fresh_ingredients = 0

    # get the range of fresh ingredients
    for range_str in ranges_str:
        start, end = range_str.split("-")
        fresh_ranges.append((int(start), int(end)))

    fresh_ranges = merge_ranges(fresh_ranges)

    # get count of total fresh ingredients
    for fresh_range in fresh_ranges:
        # length = len(range(fresh_range[0], fresh_range[1] + 1))
        total_fresh_ingredients += len(range(fresh_range[0], fresh_range[1] + 1))

    # get count of available fresh ingredients in inventory
    for ingredient in ingredient_ids:
        if range_contains_ID (fresh_ranges, int(ingredient)):
            available_fresh_ingredients += 1
    
    return available_fresh_ingredients, total_fresh_ingredients


if __name__ == "__main__":
    print("--- Day 5: Cafeteria ---")
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    fresh_ranges_str, ingredientIDs_str = split_database_inputs(load_input(input_file), separator="\n\n")
    
    if not ingredientIDs_str:
        print("Main: No ingredients IDs found! Exiting")
        exit()

    print("Main: got the ingredients database.\n")

    fresh_ingredients, total_ingredients = find_fresh_ingredients(fresh_ranges_str, ingredientIDs_str)

    print(f"Main: (part 1) total number of available fresh ingredients = {fresh_ingredients}")
    print(f"Main: (part 2) total number of fresh ingredients = {total_ingredients}")
