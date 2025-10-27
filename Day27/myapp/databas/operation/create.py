# this module opens a file
import os

def c():
    while 1:
        name=input('enter file name :')
        if os.path.exists(name):
            print('file already exist\nplease choose other name')
        else:
            f=open(name,'w')
            print('file has been successfully created ')
            break
          
 