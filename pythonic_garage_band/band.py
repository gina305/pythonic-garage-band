# Create a musician subclass
class Musician:

    def __init__(self, name="unknown"):
        self.name = name
        self.instrument = ""

    def __repr__(self):
        return f'{self.position} instance. Name = {self.name}'


    def __str__(self):
        return f'My name is {self.name} and I play {self.instrument}'


    def get_instrument(self):
        return f'{self.instrument}'


class Bassist(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.position = "Bassist"
        self.instrument = "bass"

        # Call the super init from Musician classs
        super().__repr__()


# Define a type of musician (relationship to the musician class
class Guitarist(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.position = "Guitarist"
        self.instrument = "guitar"


        # Call the super init from Musician classs
        super().__repr__()

#
    # @staticmethod - Static is unchanging (FOR GENERAL UNCHNGING OBJECT PROPERTIES)
    # Good for changing states/properties of generated object instances (i.e. weight
    # Class Method - methods that are called on the class itself, not on a specific object instance.





class Drummer(Musician):
    def __init__(self, name="unknown"):
        self.name = name
        self.position = "Drummer"
        self.instrument = "drums"

        # Call the super init from Musician class
        super().__repr__()



 # Change default memory address output of the Bassist object to a string
        def __repr__(self):
            return f'Person("{self.first_name}","{self.last_name}",{self.age})'


'''A Band instance should have a members attribute which is a list of instances that inherit from Musician base (or super) class.
'''


class Band():
    def __init__(self, name="unknown", instances=[]):
        self.name = name
        self.members = []
        self.all_bands = instances

    @classmethod
    def to_list():
        return 0


