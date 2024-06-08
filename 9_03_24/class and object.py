class Person: #class er por 1st word capital, class key word,person classs er name
    def __init__(self, name , age): #init er por self nisi specalized korar jonno,init constractor
          self.name=name
          self.age=age
    def introduce(self):
         print(f'the name of the student is {self.name} and he is {self.age} years old') 
         
student = Person('tota' ,22.5) #student holo object, parametar name and age

student.introduce()


