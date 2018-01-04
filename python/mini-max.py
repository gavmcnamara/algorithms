'''
Given five positive integers, find the minimum
and maximum values that can be calculated by
summing exactly four of the five integers.
Then print the respective minimum and maximum
values as a single line of two space-separated
long integers.

Input Format

A single line of five space-separated integers.

Constraints

Each integer is in the inclusive range [1, 10^9] .
Output Format

Print two space-separated long integers denoting
the respective minimum and maximum values that
can be calculated by summing exactly four of the
five integers.
(The output can be greater than 32 bit integer.)

Sample Input

1 2 3 4 5
Sample Output

10 14
'''

import sys

def miniMaxSum(arr):
    # complete this function
    # x adds up all integers that are in arr
    x = sum(arr)
    # x-max(arr) will subtract the highest number
    # from the sum of arr and x-min(arr)
    # will print subtract the lowest number
    # from the sim of arr
    print(x-max(arr), x-min(arr))

if __name__ == "__main__":
    arr = list(map(int, input().strip().split(' ')))
    miniMaxSum(arr)