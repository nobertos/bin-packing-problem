from utils.__instance__ import MAX_CAPACITY


class Bin:
    def __init__(self):
        self.remaining_capacity = MAX_CAPACITY
        self.items = []

    def __repr__(self):
        # draw bin
        bin_str = ""
        for item in self.items:
            bin_str += f"{item} "

        return f"(Bin: remaining capacity: {self.remaining_capacity}, items: {bin_str})"

    def __str__(self):
        return f"(Bin: remaining capacity: {self.remaining_capacity}, items: {self.items})"

    def push(self, item_size):
        if item_size > self.remaining_capacity:
            raise ValueError("Item size exceeds bin remaining capacity")

        self.items.append(item_size)
        self.remaining_capacity -= item_size


class Solution:

    def __init__(self, num_bins=1,
                 bin_list=None):
        self.num_bins = num_bins
        self.bin_list = bin_list if bin_list is not None else [
            Bin() for _ in range(num_bins)]

    def __eq__(self, other):
        return self.num_bins == other.num_bins

    def __lt__(self, other):
        return self.num_bins < other.num_bins

    def __str__(self):
        solution = f"Solution: {self.num_bins} \nbins:\n"
        num_items = 0
        for bin in self.bin_list:
            solution += f"{bin}\n"
            num_items += len(bin.items)
        solution += f"number of items: {num_items}\n"
        return solution

    def add_items(self, items):
        for item in items:
            self.add_item(item)

    def add_item(self, item_size):
        if (item_size <= self.bin_list[-1].remaining_capacity):
            self.bin_list[-1].push(item_size)
        else:
            self.num_bins += 1
            new_bin = Bin()
            new_bin.push(item_size)
            self.bin_list.append(new_bin)

    def add_item_idx(self, item_size, idx):
        if (item_size <= self.bin_list[idx].remaining_capacity):
            self.bin_list[idx].push(item_size)
            return
        raise ValueError("Item size exceeds bin remaining capacity")

    def best_fit(self, items):
        for item in items:
            self.best_fit_item(item)

    def best_fit_item(self, item_size):
        best_fit_bin = self.bin_list[0]
        for bin in self.bin_list:
            if item_size <= bin.remaining_capacity and bin.remaining_capacity < best_fit_bin.remaining_capacity:
                best_fit_bin = bin
        if item_size <= best_fit_bin.remaining_capacity:
            best_fit_bin.push(item_size)
        else:
            self.add_item(item_size)
