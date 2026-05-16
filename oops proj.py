#1.program to create a class representing a Circle. Include methods to calculate its area and perimeter.

class Circle:

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius*self.radius

    def perimeter(self):
        return 2*3.14*self.radius

c = Circle(5)

print("Area of circle:", c.area())
print("Perimeter (Circumference) of circle:", c.perimeter())



#2.Write a Python program to create a calculator class. Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self, a,b):
        self.a = a
        self.b = b
    def add(self):
        return self.a +self.b
    def sub(self):
        return self.a - self.b
    def multiply(self):
        return self.a * self.b
    def divide(self):
        return self.a / self.b
c=Calculator(10,20)
print(c.add())
print(c.sub())
print(c.multiply())
print(c.divide())


#3. Employee Salary Calculation

class Employee:

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def annual_salary(self):
        print(self.salary * 12)

e1 = Employee("Sakshi",25000)

e1.annual_salary()

#4.Create Bank class with deposit,withdraw,balance check Use private variable.

class Bank:

    def __init__(self,balance):

        self.__balance = balance

    def deposit(self,amount):

        self.__balance += amount

        print("Deposited Successfully")

    def withdraw(self,amount):

        if amount <= self.__balance:

            self.__balance -= amount

            print("Withdraw Successful")

        else:
            print("Insufficient Balance")

    def show_balance(self):

        print("Balance :",self.__balance)

b1 = Bank(5000)

b1.deposit(1000)
b1.withdraw(2000)

b1.show_balance()



# 5. Write a Python program to create a class and show students marks details.

class Student :
	course='Data Science'
	trainer='Vaibhav Patil'
	institute='JBK'
	def __init__(self,rll,nm,ct):
		#instance attribute
		self.roll=rll
		self.name=nm
		self.city=ct
		self.marks={}
	def student_details(self):
		data=f'''
        Name   :  {self.name}
        Roll   :  {self.roll}
        City   :  {self.city}
        Course :  {Student.course}
        Trainer:  {Student.trainer}
        '''
		print(data)

	def add_marks(self,testname,marks):
		self.marks[testname]=marks
		return 'done'

	def total_obt(self):
		all_marks=list(self.marks.values())
		obt=sum(all_marks)
		return obt

	def total_marks(self):
		total=len(self.marks)*100
		return total

	def percentage(self):
		obt=self.total_obt()
		total=self.total_marks()
		per=(obt/total)*100
		return per

	def result(self):
		per=self.percentage()
		if per>=40:
			return 'Pass'
		else:
			return 'Fail'

s1=Student(1,'pavan','pune')
s2=Student(2,'pranav','mumbai')
s1.student_details()
s1.add_marks('t1',89)
s1.add_marks('t2',79)
s1.add_marks('t3',82)
print(s1.percentage())
print(s1.result())



# 6. Write a Python program to create a class and show the account details.

from datetime import datetime

class Account:
    bank_name = 'State Bank Of India'
    branch = 'Karve Nagar,Pune'
    ifsc_code = 'SBIN000897'
    account_count = 602276677100

    def __init__(self, name, balance):
        self.name = name
        Account.account_count = Account.account_count + 1
        self.account = Account.account_count
        self.balance = balance
        self.transactions = {}  # {101 : {'type':'debit','amount':20000,'date':'2 dec'}}

    def account_details(self):
        details = f'''
				Bank Name:   {Account.bank_name} Branch : {Account.branch} IFSC_CODE :{Account.ifsc_code}
				Name     :   {self.name}
				Account  :   {self.account}
				Balance  :   {self.balance}
			'''
        print(details)

    def check_balance(self):
        return f'Available balance is {self.balance}'

    def add_transaction(self, type, amount):
        tr_id = len(self.transactions) + 101
        self.transactions[tr_id] = {'type': type, 'amount': amount, 'date': str(datetime.now())}

    def deposit(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            self.balance += amount
            self.add_transaction('deposit', amount)
            return 'done '

        else:
            return 'invalid amount'

    def withdraw(self, amount):
        if isinstance(amount, (int, float)) and amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.add_transaction('withdraw', amount)
                return 'done'
            else:
                return 'insufficient balance'
        else:
            return 'invalid amount'

    def display_transactions(self):
        print('-' * 100)
        print(f'|{'Id':^20}|{'Type':^20}|{'Amount':^20}|{'DateTime':^30}|')
        print('-' * 100)
        for id in self.transactions:
            print(
                f'|{id:^20}|{self.transactions[id]['type']:^20}|{self.transactions[id]['amount']:^20}|{self.transactions[id]['date']:^30}|')
            print('-' * 100)


bhushan = Account('Bhushan Patil', 20000)
kunal = Account('Kunal Kale', 10000)
vijay = Account('vijay Chopde', 40000)

vijay.account_details()
print(vijay.check_balance())
vijay.deposit(50000)
vijay.withdraw(5000)

vijay.display_transactions()




