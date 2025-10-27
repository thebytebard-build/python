def c_v(s):
    count=0
    for x in s:
        if x in 'aeiou':
            count+=1
    return count