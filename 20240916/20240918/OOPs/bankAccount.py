class Account:
    def __init__(self,number,name,initial_amount=1000):
        self.__number= number
        self.__name= name
        self.__balance= initial_amount     
    def __repr__(self):
        return f'[number= {self.__number},name= {self.__name},balance= {self.__balance}]'
    def __str__(self):
        return self.__repr__()
    def deposit(self,amount):
        self.__balance += amount
    def withdraw(self,amount):
        if amount > self.__balance:
            print("not enough balance")
            return
        self.__balance -= amount
        
raj_ac= Account(name= 'Raj',number= '3739111945',initial_amount= 3000)
print(raj_ac)#balance=3000

raj_ac.deposit(200000)
print(raj_ac)

raj_ac.deposit(10000)
print(raj_ac)

raj_ac.withdraw(50000)
print(raj_ac)
print(raj_ac.__dict__)

#print(raj_ac.__balance) #err

raj_ac.withdraw(200000)
print(raj_ac)

