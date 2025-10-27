#delete the file
import os
def delete():
    fname=input('enter file name :')
    if os.path.exists(fname):
        f=open(fname,'w')
        f.write('')
        print('file deletion successfull')
    else:
        print('file does not exist')
