### bfd soondays day 15continued 2018.04.19 ###
### Section 10: Project 11 - Lecture 70 (https://www.udemy.com/the-python-bible) ###

                                                        ### Project 11: Make your own bank ###

class Account():

    def __init__(self, name, balance, min_balance):
        self.name =  name
        self.balance =  balance
        self.min_balance = min_balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print ('Not enough funds.')

    def statement(self):
        print ('{}, your account balance is: ${}'.format(self.name, self.balance))

class Checking(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -200)

    def __str__(self):
        return ("{}'s Checkings account has ${}.".format(self.name, self.balance))

class Savings(Account):

    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = 0)

    def __str__(self):
        return ("{}'s Savings account has ${}.".format(self.name, self.balance))

manny_c = Checking('Manny', 100)        ##instance of the class
manny_s = Savings('Manny', 1800)
gushi_c = Checking('Gushi', 234000)
gushi_s = Savings('Gushi', 180000)

## Two instance of the class Checking and Savings were created

print (manny_c)                 # $100
manny_c.deposit(100)
print (manny_c)                 # $200
manny_c.withdraw(300)
print (manny_c, '\n')       # -$100

print (manny_s)                 # $1800
manny_s.withdraw(2000)
print (manny_s, '\n')       # $1800



gushi_s.statement()         ## method (.statement) has print function



