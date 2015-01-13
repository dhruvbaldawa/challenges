def petrol(A):
    min = None
    max_profit = None
    buy = None
    sell = None

    for index, item in enumerate(A):
        if (min is None) or (item < min):
            min = item
            buy = index

        elif (max_profit is None) or (item - min) > max_profit:
            max_profit = item - min
            sell = index

    return max_profit, buy, sell


print petrol([75, 70, 72, 74, 76, 79, 72, 74])
