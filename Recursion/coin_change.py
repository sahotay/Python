#!/usr/local/bin/python3
def rec_coin(target,coins):
    min_coins = target
    # Edge case
    if target in coins:
        return 1
    for i in [c for c in coins if c<= target]:
        num_coins = 1 + rec_coin(target-i, coins)
        if num_coins < min_coins:
            min_coins = num_coins
    return min_coins
print(rec_coin(10,[1,5])) #2

#recursive programming
def rec_coin_dynamic(target,coins,know_results):
    # Default output of target
    min_coins = target

    # Edge Case
    if target in coins:
        know_results[target] = 1
        return 1
    # Return a known result if it happens to be greater than 1
    elif know_results[target] > 0:
        return know_results[target]
    else:
        # for every coin value that is <= than target
        for i in [c for c in coins if c<= target]:
            # Recursive call, note how we include the known results!
            num_coins = 1 + rec_coin_dynamic(target-i,coins,know_results)

            # Reset Minimum if we have a new minimum
            if num_coins < min_coins:
                min_coins = num_coins

                # Reset the known results
                know_results[target] = min_coins
    return min_coins

target = 74
coins = [1,5,10,25]
known_results = [0]*(target+1)
print(rec_coin_dynamic(target,coins,known_results))