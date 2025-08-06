class Duck():

    def quack(self):
        return f"{self.__class__.__name__} goes Quack"

    def swim(self):
        return f"{self.__class__.__name__} justs keeps swiming, justs keeps swiming"

    def display(self):
        return f"Looks like a {self.__class__.__name__}"

    def __str__(self):
        return self.__class__.__name__


class MallardDuck(Duck):
    def display(self):
        return super().display()
    
class RedheadDuck(Duck):
    def display(self):
        return super().display()


duck = MallardDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())
print()

duck = RedheadDuck()
print(duck.display())
print(duck.quack())
print(duck.swim())