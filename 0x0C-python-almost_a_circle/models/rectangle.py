#!/usr/bin/python3
'''Create Class Rectangle'''
from models.base import Base


class Rectangle(Base):
    '''Define Class Rectangle that inhertance from Base'''
    def __init__(self, width, height, x=0, y=0, id=None):
        '''constrector'''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''Width of this rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        '''Height of this rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        '''x of this rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        '''y of this rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        '''Computes area of this rectangle.'''
        return self.width * self.height

    def display(self):
        '''Prints string representation of this rectangle.''' 
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x, end="")
            for _ in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        '''Returns string info about this rectangle.'''
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        '''Update the args of the rectangle'''
        if args and len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        elif kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value

