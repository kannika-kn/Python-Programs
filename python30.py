try:
    age=int(input("ENTER YOUR AGE: "))
    years_left=100-age
    if years_left>0:
        print(f"YOU WILL BE 100 YEARS OLD IN {years_left} YEARS")
    elif years_left==0:
        print("YOU ARE 100 YEARS OLD THIS YEAR")
    else:
        print(f"YOU TURNED 100 {years_left} YEARS BACK")
except ValueError:
    print("INVALID INPUT! PLEASE ENTER A VALID NUMBER")
#2
try:
    num1=float(input("ENTER 1ST NUM: "))
    num2=float(input("ENTER 2ND NUM: "))
    a=num1/num2
    print(f"RESULT:{a}")
except ZeroDivisionError:
    print("ERROR: CANT DIVIDE BY 0")
except ValueError:
    print("Error:Please enter a valid number")



    