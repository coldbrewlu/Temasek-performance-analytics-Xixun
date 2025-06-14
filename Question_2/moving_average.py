# input: 
# 1) a list of N daily closing prices
# 2) an integer M representing the number of days for the moving average

# output: a list of M-day moving averages
def moving_average(prices, M):
    if M <= 0 or M > len(prices):
        raise ValueError("Window size M must be a positive integer and less than or equal to the length of prices.")

    res = []
    window_sum = 0

    # slide the window from index M to the end of the list
    for i in range(len(prices)):
        window_sum += prices[i]
        # when the first M elements are added
        if i >= M - 1:
            # calculate the average for the current window
            res.append(window_sum / M)
            # subtract the element that is sliding out of the window
            window_sum -= prices[i - (M - 1)]
    return res

### Time complexity: O(N)
    # The function contains a single for loop that iterates through the list of prices once. Inside the loop, each element is added to window_sum once at constant time. Once the window reaches size M, the function calculates the average and subtracts the element that is sliding out of the window, which also takes constant time. Therefore, the overall time complexity is O(N), where N is the number of daily closing prices.
    
### Space complexity: O(N-M+1) 
    # The space complexity is determined by the number of elements stored in res list. Given a window of size M and a list of N prices, the maximum number of averages that can be stored in res is N-M+1. Hence, the overall space complexity would be O(N-M+1). The worst case occurs when M is 1, resulting in O(N) space complexity. 
    
