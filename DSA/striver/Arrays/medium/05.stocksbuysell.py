prices = [7, 1, 5, 3, 6, 4]

n = len(prices)
max_profit = 0

for buy in range(n):
    for sell in range(buy+1, n):
        profit = prices[sell] - prices[buy]

        max_profit = max(max_profit, profit) 

print(max_profit)

#optimal

prices = [7, 1, 5, 3, 6, 4]

n = len(prices)
max_profit = 0
min_price = float("inf")

for price in prices:
    if price < min_price:
        min_price = price
    else:
        max_profit = max(max_profit, price - min_price)