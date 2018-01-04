'''
Colleen is turning n years old! Therefore,
she has n candles of various heights on her
cake, and candle i has height heighti. Because the
taller candles tower over the shorter ones,
Colleen can only blow out the tallest candles.

Given the heighti for each individual candle, find
and print the number of candles she can
successfully blow out.
'''

import sys

def birthdayCakeCandles(n, ar):
    # Complete this function
    return ar.count(max(ar))

n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))
result = birthdayCakeCandles(ar)
print(result)