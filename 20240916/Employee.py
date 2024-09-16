class Employee:
    def __init__(self, name, address, code, salary):
        self.name= name
        self.address= address
        self.code= code
        self.salary= salary
        
    def __str__(self):
            return f'{self.name}, {self.address}, {self.code}, {self.salary}'
        
        
rohit=Employee('Rohit','3809,Ashok Nagar','ABCD121314',300000)
print(rohit)