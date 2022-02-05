def sliding_window(n, array):
    """
        The approach being utilized here in this sliding window pattern is: 
        - we will loop through all elements in the array 
        - add each element to this 'window'
        - slide the window if we have hit the required window size of 'K'
        - Perform whatever process that needs to be done
        - subtract the element going out
        - slide the window ahead 
    """
    windowSum, windowStart = 0, 0

    for windowEnd in range(len(array)):
        windowSum += array[windowEnd] # add the next element 
        # slide the window if the required window size of 'K' has been met 
        if windowEnd >= K - 1:
            # do something here or some process
            windowSum -= array[windowStart] # subtract the element going out 
            windowStart += 1 # slide the window ahead
    

