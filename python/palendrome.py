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





