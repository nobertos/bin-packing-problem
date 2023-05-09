import numpy as np
from utils.instance import MAX_CAPACITY
def dynamic_programming(items):
    size = len(items)
    dp = np.full((size,size),np.inf)
    dp[0,0] = 0
    for bin_idx in range(size-1):
        for item_idx in range(size):
            if dp[bin_idx,item_idx] != np.inf:
                left = MAX_CAPACITY
                dp[bin_idx + 1,item_idx] = min(dp[bin_idx + 1,item_idx], (dp[bin_idx, item_idx] + left**2))
                print(dp)
                for next_item_idx in range(item_idx+1, size):
                    left -= items[next_item_idx]
                    if left < 0:
                        break
                    dp[bin_idx+1, next_item_idx] = min(dp[bin_idx+1, next_item_idx], dp[bin_idx, item_idx] + left*left)
    return dp
