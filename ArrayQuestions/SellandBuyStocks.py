## Best time to buy and sell stocks

def findMaxProfit(arr):
    max_profit = 0
    for i in range(len(arr)-1):
        for j in range(i+1, len(arr)):
            if arr[j]-arr[i] > max_profit:
                max_profit = arr[j]-arr[i]

    return max_profit





## Driver Code
prices = [7, 1, 5, 3, 6, 4]

result = findMaxProfit(prices)
print(result)