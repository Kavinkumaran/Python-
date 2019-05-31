print("welcome to OLA cab")
a=int(input("Enter the starting km:"))
b=int(input("Enter the destination km:"))
print("cab type:auto,micro,mini")
c=(input("Enter the cab type:"))
n=int(input("Enter the no of person traveled:"))
d=b-a
if a<=0:
    print("Enter the correct starting km!")
elif c=='auto': 
    g=15
    e=g*d*n
    print("your payment:",e)
elif c=='micro':
    g=20
    e=g*d*n
    print("your payment:",e)  
elif c=='mini':
    g=30
    e=g*d*n
    print("your payment:",e)
else:
    print("Enter the correct details")   
print("Thank you!")        
