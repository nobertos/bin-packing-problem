from utils.__instance__ import MAX_CAPACITY
import math


def evaluate(num_bins, remaining_items):
    total_size = sum(remaining_items)
    opt_bins_needed = num_bins + math.floor(total_size / MAX_CAPACITY)
    return opt_bins_needed

# to use this version of the code, you need to prune when child.lower_bound > best_num_bins


def evaluate2(num_bins, remaining_items):
    total_size = sum(remaining_items)
    opt_bins_needed = num_bins + math.ceil(total_size/MAX_CAPACITY)
    return opt_bins_needed

# third evaluation function


def evaluation_fn(items1, items2, items3):
    return len(items1) + len(items2) + max(0, math.ceil((sum(items3)-(len(items2)*MAX_CAPACITY - sum(items2)))/MAX_CAPACITY))


def separate(remaining_items):
    min_size = remaining_items[-1]
    items1 = [item for item in remaining_items if item >
              MAX_CAPACITY - min_size]
    items2 = [item for item in remaining_items if item <=
              MAX_CAPACITY - min_size and item > MAX_CAPACITY//2]
    items3 = [item for item in remaining_items if item <= MAX_CAPACITY//2]
    return items1, items2, items3


def evaluate3(num_bins, remaining_items):
    opt_bins_needed = num_bins
    if len(remaining_items) != 0:
        items1, items2, items3 = separate(remaining_items)
        opt_bins_needed += evaluation_fn(items1, items2, items3)
    return opt_bins_needed
