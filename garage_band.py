class Musician(name):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'My name is {self.name} and I play guitar'

    def __repr__(self):
        return f'Guitarist instance. Name = {self.name}'

    # Define a function to get the instrument
    def get_instrument(self):
        print("In superclass method: name:", self.name, "age:", self.age)

# Create a musician subclass
class Guitarist(Musician):
    def display2(self):
        self.instrument= "guitar"
        print("In subclass method: name:", self.instrument)

class Drummer(Musician):
    def display2(self):
        self.instrument= "guitar"
        print("In subclass method: name:", self.instrument)


class Band():
    pass
