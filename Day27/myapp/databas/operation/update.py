#this file update data
import os 
def update():
    fname=input('enter the file name ')
    if os.path.exists(fname):
        f=open(fname,'a')
        data=input('enter the data')
        f.write(data+'\n')
        print('\nfile hs been updated successfully')
    else:
        print('file does not exist')