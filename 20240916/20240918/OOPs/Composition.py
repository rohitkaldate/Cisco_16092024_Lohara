class Engine:
    def start(self):
        return "Engine started."

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition
    
    def start(self):
        return self.engine.start()

car1 = Car()
print(car1.start())  # Output: Engine started.