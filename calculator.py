# bhavesh-multi,divide
#addition subtraction -himanshu
#harsh -power
add_minus
def add():
     a=float(input("enter the first number : "))
     b=float(input("enter the second number : "))
     print(f"Addition of {a} and {b} is {a+b}")
 
def sub(a,b) :
     print(f"Subtraction of {a} and {b} is {a-b}")


def power():
    a=float(input("enter number for base : "))
    b=float(input("enter number for power : "))
    if (b==0):
        print(1)
    elif(b>0):
        c=1
        for i in range(0,int(b)):
            c=c*a
        print(c)
    else:
        b=-(b)
        c=1
        for i in range(0,int(b)):
            c=c*a
        print(a)
num=int(input("enter 1 if you want to ADDITION and 2 for SUBTRACTION :: \nenter 3 if you want to MULTIPLICATION and 4 for DIVISION ::\nenter 5 if you want to find POWER ::  \n"))
if(num==5):
    power()
elif(num==1):
     add()
elif(num==2):
    sub()
elif(num==3):
    multi()
elif(num==4):
    divide()
else:
    print("BUND MARAO")
 


