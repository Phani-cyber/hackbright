"""Discussion Questions

1. What are the three main design advantages that object orientation
   can provide? Explain each concept.

(replace this with your answer)
Encapsulation Enforces Modularity.
Encapsulation: Using OOP in Python, we can restrict access to methods and variables. 
This prevents data from direct modification which is called encapsulation. 
In Python, we denote private attributes using underscore as the prefix i.e single _ or double __ .

Inheritance Passes "Knowledge" Down.
 Inheritance allows us to define a class that inherits all the methods and properties from another class
 Child class is the class that inherits from another class, also called derived class. ..
 Parent class is the class being inherited from, also called base class.


Polymorphism Takes any Shape.
he literal meaning of polymorphism is the condition of occurrence in different forms.

Polymorphism is a very important concept in programming. It refers to the use of a single type entity (method, operator or object) to represent different types in different scenarios.


2. What is a class?
Python is an object oriented programming language. Almost everything in Python is an object, with its properties and methods. 
A Class is like an object constructor, or a "blueprint" for creating objects.


3. What is a method?
A method in python is somewhat similar to a function, except it is associated with object/classes. Methods in python are very similar to functions except for two major differences.

The method is implicitly used for an object for which it is called.

The method is accessible to data that is contained within the class

(replace this with your answer)


4. What is an instance in object orientation?
An instance, in object-oriented programming (OOP), is a specific realization of any object. An object may be varied in a number of ways. 
Each realized variation of that object is an instance. The creation of a realized instance is called instantiation.

Each time a program runs, it is an instance of that program. In languages that create objects from classes, an object is an instantiation of a class. 
That is, it is a member of a given class that has specified values rather than variables. 
In a non-programming context, you could think of "dog" as a class and your particular dog as an instance of that class.


5. How is a class attribute different than an instance attribute?
   Give an example of when you might use each.

The difference is that class attributes is shared by all instances.
When you change the value of a class attribute, it will affect all instances that share the same exact value. 
The attribute of an instance on the other hand is unique to that instance.
class ExampleClass(object):
    class_attr = 0
    def __init__(self, instande_attr):
        self.instance_attr = instance_attr
instance_attr is an instance attribute defined inside the constructor.

class_attr  is a class attribute defined outside the constructor.

""2. Road Class"""

class Road():

    def __init__(self , num_lanes=2 , speed_limit=25):
        
        self.num_lanes = num_lanes
        self.speed_limit = speed_limit
road_1 = Road()
road_2 =Road()
print (road_1.num_lanes, road_1.speed_limit)
road_1.num_lanes = 4
road_1.speed_limit = 60
print (road_1.num_lanes, road_1.speed_limit)
# Replace this with your code


"""3. Update Password"""


class User(object):
    """A user object."""

    def __init__(self, username, password):
        """create a user with the given username and password."""

        self.username = username
        self.password = password
    def update_password(self, new_password):
        if(self.password == new_password):
            print("Same Password")
        else:
            self.password = new_password
            print("password changed")
user = User('username', 'password')

user.update_password('new')

"""4. Build a Library"""
class Library:
    def __init__(self, books):
        self.books = []
    
    def create_and_add_book(self, title, author):
        book_object = Book(title, author)
        self.books.append(book_object)
    
    def find_books_by_author(self, author):
        list_of_books = []
        for book in self.books:
            if book.author == author:
                list_of_books.append(book.title)
        return list_of_books



class Book(object):
    """A Book object."""

    def __init__(self, title, author):
        """Create a book with the given title and author."""

        self.title = title
        self.author = author

    #def check_author(self):
    #    return self.author
    #def check_title(self):
    #    return self.title
    
#print(book.check_author)
book_list = []
library = Library(book_list)
library.create_and_add_book('title', 'author')
library.create_and_add_book('title2', 'author2')
library.create_and_add_book('title3', 'author')
library.create_and_add_book('title4', 'author')
print(library.find_books_by_author('author'))

"""5. Rectangle"""


class Rectangle:
    """A rectangle."""

    def __init__(self, length, width):
        """Create a rectangle with the given length and width."""

        self.length = float(length)
        self.width = float(width)

    def calculate_area(self):
        """Return the area of the rectangle."""
        return self.length * self.width
class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(length, width)
    

    def area_square(self):
        if(self.width == self.length):
            return self.width * self.length
        else:
            print("Not a square")

square = Square(5,6)
print(square.area_square())








