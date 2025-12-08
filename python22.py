#MENU--DRIVEN--PROGRAM
#1>>BUILDING A CALCULATOR:
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):#tdddddd66666666666ddddrssnhysbvgtrfxsb vbde sebd srx4rx vmdxs6rxvn 6rsxvn xrv n vn vnv nv n
    return a*b
def div(a,b):
    return a/b
def display_menu():
    print("###SIMPLE CALCULATOR###")
    print("1.ADDITION\n2.SUBTRACTION\n3.MULTIPLICATION\n4.DIVISION\n5.QUIT")
while True:
        display_menu() 
        choice=int(input("ENTER YOUR CHOICE: "))
        if choice in (1,2,3,4):
            a=int(input("ENTER 1ST NO: "))
            b=int(input("ENTER 2ND NO: "))
        if choice==1:
                print("RESULT:",add(a,b))
        elif choice==2:
                print("RESULT:",sub(a,b))
        elif choice==3:
                print("RESULT:",mul(a,b))
        elif choice==4:
                print("RESULT:",div(a,b))
        elif choice==5:
                print("QUITING....")
                break
        else:
                print("INVALID CHOICE,TRY AGAIN!")
            
    