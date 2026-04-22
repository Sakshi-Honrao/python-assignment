""" 1. Write a program to add item 7000 after 6000 in the following Python List
 list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]"""
	

lst1=[10,20,[300,400,[5000,6000,],500],30,40]

lst1[2][2].append(7000)
print(lst1)


""" 2.Type Checking"""

a = 10
b = 10.0
print(type(a) == type(b))


"""3. Write a program to print area of rectangle"""

length=int(input("enter length of rectangle:"))
width=int(input("enter width of rectangle:"))
area=length*width
print(area)

""" 4.Write a program to print area of circle"""

pie=3.14
radius=int(input("enter radius of circle:"))
area=pie*radius*radius
print(area)


""" 5. Write a program to print area of square"""

side=int(input("enter side of square:"))
area=side*side
print(area)



"""6.Write a program to add item "saibaba" after 2 in the following Python List.
    l=[l1,2,33,6,55,98] """

l=[l1,2,33,6,55,98]
l.insert(1,"saibaba")
print(l)

""" reverse the element of list"""

l=[1,2,88,99,65,4,7]
l.reverse()
print(l)



"""7.write a program to add 5 bonus marks to values in a dictionary"""


marks = {"amit": 60, "raj": 70, "neha": 55}
for student in marks:
    marks[student]=marks[student]+5
print(marks)



"""8.Write a Python program to filter residents aged 18 or above and store them in separate lists based on their ward number"""

resident= {
    "sakshi patil": {"age": 2, "ward_number": 1},
    "rahul sharma": {"age": 28, "ward_number": 2},
    "priya deshmukh": {"age":5, "ward_number": 3},
    "amit joshi": {"age": 40, "ward_number": 1},
    "neha kulkarni": {"age": 30, "ward_number": 4},
       }
ward1=[]
ward2 = []
ward3 = []
ward4= []
ward5 = []
for name, data in resident.items():
    if data['age']>=18:
        if data['ward_number']==1:
            ward1.append(name)
        elif data['ward_number']==2:                                    
            ward2.append(name)
        elif data['ward_number'] == 3:
            ward3.append(name)
        elif data['ward_number'] == 4:
            ward4.append(name)
        elif data['ward_number'] == 5:
            ward5.append(name)
        else:
            pass
print(f'eligible person from ward1:{ward1}')
print(f'eligible person from ward2:{ward2}')
print(f'eligible person from ward3:{ward3}')
print(f'eligible person from ward4:{ward4}')
print(f'eligible person from ward5:{ward5}')



"""9. wap to determine character entered by user. """

char=input("press nay key:")
if char.isalpha():
    print("the user has enteres a character")
if char.isdigit():
    print("the user has enteres a digit")
if char.isspace():
    print("the user has enteres a space character")


"""10. Find list of common unique items from two list. and show in increasing order."""

num1 = [23, 45, 67, 78, 89, 34]
num2 = [34, 89, 55, 56, 39, 67]

result = list(set(num1) & set(num2))
result.sort()
print(result)


"""11. wap to that display all leap years from 1900 to 2101."""

print("leap year from 1900 to 2101 are:")
for i in range(1900,2101):
    if i%4==0:
        print(i,end=" ")

"""12.write a program to check given character is present in given string or not."""

ch=input("enter character:")
str=input("enter a string:")

for i in str:
    if i==ch:
        print("present")
    else:
        print("not present")

"""13. Write a program that can find the max number of each row of a matrix."""

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = []
for row in matrix:
    result.append(max(row))
print(result)

"""14.Write a program to find set of common elements in three lists using sets."""

ar1 = [1, 5, 10, 20, 40, 80]
ar2 = [6, 7, 20, 80, 100]
ar3 = [3, 4, 15, 20, 30, 70, 80, 120]

result = list(set(ar1) & set(ar2) & set(ar3))
print(result)



"""15.Write a Python program to simulate a basic banking system using a dictionary."""


accounts={101:{'name':'sakshi','balance':30000,'pin':4589},102:{'name':'neha','balance':40000,'pin':6589},
          103:{'name':'priya','balance':50000,'pin':5589}}


while True:
    print('''
    1.Detail
    2.Deposit
    3.Withdraw
    4.Check Balance
    5.Logout
    ''')
    ch=int(input("enter your choice:"))
    if ch==1:
        ac=int(input("account number:"))
        data=accounts[ac]
        print(f'''
        Name:{data['name']}
        Account no:{ac}
        Balance:{data['balance']}
      ''')

    elif ch==2:
        ac=int(input("ac:"))
        amount=float(input("amount:"))
        accounts[ac]['balance']=accounts[ac]['balance']+amount
        print("done")


    elif ch==3:
        ac=int(input("ac:"))
        amount=float(input("amount:"))

        if amount <= 0:
            print("Invalid amount. Enter a positive number.")
        else:
            accounts[ac]['balance']=accounts[ac]['balance']-amount
            print("Withdrawal successful!")

    elif ch==4:
            ac=int(input("ac:"))
            print("your balance is:",accounts[ac]['balance'])
    elif ch==5:
             print("logout")



"""16.write a Python program to print the even numbers from a given list."""

lst = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []
for num in lst:
    if num % 2 == 0:
        result.append(num)
print(result)