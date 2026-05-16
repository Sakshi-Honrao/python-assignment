#1.Given a list of strings, filter out the ones with more than 5 characters.
#words = ["apple", "banana", "cat", "elephant", "dog", "grape"]

words = ["apple", "banana", "cat", "elephant", "dog", "grape"]
long_word=list(filter(lambda  w:len(w)>5 ,words))
print(long_word)
print("*"*55)


#2.Write a program to filter numbers from a list that are divisible by 3.

nums = [3, 5, 9, 12, 15, 17, 20]
div=list(filter(lambda n:n%3==0,nums))
print(div)
print("*"*55)

#3.From a list of strings, filter out all empty strings.

strings = ["Python", "", "Code", " ", "Filter", ""]
non_empty=list(filter(lambda s: s.strip()!="",strings))
print(non_empty)
print("*"*55)

#4. Filter Passing Students names only

students = {
    "Amol": 45,
    "Suraj": 78,
    "Ved": 88,
    "Siddhi": 55,
    "Payal": 33,
    "Ragini": 99,
    "Samruddi": 49
	}

pass_stud=list(filter(lambda name:students[name]>=50,students))
print(pass_stud)
print("*"*55)


#5.Given a dictionary of students and their percentages, filter out only the students who have passed (percentage >= 50). Return the result as a dictionary.

students = {
    "Amol": 45,
    "Suraj": 35,
    "Ved": 88,
    "Siddhi": 55,
    "Payal": 33,
    "Ragini": 60,
    "Samruddi": 99
	}
pass_stud=dict(filter(lambda name:name[1]>=50,students.items()))
print(pass_stud)
print("*"*55)

#Given a list of numbers, double each element using the map() function.

nums = [1, 2, 3, 4, 5]
double=list(map(lambda x:x*2,nums))
print(double)
print("*"*55)


#7.Given a list of strings, convert each string to uppercase using map().

names= ["dishant", "rajput", "sakshi", "shiddi"]
upper=list(map(lambda x:x.upper(),names))
print(upper)
print("*"*55)


#8.Given a list of integers, calculate the square of each number using the map() function and represent in dict.

numbers = [2, 3, 4, 5]
square=list(map(lambda x:x**2,numbers))
print(square)
print("*"*55)

#9. Given two lists of equal length, add their corresponding elements using map().

list1 = [1, 2, 3]
list2 = [4, 5, 6]

add=list(map(lambda x,y:x+y,list1,list2))
print(add)
print("*"*55)


#10.Given a list of strings, find the length of each string using map().

words = ["ragini", "samruddhi", "shiddi", "shyam"]
length=list(map(lambda w:len(w),words))
print(length)
print("*"*55)


#11.Given a list of numbers, calculate the product of all the elements using reduce().

from functools import reduce
nums = [2, 3, 4, 5]
product=reduce(lambda x,y:x*y,nums)
print(product)
print("*"*55)


#12.Given a list of numbers, find the maximum number using reduce().

from functools import reduce

nums = [10, 45, 23, 78, 34]
max_num=reduce(lambda x,y:x if x>y else y,nums)
print(max_num)
print("*"*55)

#13.Given a list of strings, concatenate them into a single string using reduce().

from functools import reduce

words = ["Python", "is", "fun"]
concat=reduce(lambda x,y:x+" "+y,words)
print(concat)
print("*"*55)


# 14.Addition using lambda function
add = lambda x, y: x + y
print(add(10, 5))  # Output: 15
print("*"*55)

#15.Multiplication
multiply = lambda x,y:x*y
print(multiply(4, 3))  # Output: 12
print("*"*55)

#16.max_value
max_value = lambda x, y: x if x > y else y
print(max_value(10, 20))  # Output: 20
print("*"*55)


#17.square of number
square = lambda num: num**2
print(square(4))  # Output: 16
print("*"*55)

#18. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda.

lst = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
result = list(filter(lambda x: x % 19 == 0 or x % 13 == 0, lst))
print(result)


#19. Write a Python program to count the even and odd numbers in a given array of integers using Lambda.

lst = [1, 2, 3, 5, 7, 8, 9, 10]

even_count = len(list(filter(lambda x: x % 2 == 0, lst)))
odd_count = len(list(filter(lambda x: x % 2 != 0, lst)))
print(even_count)
print(odd_count)