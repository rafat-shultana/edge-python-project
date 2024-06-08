class Person:
    def __init__(self, name=None, age=None):
        if name is None:
             name = input('Enter your name: ')
        if age is None:
            age = input('Enput your age: ')     
        self.name = name
        self.age =age
        print('this is the init function!')


    def introduce(self):
        print(f'I am {self.name} and {self.age} years old')

# from app import Person 
# person1 = Person()
# person1.introduce()
        

