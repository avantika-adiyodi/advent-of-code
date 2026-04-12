# --- Day 5: Cafeteria ---
# fresh ingredients in the cafeteria

import os
from helpers import load_input, split_data
import bisect

example = False # set to True to run with example input, False to run with actual input
input_file = os.path.join(os.path.dirname(__file__), "inputs", "inp5.txt")
input_file_ex = os.path.join(os.path.dirname(__file__), "inputs", "inp5_example.txt") # path to example file

def split_database_inputs(content: str) -> list[str]:
    # split input file into list of ranges and list of ingredient IDs
    if not content:
        return []
    
    # to separate range and IDs
    sep = content.index("\n\n")
    ranges = content[:sep].split("\n")
    ids = content[sep+2:].split("\n")
    return ranges, ids


def merge_intervals(ranges: list[tuple]):
    ranges.sort()
    merged = []

    for start, end in ranges:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return merged


def contains(merged: list, x: int) -> bool:
    # find position where x would go
    i = bisect.bisect_right(merged, [x, float('inf')]) - 1
    
    if i >= 0:
        start, end = merged[i]
        return start <= x <= end
    
    return False


def find_fresh_ingredients (fresh_range_str: list[str], ingredient_ids: list[str]) -> int:
    ranges_str = []
    available_fresh_ingredients = 0
    total_fresh_ingredients = 0

    # get the range of fresh ingredients
    for range_str in fresh_range_str:
        start, end = range_str.split("-")
        tuple_ = (int(start), int(end))
        ranges_str.append(tuple_)

    fresh_range = merge_intervals(ranges_str)
    # print(f"fresh_range[0] = {fresh_range[0]}")
    # print(f"fresh range = {fresh_range}")
    # print(f"{(range_[0], range_[1]) for range_ in fresh_range}")

    # get count of total fresh ingredients
    for range_ in fresh_range:
        start = range_[0]
        end = range_[1]
        length = len(range(start, end+1))
        total_fresh_ingredients += length
        # total_fresh_ingredients += len(range(range_[0], range_[1]))
        pass

    # get count of available fresh ingredients
    for ingredient in ingredient_ids:
        if contains (fresh_range, int(ingredient)):
            available_fresh_ingredients += 1

    
    
    return available_fresh_ingredients, total_fresh_ingredients


if __name__ == "__main__":
    print("--- Day 5: Cafeteria ---")
    if example:
        input_file = input_file_ex
        print("\nMain: Running with example input.")

    # print(f"Main: input file = {load_input(input_file)}")
    # arr_str = split_data(load_input(input_file), "\n")

    ranges_str, ingredientIDs_str = split_database_inputs(load_input(input_file))
    # print (f"Main: ranges_str = {ranges_str}")
    # print (f"Main: ingredientIDs_str = {ingredientIDs_str}")
    
    if not ingredientIDs_str:
        print("Main: No ingredients IDs found! Exiting")
        exit()

    print("Main: got the ingredients database.\n")

    fresh_ingredients, total_ingredients = find_fresh_ingredients(ranges_str, ingredientIDs_str)

    print(f"Main: (part 1) total number of available fresh ingredients = {fresh_ingredients}")
    print(f"Main: (part 2) total number of fresh ingredients = {total_ingredients}")
