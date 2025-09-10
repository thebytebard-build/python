a=1
while a>0:
    n=input('enter a string ')
    choice=int(input('enter a number '))
    match choice:
        case 1:
            print(n.isalnum())
        case 2:
            print(n.isalpha())
        case 3:
            print(n.isdigit())
        case 4:
            print(n.islower())
        case 5:
            print(n.isupper())
        case 6:
             print(n.istitle())
        case 7:
             print(n.isspace())
        case 8:
            a=0
     
    