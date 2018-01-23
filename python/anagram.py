'''
 Given two strings s and t, determine whether some anagram
 of t is a substring of s. For example: if s = "udacity"
 and t = "ad", then the function returns True.
 Your function definition should look
 like: question1(s, t) and return a boolean True or False.

 Takes in 2 aruements and checks if they are anagrams
 '''

def isAnagram(str1, str2):
    # Creates 2 sorted lists
    str1_list = sorted(str1)
    str2_list = sorted(str2)
    # Compares and returns the sorted lists
    return (str1_list==str2_list)

def question1(s, t):
    # Iterates to see if t is a substring of s
    for i in range(len(s)-len(t)+1):
        if isAnagram(s[i: i+len(t)], t):
            return True
    return False

print(question1("gavin", "vin"))
print(question1("gavin", "asd"))

'''
Efficiency: O(n)
'''