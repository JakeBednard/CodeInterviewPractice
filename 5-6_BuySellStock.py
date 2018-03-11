def calculate_max_gain(prices):
    """
    Calculate the maximum profit possible from a list of stock prices over time.
    It is possible that no profit can be made, if so return 0.
    Runs in O(n)
    """

    max_profit = 0
    local_min, local_max = prices[0], prices[0]

    for i in range(1, len(prices)):

        if prices[i] < local_min:
            local_min = prices[i]
            local_max = prices[i]

        elif prices[i] > local_max:
            local_max = prices[i]

        profit = local_max - local_min
        max_profit = profit if profit > max_profit else max_profit

    return max_profit


if __name__ == "__main__":
    # Test 1
    stock_price = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    profit = calculate_max_gain(stock_price)
    print(profit == 30)  # should be 30

    # Test 2
    stock_price = [230, 255, 250, 300]
    profit = calculate_max_gain(stock_price)
    print(profit == 70)  # should be 70

    # Test 3
    stock_price = [230, 255, 220, 300]
    profit = calculate_max_gain(stock_price)
    print(profit == 80)  # should be 80

    # Test 4
    stock_price = [300, 255, 220, 100]
    profit = calculate_max_gain(stock_price)
    print(profit == 0)  # should be 0

    # Test 4
    stock_price = [200, 300, 180, 210]
    profit = calculate_max_gain(stock_price)
    print(profit == 100)  # should be 100