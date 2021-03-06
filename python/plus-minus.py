'''
Given an array of integers, calculate which fraction
of its elements are positive, which fraction of its
elements are negative, and which fraction of its
elements are zeroes, respectively. Print the decimal
value of each fraction on a new line.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places,
though answers with absolute error of up to 10^-4
are acceptable.

Input Format

The first line contains an integer, N, denoting
the size of the array. The second line contains
N space-separated integers describing an array of numbers .

Output Format

You must print the following  lines:

A decimal representing of the fraction
of positive numbers in the array compared to its size.

A decimal representing of the fraction of
negative numbers in the array compared to its size.

A decimal representing of the fraction of zeroes
in the array compared to its size.

Sample Input
6
-4 3 -9 0 4 1
Sample Output

0.500000
0.333333
0.166667'''


import sys

def plusMinus(arr):
    # Complete this function
    print(round(len([x for x in arr if x > 0])/n, 6))
    print(round(len([x for x in arr if x < 0])/n, 6))
    print(round(len([x for x in arr if x == 0])/n, 6))


if __name__ == "__main__":
    n = int(input().strip())
    arr = list(map(int, input().strip().split(' ')))
    plusMinus(arr)