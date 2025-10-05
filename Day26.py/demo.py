#this file is for __name__ checking and for future import in check.py

def greet():
    print('hello from demo model ')

def module_check():
    if __name__=='__main__':
        print('this module is being directly running')
    else:
        print('this module is not being directly running')
