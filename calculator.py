# bhavesh-multi,divide
#addition subtraction -himanshu
#harsh -power



def add(n):
 n1 = int(input("enter first number to perform addition/subtraction :"))
 n2 = int(input('Enter second number to add/subtract from : '))

 print('Enter  : \n  "A" for Addition \n "S" for subtraction  ')
 input = str(input())
 if input == 'a' or input == "A" :
    print(f'the sum of the numbers is : {n1+n2}')
 elif input == "S" or input =='s' :
    print(f'The difference of the numbers is : {n1-n2}')
  
 print('thank you')
