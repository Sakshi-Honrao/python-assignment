n=int(input("enter a number:"))
if(n<=0):
    print(" {} is invalid".format(n))
else:
    i=1
    while(i<=10):
        print("{}*{}={}".format(i,n,i*n))
        i=i+1
    else:
        print("-"*50)



num=int(input("enter a number:"))
i=1
while(i<=10):
    print(num*i)
    i=i+1
