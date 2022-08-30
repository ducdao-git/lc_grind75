def coin_change(coins, amount):
    min_coins = {0: 0}

    for num in range(1, amount + 1):
        min_coin_num = amount
        is_updated = False

        for coin in coins:
            remain = num - coin

            if remain >= 0 and min_coins[remain] >= 0:
                min_coin_num = min(1 + min_coins[remain], min_coin_num)
                is_updated = True

        if is_updated:
            min_coins[num] = min_coin_num
        else:
            min_coins[num] = -1

    return min_coins[amount]


coin_change([3, 5], 11)
