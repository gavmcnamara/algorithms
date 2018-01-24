''' Given a substring a, find the longest palendromic
substring contained in a.
'''

def palendrome(a):
    # makes sure there is not runtime errors
    if a <= "":
        return a

    # empty string for long palendrome
    lng_palendrome = ""
    for i in range(len(a)):
        for x in range(i):
            substring = a[x: i+1]
            # checks if there is a pandrome in string
            if substring == substring[::-1]:
                if len(substring) > len(lng_palendrome):
                    lng_palendrome = substring
    if len(lng_palendrome) == 0:
        print a, "is not a palendrome!"
    return lng_palendrome


print(palendrome("racecar"))
print(palendrome("abba"))
print(palendrome(""))
print(palendrome("dsfsdkjfabbaorejirv"))
print(palendrome("ab"))


'''Efficiency: O(n^2), this is because of the two for loops
the first for loop is equal to O(n) and the second is
equal to O(n). So combined it is O(n^2).

Code Design: this function will detect a palendrome in
string a and find the longest outcome. This will also
see if there is no palendromes and print out the input
with a statement declaring this is not a palendrome.
'''


