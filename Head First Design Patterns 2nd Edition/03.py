class Duck():
    def quack(self):
        return f"{self.__class__.__name__} goes Quack"

    def swim(self):
        return f"{self.__class__.__name__} justs keeps swiming, justs keeps swiming"

    def display(self):
        return f"Looks like a {self.__class__.__name__}"
    
    def fly(self):
        return f"{self.__class__.__name__} is flying high"

    def __str__(self):
        return self.__class__.__name__


class MallardDuck(Duck):
    def display(self):
        return super().display()


class RedheadDuck(Duck):
    def display(self):
        return super().display()

class RubberDuck(Duck):
    def display(self):
        return super().display()
    
    def quack(self):
        return f"{self.__class__.__name__} goes Squeak"
        

# added decoy duck class
class DecoyDuck(Duck):
    def display(self):
        return super().display()
    
    def quack(self):
        pass

    def fly(self):
        pass
    
    

duck = MallardDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())
print()

duck = RedheadDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())
print()

duck = RubberDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())
print()

# added Decoy duck print statements
duck = DecoyDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())      

""" 
problems with this approach:
- code dupllicartion accross classes
- runtime behavior changes are difficult
- hard to gain knowledge of all duck behaviours
- changes to existing duck types can break existing code
- violates Open/Closed Principle (OCP) of SOLID principles
"""
