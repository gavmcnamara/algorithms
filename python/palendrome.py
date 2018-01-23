''' Given a substring a, find the longest palendromic
substring contained in a.
'''

def question2(a):
    # if a has no values there is no runtime error
    if a <= "":
        return a

    lng_palendrome = ""
    for i in range(len(a)):
        for x in range(i):
            substring = a[x: i+1]
            if substring == substring[:: -1]:
                if len(substring) > len(lng_palendrome):
                    lng_palendrome = substring

    if len(lng_palendrome) == 0:
        print(a, "is not a palendrome")
    return lng_palendrome

print(question2("racecar"))
print(question2("dabbac"))

'''Efficiency: O(n^2), this is because of the two for loops
the first for loop is equal to O(n) and the second is
equal to O(n). So combined it is O(n^2).

Code Design: this function will detect a palendrome in
string a and find the longest outcome. This will also
see if there is no palendromes and print out the input
with a statement declaring this is not a palendrome.
'''


