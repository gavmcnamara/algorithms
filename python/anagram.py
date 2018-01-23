'''
 Given two strings s and t, determine whether some anagram
 of t is a substring of s. For example: if s = "palendrome"
 and t = "end", then the function returns True.
 Your function definition should look
 like: question1(s, t) and return a boolean True or False.

 Takes in 2 aruements and checks if they are anagrams
 '''

def isAnagram(str1, str2):
    # creates 2 lists and compares and returns sorted list
    str1_list = sorted(str1)
    str2_list = sorted(str2)
    return (str1_list == str2_list)

def question1(s, t):
    for i in range(len(s)-len(t)+1):
        # if t is a substring of s return True
        if isAnagram(s[i: i+len(t)], t):
            return True
    return False

print(question1("palendrome", "end"))
print(question1("gavin", "vin"))
print(question1("gavin", "asd"))

'''
Efficiency: O(n)

Code design:
The isAnagram function creates two sorted lists and returns
them equal to eachother

The question1 function takes a for loop and iterates
to see if t is a substring of s.
There for the efficiency is O(n)

Readability:
The way I approached this problem was to use pythons sorted
function to create two sorted lists. Then, create to arguments
(s, t) to check if t is a substring of s. If this was true
it would return boolean true and if not return false.
'''