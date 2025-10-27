import os 

def read():
    fname = input('enter the file name: ')
    if os.path.exists(fname):
        f = open(fname, 'r')
        data = f.readline()     

        while data != '':       
            print(data, end='') 
            data = f.readline() 

        f.close()
        print('\nfile has been read')
    else:
        print('file does not exist')
