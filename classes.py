class Dog():


    def __init__(self,breed,name):
        self.breed = breed
        self.name = name

    def bark(self):
        print(f"woof! my name is {self.name}")
        
    
dog = Dog(  "husky","manga")
print(dog.breed)
dog.bark()


class Circle():

    pi = 3.14
    def __init__(self,radius = 1):
        self.radius = radius
        self.area = radius* radius*Circle.pi


    #method
    def get_circumfrence(self):
        return self.radius * Circle.pi * 2
    
    

my_circle = Circle(30)
print(my_circle.get_circumfrence())
print(my_circle.area )  