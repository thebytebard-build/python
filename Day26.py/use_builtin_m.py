#in this file we will use builtin module 

#working with datetime
def use_datetime():
    import datetime as d

    # print today date
    print(f"Today date: {d.date.today()}")

    now = d.datetime.now()
    
    # print current time without microseconds
    print(f"Current time: {now.time().replace(microsecond=0)}")

    # print current year
    print(f"Current year: {now.year}")

    # print without using 'now' variable
    print("Current year (without variable):", d.datetime.now().year)
    print("Current time (without variable):", d.datetime.now().time().replace(microsecond=0))


#working with string module
def use_string():
    import string as s

    # Print lowercase letters
    print(f"Lowercase letters: {s.ascii_lowercase}")

    # Print digits
    print(f"Digits: {s.digits}")

    # Print punctuation
    print(f"Punctuation: {s.punctuation}")


#working with os module
def use_os():
    import os

    #print current working directory
    print(f"current working directory : {os.getcwd()}")

    #list all files in current working directory
    print(f"files in current working directory : {os.listdir()}")


use_os()





