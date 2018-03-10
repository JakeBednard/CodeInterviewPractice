def calculate_max_gain(prices):
    """
    Calculate the maximum profit possible from a list of stock prices over time.
    It is possible that no profit can be made, if so return 0.
    """

    max_profit = 0
    local_min, local_max = prices[0], prices[0]

    for i in range(len(prices)):

        if prices[i] < local_min:
            profit = local_max - local_min
            max_profit = profit if profit > max_profit else max_profit
            local_min = prices[i]
            local_max = prices[i]

        elif prices[i] > local_max:
            local_max = prices[i]

    return max_profit


if __name__ == "__main__":
    stock_price = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
    profit = calculate_max_gain(stock_price)
    print(profit)  # should be 30
