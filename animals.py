#!/usr/bin/python3


class Animal:
    def __init__(self, specie="none", name="", age=1):
        self.name = name
        self.specie = specie
        self.age = age

    @property
    def specie(self):
        return (self.__specie)

    @specie.setter
    def specie(self, value):
        if not isinstance(value, str):
            raise TypeError("specie must be a string")
        self.__specie = value

    @property
    def name(self):
        return (self.__name)

    @specie.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def age(self):
        return (self.__age)

    @specie.setter
    def name(self, value):
        if not isinstance(value, int):
            raise TypeError("name must be a int")
        elif value < 0:
            raise ValueError("age must be >=0")
        self.__age = value

    @classmethod
    def move(self):
        return print("I'm moving")

    @classmethod
    def show(self):
        return print("≧◠ᴥ◠≦")

    @classmethod
    def sound(self):
        return print("My sound is: Wof!") 



class Aquatic(Animals):
    def __init__(self, specie="none", name="", age=1):
        self.name = name
        self.specie = specie
        self.age = age

    @property
    def specie(self):
        return (self.__specie)

    @specie.setter
    def specie(self, value):
        if not isinstance(value, str):
            raise TypeError("specie must be a string")
        self.__specie = value

    @property
    def name(self):
        return (self.__name)

    @specie.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def age(self):
        return (self.__age)

    @specie.setter
    def name(self, value):
        if not isinstance(value, int):
            raise TypeError("name must be a int")
        elif value < 0:
            raise ValueError("age must be >=0")
        self.__age = value

class Fish(Aquatic):
    def __init__(self, specie="none", name="", age=1): 
        self.name = name
        self.specie = specie
        self.age = age

    @property
    def specie(self):
        return (self.__specie)

    @specie.setter
    def specie(self, value):
        if not isinstance(value, str):
            raise TypeError("specie must be a string")
        self.__specie = value

    @property
    def name(self):
        return (self.__name)

    @specie.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def age(self):
        return (self.__age)

    @specie.setter
    def name(self, value):
        if not isinstance(value, int):
            raise TypeError("name must be a int")
        elif value < 0:
            raise ValueError("age must be >=0")
        self.__age = value


class Starfish(Aquatic):
    def __init__(self, specie="none", name="", age=1):
        self.name = name
        self.specie = specie
        self.age = age

    @property
    def specie(self):
        return (self.__specie)

    @specie.setter
    def specie(self, value):
        if not isinstance(value, str):
            raise TypeError("specie must be a string")
        self.__specie = value

    @property
    def name(self):
        return (self.__name)

    @specie.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self.__name = value

    @property
    def age(self):
        return (self.__age)

    @specie.setter
    def name(self, value):
        if not isinstance(value, int):
            raise TypeError("name must be a int")
        elif value < 0:
            raise ValueError("age must be >=0")
        self.__age = value




