#assignemnt2
#basic calculator

num1=int(input("enter the first number : "))
num2=int(input("enter the second number : "))

s=input("enter the operator +,-,*,/,//,%  : ")

if s== "+":
    print(num1+num2)

elif s=="-":
    print(num1-num2)    

elif s=="*":
    print(num1*num2)

elif s=="/":
    print(num1/num2)

elif s=="//":
    print(num1//num2)

elif s=="%":
    print(num1%num2)        

else:
    print("invalid operator")    