#this is utilities module and will be use in futre for import for use_utils.py

def iseven(n):
    return True if n%2==0 else False

def isodd(n):
    return True if n%2!=0 else False

def reverse_string(s):
    return s[::-1]

def count_vowels(s):
    count=0
    for x in s:
        if x.lower() in 'aeiou':
            count+=1
    return count